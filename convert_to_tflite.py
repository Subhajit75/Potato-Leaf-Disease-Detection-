import tensorflow as tf

model = tf.keras.models.load_model("potato_disease_model.h5")

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save as .tflite
with open("potato_model.tflite", "wb") as f:
    f.write(tflite_model) 