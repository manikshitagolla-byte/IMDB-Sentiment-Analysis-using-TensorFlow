import tensorflow as tf
import matplotlib.pyplot as plt

print("Script Started")
print("TensorFlow Version:", tf.__version__)

# Load IMDB dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(num_words=10000)

# Tokenization / Padding
x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=200)

x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen=200)

# Model
model = tf.keras.Sequential(
    [
        tf.keras.layers.Embedding(10000, 16, input_length=200),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(16, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ]
)

# Compile
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

print("Starting Training...")

# Train
history = model.fit(
    x_train, y_train, epochs=5, validation_data=(x_test, y_test), verbose=1
)

# Evaluate
loss, accuracy = model.evaluate(x_test, y_test)

print("\nTest Accuracy:", accuracy)

# Save Model
model.save("sentiment_model.h5")

# Plot Training Curves
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Training Curve")
plt.legend()
plt.grid(True)

plt.savefig("training_curve.png")
plt.show()

print("\nModel Saved Successfully")
print("Training Curve Saved Successfully")
