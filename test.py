import pickle
import numpy as np
import cv2
import mediapipe as mp

# Load the trained model
model_dict = pickle.load(open('model9.p', 'rb'))
model = model_dict['model']

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.3, max_num_hands=2)

# Initialize video capture
cap = cv2.VideoCapture(0)

# Ensure that the labels match those used during model training
labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

def preprocess_data(data, max_length):
    # Pad data to ensure consistent feature size
    return np.array([np.pad(item, (0, max_length - len(item)), 'constant') for item in data])

# Determine the feature size used during training
max_length = 84  # Replace with the actual feature length used during training

while True:
    ret, frame = cap.read()
    if not ret:
        break

    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            data_aux = []
            x_ = []
            y_ = []

            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)

            # Normalize data and prepare it for prediction
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

            # Ensure data length matches the model's expected input
            if len(data_aux) < max_length:
                data_aux = np.pad(data_aux, (0, max_length - len(data_aux)), 'constant')
            elif len(data_aux) > max_length:
                data_aux = data_aux[:max_length]

            # Calculate bounding box
            x1 = int(min(x_) * W)-35
            y1 = int(min(y_) * H)-25
            x2 = int(max(x_) * W)+25
            y2 = int(max(y_) * H)+25

            # Preprocess data for prediction
            input_data = preprocess_data([data_aux], max_length)
            prediction = model.predict(input_data)

            # Map prediction to character
            predicted_character = labels_dict.get(int(prediction[0]), "Unknown")

            # Draw bounding box and text
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

    # Display the result
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
