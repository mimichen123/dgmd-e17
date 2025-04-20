from enum import Enum
import cv
import time
from PIL import Image
import numpy as np
import cv2
from typing import Tuple

# Mock car class to simulate motor control
class MockCar:
    def command_motor_pwms(self, left, right):
        print(f"Simulating motor control: left={left}, right={right}")

# States that the driver can be in.
class DriveState(Enum):
    STOPPED = 1
    ROLLING_INTO_INTERSECTION = 2
    IN_INTERSECTION = 3
    FOLLOWING_LANE = 4
    FINISHED = 5

class Driver:
    def __init__(self, arduino_interface):
        self.car = arduino_interface  # MockCar instance
        self.speed_limit = 10.0
        self.last_stop = False
        self.num_updates = 0
        self.start_time = None

        self.set_state(DriveState.FOLLOWING_LANE)
        self.needs_instruction = True
        self.next_turn = None

        self.red_roi = cv.red_roi
        self.green_roi = cv.green_roi
        self.green_roi.recenter(*self.red_roi.get_center())

    def set_state(self, new_state):
        print(f'State changed to {new_state}')
        self.state = new_state
        self.start_time = time.time()
        self.num_updates = 0
        
    def update(self, image):
        if self.needs_instruction:
            print('Driver needs instruction!')
            return

        self.num_updates += 1

        # Lane Following
        if self.state == DriveState.FOLLOWING_LANE:
            steering = compute_steering(image)
            
            # Use the computed steering to control the car's motors
            self.car.command_motor_pwms(self.speed_limit, steering)
        
        elif self.state == DriveState.STOPPED:
            # Implement stop logic or checking for green light
            pass

    def debug_image(self, image):
        print('Debugging image')
        cv.draw_region(image, self.red_roi, (255, 255, 255))
        cv.draw_region(image, self.green_roi, (255, 255, 0))
        Image.fromarray(image, 'RGB').show()


# Function to compute the steering based on lane markings
def compute_steering(image: np.ndarray) -> float:
    mask_left_edge, mask_right_edge = detect_lane_markings(image)
    
    # Get the steering weight matrices
    steer_matrix_left = get_steer_matrix_left_lane_markings(mask_left_edge.shape)
    steer_matrix_right = get_steer_matrix_right_lane_markings(mask_right_edge.shape)
    
    # Compute steering command by summing weighted masks
    steering = np.sum(steer_matrix_left * mask_left_edge) + np.sum(steer_matrix_right * mask_right_edge)
    
    return steering

def detect_lane_markings(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Detects the lane markings in the input image.
    Returns masks for yellow (left) and white (right) lane markings.
    """
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    yellow_lower = np.array([20, 100, 100], dtype=np.uint8)
    yellow_upper = np.array([30, 255, 255], dtype=np.uint8)
    white_lower = np.array([0, 0, 200], dtype=np.uint8)
    white_upper = np.array([180, 25, 255], dtype=np.uint8)

    mask_left_edge = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    mask_right_edge = cv2.inRange(hsv_image, white_lower, white_upper)

    return mask_left_edge, mask_right_edge

def get_steer_matrix_left_lane_markings(shape: Tuple[int, int]) -> np.ndarray:
    """
    Args:
        shape:              The shape of the steer matrix.

    Return:
        steer_matrix_left:  The steering (angular rate) matrix for Braitenberg-like control
                            using the masked left lane markings (numpy.ndarray)
    """
    rows, cols = shape
    steer_matrix_left = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            # The further right the yellow line is detected, the more negative the steering (turn right)
            steer_matrix_left[i, j] = -1 * (j / cols)

    return steer_matrix_left


def get_steer_matrix_right_lane_markings(shape: Tuple[int, int]) -> np.ndarray:
    """
    Args:
        shape:               The shape of the steer matrix.

    Return:
        steer_matrix_right:  The steering (angular rate) matrix for Braitenberg-like control
                             using the masked right lane markings (numpy.ndarray)
    """
    rows, cols = shape
    steer_matrix_right = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            # The further left the white line is detected, the more positive the steering (turn left)
            steer_matrix_right[i, j] = j / cols

    return steer_matrix_right


if __name__ == '__main__':
    # Example of using the mock car for testing
    mock_car = MockCar()
    driver = Driver(mock_car)
    
    # Simulating image input (use an actual image here)
    dummy_image = np.zeros((240, 320, 3), dtype=np.uint8)  # Placeholder image for testing

    # Run the update method with dummy image
    driver.update(dummy_image)
