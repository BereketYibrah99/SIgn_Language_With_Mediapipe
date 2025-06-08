from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pickle

# Load and prepare data
data_dict = pickle.load(open('./data3.pickle', 'rb'))

# Convert data to uniform shape
max_length = max(len(item) for item in data_dict['data'])
padded_data = [np.pad(item, (0, max_length - len(item)), 'constant') for item in data_dict['data']]
data = np.array(padded_data)
labels = np.array(data_dict['labels'])

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Make predictions
y_predict = model.predict(x_test)

# Calculate accuracy
score = accuracy_score(y_test, y_predict)

# Print the accuracy
print('{}% of samples were classified correctly!'.format(score * 100))

# Save the model
with open('model9.p', 'wb') as f:
    pickle.dump({'model': model}, f)
