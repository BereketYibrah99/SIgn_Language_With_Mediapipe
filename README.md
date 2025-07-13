# 🧠 Sign Language Recognition using MediaPipe + scikit-learn

This project implements an English alphabet sign language recognizer using hand keypoints extracted via **MediaPipe**. The keypoints are preprocessed by subtracting all values from the largest coordinate and then normalized. The resulting data is used to train a classifier with **scikit-learn** to predict hand gestures corresponding to English letters.

---

## 📌 Features

- Real-time hand detection and keypoint extraction using **MediaPipe**
- Keypoint preprocessing:
  - Subtract all coordinates from the largest value
  - Normalize for consistent scaling
- Uses **scikit-learn** models like KNN, SVM, or Random Forest for classification
- Recognizes static ASL alphabet signs (A–Y; excluding J and Z)

---

## 🛠️ Technologies Used

- Python
- [MediaPipe](https://google.github.io/mediapipe/)
- [scikit-learn](https://scikit-learn.org/)
- OpenCV
- NumPy



