import os
import warnings

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

import tensorflow as tf

print("TensorFlow version:", tf.__version__)
print(tf.reduce_sum(tf.random.normal([1000, 1000])))
#TensorFlow version: 2.17.0
# tf.Tensor(-1190.2538, shape=(), dtype=float32)

#Load a dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build a machine learning model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
#predictions
#array([[ 0.19408129,  1.2371969 ,  0.06291097, -0.4625428 ,  0.08895354,
#         0.61576784, -0.01314712, -0.6106871 , -0.02804303, -0.05408379]],
#      dtype=float32)

tf.nn.softmax(predictions).numpy()
#array([[0.0952424 , 0.27030227, 0.08353409, 0.04939263, 0.08573811,
#        0.14519994, 0.07741626, 0.04259159, 0.07627162, 0.07431109]],
#      dtype=float32)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
#1.9296435

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# Train and evaluate your model
model.fit(x_train, y_train, epochs=5)
#Epoch 1/5
#1875/1875 ━━━━━━━━━━━━━━━━━━━━ 6s 3ms/step - accuracy: 0.8546 - loss: 0.4918
#Epoch 2/5
#1875/1875 ━━━━━━━━━━━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9550 - loss: 0.1542
#Epoch 3/5
#1875/1875 ━━━━━━━━━━━━━━━━━━━━ 6s 3ms/step - accuracy: 0.9655 - loss: 0.1139
#Epoch 4/5
#1875/1875 ━━━━━━━━━━━━━━━━━━━━ 6s 3ms/step - accuracy: 0.9714 - loss: 0.0885
#Epoch 5/5
#1875/1875 ━━━━━━━━━━━━━━━━━━━━ 6s 3ms/step - accuracy: 0.9773 - loss: 0.0720

model.evaluate(x_test,  y_test, verbose=2)
#313/313 - 1s - 2ms/step - accuracy: 0.9795 - loss: 0.0714
#[0.07136622071266174, 0.9794999957084656]

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])
probability_model(x_test[:5])
#<tf.Tensor: shape=(5, 10), dtype=float32, numpy=
#array([[1.8339530e-09, 3.1580915e-11, 4.2249038e-08, 3.1699299e-05,
#        5.0762404e-16, 1.6639514e-09, 6.8974412e-16, 9.9996817e-01,
#        2.4228599e-09, 9.2040978e-08],
#       [2.5973312e-11, 8.0671416e-06, 9.9999177e-01, 1.8524943e-07,
#        1.7679048e-26, 3.1198656e-08, 1.9687084e-10, 1.4972042e-20,
#        3.8471573e-09, 4.3744702e-19],
#       [2.3742479e-09, 9.9995065e-01, 6.3384516e-07, 4.1453593e-08,
#        9.0594227e-07, 4.0813717e-08, 2.1907526e-05, 1.5785812e-05,
#        1.0058512e-05, 1.1543606e-09],
#       [9.9999297e-01, 9.5381559e-13, 2.0272655e-07, 1.3014569e-10,
#        3.0518990e-10, 1.4884679e-08, 6.5601744e-06, 1.3750275e-07,
#        2.0468620e-10, 1.7288009e-07],
#       [3.9699387e-07, 1.3512171e-10, 5.9868853e-06, 1.6296971e-08,
#        9.6969795e-01, 1.2552491e-07, 8.1775703e-08, 4.3762723e-04,
#        7.3606102e-06, 2.9850516e-02]], dtype=float32)>
