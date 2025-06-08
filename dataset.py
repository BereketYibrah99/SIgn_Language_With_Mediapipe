import os
import pickle
import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data3'

data = []
labels = []

# Iterate through directories and image files
for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)
    
    # Ensure the item is a directory and not a hidden system file like .DS_Store
    if os.path.isdir(dir_path) and not dir_.startswith('.'):
        for img_file in os.listdir(dir_path):
            img_path = os.path.join(dir_path, img_file)
            
            # Ensure the item is a file and has an image extension
            if os.path.isfile(img_path) and img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                data_aux = []
                x_ = []
                y_ = []
                img = cv2.imread(img_path)
                if img is None:
                    print(f"Warning: Unable to read image {img_path}. Skipping.")
                    continue
                
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = hands.process(img_rgb)
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        #for i in range(len(hand_landmarks.landmark)):
                        #    x = hand_landmarks.landmark[i].x
                        #    y = hand_landmarks.landmark[i].y
                        #    x_.append(x)
                        #    y_.append(y)
                        # Normalize coordinates
                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y
                            data_aux.append(x)
                            data_aux.append(y)

                    # Only append data if landmarks are successfully extracted
                    data.append(data_aux)
                    labels.append(dir_)
print(data)
# Save data to a pickle file
with open('data9.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)

print("Data processing complete. Pickle file created.")
