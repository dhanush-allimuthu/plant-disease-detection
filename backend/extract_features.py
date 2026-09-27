import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from config import CLASSES

IMG_SIZE = 224
BATCH_SIZE = 32

print("Loading MobileNetV2...")
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    pooling="avg",
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

print("Loading dataset...")
datagen = ImageDataGenerator(rescale=1./255)

data = datagen.flow_from_directory(
    "dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False,
    classes=CLASSES
)

print("Extracting features...")
features = base_model.predict(data)
labels = data.classes

np.save("ml_features.npy", features)
np.save("ml_labels.npy", labels)

print("✅ CNN Features Saved Successfully")
