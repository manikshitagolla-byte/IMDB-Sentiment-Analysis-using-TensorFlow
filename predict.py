import tensorflow as tf

model = tf.keras.models.load_model("sentiment_model.h5")

print("Model loaded successfully!")
