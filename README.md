# Python-Gesture-Game-Control

This project enables immersive and intuitive game control using hand gestures detected through a webcam. It leverages the power of OpenCV and Mediapipe for real-time hand tracking and gesture recognition, translating hand movements into corresponding in-game actions.

## Key Features

* **Real-time Hand Tracking:**  Accurately detects and tracks hand movements in real-time using OpenCV and Mediapipe.
* **Intuitive Gesture Mapping:**  Maps specific hand gestures to predefined game commands (left, right, up, down).
* **Customizable Control Region:**  The active control area is visually defined within the camera feed, allowing for personalized adjustments.
* **Cooldown Mechanism:**  Implements a cooldown timer to prevent unintended repeated actions from a single gesture.

## How it Works

1. **Hand Detection & Tracking:**  The `hand_tracking.py` module uses Mediapipe's hand tracking model to identify and track the user's hand within the camera frame.
2. **Landmark Extraction:** Key landmark points on the detected hand are extracted, providing coordinates for gesture analysis.
3. **Gesture Recognition:**  The `game_control.py` module analyzes the relative positions of specific landmarks to recognize predefined gestures.
4. **Command Execution:**  Recognized gestures trigger corresponding keyboard inputs, effectively controlling the game.

## Getting Started

### Prerequisites

* Python 3.9 and above
* OpenCV (`pip install opencv-python`)
* Mediapipe (`pip install mediapipe`)
* Keyboard (`pip install keyboard`) 

### Installation

1. Clone the repository: `git clone https://github.com/your-username/your-repo-name.git`
2. Navigate to the project directory: `cd your-repo-name`
3. Install the required libraries: `pip install -r requirements.txt`

### Running the Application

1. Ensure your webcam is connected and accessible.
2. Run the main script: `python game_control.py`
3. The application window will open, displaying the camera feed with the active control area.
4. Position your hand within the control area and perform gestures to control the game.

## Customization

* **Gesture Mapping:** You can modify the gesture-to-command mapping in the `game_control.py` script to suit your preferences.
* **Control Area:**  Adjust the coordinates defining the active control region in the `game_control.py` script to fine-tune the interactive space.
* **Cooldown Duration:**  Modify the `cooldown_duration` variable in `game_control.py` to adjust the delay between consecutive actions.
