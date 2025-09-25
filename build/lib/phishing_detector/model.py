import os
print(f"[DEBUG] model.py loaded from: {__file__}")
import joblib
from phishing_detector.features import extract_features

def predict_url(url: str) -> str:
    """
    Predict if a given URL is a phishing attempt or a legitimate website.
    """

    # 💡 Get current working directory instead of __file__-based logic
    project_root = os.getcwd()  # or use pathlib.Path.cwd()
    model_path = os.path.join(project_root, 'model', 'phishing_model.pkl')

    print(f"[DEBUG] Resolved model path: {model_path}")  # Add this for verification

    # Check if model file exists
    if not os.path.exists(model_path):
        return f"[ERROR] Model file not found at: {model_path}\nPlease ensure the model exists."

    try:
        model = joblib.load(model_path)
    except EOFError:
        return f"[ERROR] Failed to load model — file is corrupted: {model_path}"
    except Exception as e:
        return f"[ERROR] Unexpected error loading model: {str(e)}"

    try:
        url_features = extract_features(url)
    except Exception as e:
        return f"[ERROR] Failed to extract features from URL: {str(e)}"

    try:
        prediction = model.predict([url_features])[0]
        return "Phishing" if prediction == 1 else "Legitimate"
    except Exception as e:
        return f"[ERROR] Model failed to make prediction: {str(e)}"
