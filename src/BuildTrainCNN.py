import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

import tensorflow as tf 
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, MaxPooling2D, Dense
import cv2
import numpy as np

print("TensorFlow", tf.__version__)

path = '/home/Chris/ocr_dataset/data/training_data'
images = []
labels = []

print('Build lists of images, labels from dataset')
dir_list = os.listdir(path)
for i in dir_list:
  dir = os.path.join(path, i)
  file_list = os.listdir(dir)
  for j in file_list:
    files = os.path.join(dir, j)
    img = cv2.imread(files)
    img = cv2.resize(img, (64,64))
    img = np.array(img, dtype=np.float32)
    img = img/255
    images.append(img)
    labels.append(i)
print(f"['E' 'E' 'E' 'E' 'E' 'E' ... '1' '1' '1' '1' '1' '1'] {len(labels)}\n")

print('Convert lists to NumPy arrays')
X = np.array(images)
y = np.array(labels)
print(f'{y} {len(y)}\n')

print('Label encoding')
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(f'{y} {len(y)}\n')

print('Shuffle arrays')
from sklearn.utils import shuffle
X_sh, y_sh = shuffle(X, y, random_state=42)
print(f'{y_sh} {len(y_sh)}\n')

print('Build NN model')
model = Sequential()
model.add(Conv2D(filters=16, kernel_size=(3,3), activation='relu', input_shape=(64,64,3)))
model.add(MaxPooling2D())
model.add(Conv2D(filters=32, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
#model.add(MaxPooling2D())
#model.add(Conv2D(filters=128, kernel_size=(3,3), activation='relu'))
model.add(Flatten())
#model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=36, activation='softmax'))
#print(f'{model.get_config()}\n')

print('Compile, train')
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(X_sh, y_sh ,validation_split=0.2, batch_size=16, epochs=5)

model.save('rff.tf', save_format='tf')

# load_model('rff.tf')



# print('\nTest model')
# test_images = []
# test_labels = []

# path = '/home/Chris/ocr_dataset/data/testing_data'

# dir_list = os.listdir(path)
# for i in dir_list:
#   dir = os.path.join(path, i)
#   file_list = os.listdir(dir)
#   for j in file_list:
#     files = os.path.join(dir, j)
#     img = cv2.imread(files)
#     img = cv2.resize(img, (64,64))
#     img = np.array(img, dtype=np.float32)
#     img = img/255
#     test_images.append(img)
#     test_labels.append(i)
# #print(f"['E' 'E' 'E' 'E' 'E' 'E' ... '1' '1' '1' '1' '1' '1'] {len(test_labels)}\n")
# print(f"{test_labels} {len(test_labels)}\n")

# print('Convert test lists to NumPy arrays')
# X_test = np.array(test_images)
# y_test = np.array(test_labels)
# print(f'{y_test} {len(y_test)}\n')

# print('Predict tests')
# preds = model.predict(X_test)
# predicted_labels = le.inverse_transform(np.argmax(preds, axis=1))
# print(f'{predicted_labels} {len(predicted_labels)}\n')

# #plt.imshow(X_test[197])
# #plt.title(f"Label: {predicted_labels[197]}")
# #plt.show()

# print('Evaluate test')
# y_test = le.fit_transform(y_test)
# test_loss, test_accuracy = model.evaluate(X_test, y_test)
# print(f"Accuracy {test_accuracy}")

