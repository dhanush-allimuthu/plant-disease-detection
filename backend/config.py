CLASSES = [
    "Apple Apple scab",
    "Apple Black rot",
    "Apple Cedar apple rust",
    "Apple healthy",

    "Blueberry healthy",

    "Cherry (including sour) Powdery mildew",
    "Cherry (including sour) healthy",

    "Corn (maize) Cercospora leaf spot Gray leaf spot",
    "Corn (maize) Common rust",
    "Corn (maize) Northern Leaf Blight",
    "Corn (maize) healthy",

    "Grape Black rot",
    "Grape Esca (Black Measles)",
    "Grape Leaf blight (Isariopsis Leaf Spot)",
    "Grape healthy",

    "Orange Haunglongbing (Citrus greening)",

    "Peach Bacterial spot",
    "Peach healthy",

    "Pepper bell Bacteria spot",
    "Pepper,_bell healthy",

    "Potato Early blight",
    "Potato Late blight",
    "Potato healthy",

    "Raspberry healthy",

    "Soybean healthy",

    "Squash Powdery mildew",

    "Strawberry Leaf scorch",
    "Strawberry healthy",

    "Tomato Bacterial spot",
    "Tomato Early blight",
    "Tomato Late blight",
    "Tomato Leaf Mold",
    "Tomato Septoria leaf spot",
    "Tomato Spider mites Two-spotted spider mite",
    "Tomato Target Spot",
    "Tomato Tomato mosaic virus",
    "Tomato Tomato Yellow Leaf Curl Virus",
    "Tomato healthy"
]
MEDICINE_DB = {

    "Apple Apple scab": {
        "organic": ["Neem oil spray", "Sulfur spray"],
        "chemical": ["Captan", "Mancozeb"],
        "precautions": ["Remove infected leaves", "Improve air circulation"]
    },
    "Apple Black rot": {
        "organic": ["Prune infected branches", "Neem oil"],
        "chemical": ["Copper fungicide"],
        "precautions": ["Avoid water on leaves", "Destroy fallen leaves"]
    },
    "Apple Cedar apple rust": {
        "organic": ["Neem oil"],
        "chemical": ["Myclobutanil"],
        "precautions": ["Remove nearby juniper hosts", "Improve airflow"]
    },
    "Apple healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Blueberry healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Cherry (including sour) Powdery mildew": {
        "organic": ["Neem oil", "Baking soda spray"],
        "chemical": ["Sulfur fungicide"],
        "precautions": ["Avoid leaf wetness", "Ensure ventilation"]
    },
    "Cherry (including sour) healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Corn (maize) Cercospora leaf spot Gray leaf spot": {
        "organic": ["Neem oil"],
        "chemical": ["Strobilurin fungicide"],
        "precautions": ["Crop rotation", "Destroy infected debris"]
    },
    "Corn (maize) Common rust": {
        "organic": ["Neem oil"],
        "chemical": ["Triazole fungicide"],
        "precautions": ["Use resistant varieties"]
    },
    "Corn (maize) Northern Leaf Blight": {
        "organic": ["Neem oil"],
        "chemical": ["Azoxystrobin"],
        "precautions": ["Good spacing", "Crop rotation"]
    },
    "Corn (maize) healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Grape Black rot": {
        "organic": ["Prune affected leaves", "Neem oil"],
        "chemical": ["Myclobutanil"],
        "precautions": ["Improve airflow", "Avoid overhead watering"]
    },
    "Grape Esca (Black Measles)": {
        "organic": ["Remove infected wood"],
        "chemical": [],
        "precautions": ["Prune properly", "Maintain plant health"]
    },
    "Grape Leaf blight (Isariopsis Leaf Spot)": {
        "organic": ["Neem oil"],
        "chemical": ["Copper fungicide"],
        "precautions": ["Destroy infected leaves"]
    },
    "Grape healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Orange Haunglongbing (Citrus greening)": {
        "organic": ["Remove infected branches"],
        "chemical": [],
        "precautions": ["Control psyllid insects", "Use disease-free plants"]
    },

    "Peach Bacterial spot": {
        "organic": ["Neem oil"],
        "chemical": ["Copper fungicide"],
        "precautions": ["Avoid wet leaves"]
    },
    "Peach healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Pepper bell Bacteria spot": {
        "organic": ["Neem spray weekly"],
        "chemical": ["Copper fungicide"],
        "precautions": ["Avoid water splash"]
    },
    "Pepper,_bell healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Potato Early blight": {
        "organic": ["Neem oil spray"],
        "chemical": ["Chlorothalonil"],
        "precautions": ["Healthy watering practice"]
    },
    "Potato Late blight": {
        "organic": ["Neem oil", "Remove infected leaves"],
        "chemical": ["Copper fungicide"],
        "precautions": ["Avoid overwatering"]
    },
    "Potato healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Raspberry healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Soybean healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Squash Powdery mildew": {
        "organic": ["Neem oil", "Milk spray"],
        "chemical": ["Sulfur fungicide"],
        "precautions": ["Improve airflow"]
    },

    "Strawberry Leaf scorch": {
        "organic": ["Remove infected leaves"],
        "chemical": ["Captan"],
        "precautions": ["Avoid water on leaves"]
    },
    "Strawberry healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    },

    "Tomato Bacterial spot": {
        "organic": ["Neem oil regularly"],
        "chemical": ["Copper based fungicide"],
        "precautions": ["Avoid water splashing"]
    },
    "Tomato Early blight": {
        "organic": ["Neem oil", "Baking soda spray"],
        "chemical": ["Copper fungicide"],
        "precautions": ["Remove infected leaves"]
    },
    "Tomato Late blight": {
        "organic": ["Neem oil spray", "Remove infected leaves", "Maintain dry leaves"],
        "chemical": ["Mancozeb", "Chlorothalonil"],
        "precautions": ["Avoid overhead watering", "Ensure airflow"]
    },
    "Tomato Leaf Mold": {
        "organic": ["Use neem oil", "Improve ventilation"],
        "chemical": ["Chlorothalonil"],
        "precautions": ["Avoid moisture on leaves"]
    },
    "Tomato Septoria leaf spot": {
        "organic": ["Neem oil"],
        "chemical": ["Chlorothalonil"],
        "precautions": ["Remove damaged leaves"]
    },
    "Tomato Spider mites Two-spotted spider mite": {
        "organic": ["Neem oil", "Water spray to wash mites"],
        "chemical": ["Miticide"],
        "precautions": ["Maintain humidity"]
    },
    "Tomato Target Spot": {
        "organic": ["Neem oil"],
        "chemical": ["Chlorothalonil"],
        "precautions": ["Avoid leaf wetness"]
    },
    "Tomato Tomato mosaic virus": {
        "organic": [],
        "chemical": [],
        "precautions": ["Remove infected plant", "Disinfect tools"]
    },
    "Tomato Tomato Yellow Leaf Curl Virus": {
        "organic": [],
        "chemical": [],
        "precautions": ["Control whiteflies", "Remove infected plants"]
    },
    "Tomato healthy": {
        "organic": [],
        "chemical": [],
        "precautions": ["Healthy plant. Maintain regular care."]
    }
}
