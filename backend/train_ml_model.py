import numpy as np
import joblib
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.utils.class_weight import compute_class_weight
from config import CLASSES
import os

print("Loading extracted features...")
X = np.load("ml_features.npy")
y = np.load("ml_labels.npy")

print("Features shape:", X.shape)
print("Labels shape:", y.shape)

# Handle class imbalance
class_weights = compute_class_weight(
    class_weight="balanced",
    classes=np.unique(y),
    y=y
)
class_weight_dict = {cls: w for cls, w in zip(np.unique(y), class_weights)}

print("Training SVM Model...")
model = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC(
        kernel="rbf",
        probability=True,
        C=5,
        gamma="scale",
        class_weight=class_weight_dict
    ))
])

model.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/plant_ml_model.pkl")
joblib.dump(CLASSES, "model/classes.pkl")

print("✅ ML Model Trained & Saved Successfully")
