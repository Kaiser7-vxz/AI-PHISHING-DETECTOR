import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from phishing_detector.features import extract_features

def load_training_data(csv_path):
    """
    Load a CSV with 'url' and 'label' columns.
    Returns two lists: URLs and labels.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Training data not found at: {csv_path}")
    
    df = pd.read_csv(csv_path)
    if 'url' not in df.columns or 'label' not in df.columns:
        raise ValueError("CSV must contain 'url' and 'label' columns.")
    
    urls = df['url'].tolist()
    labels = df['label'].tolist()
    return urls, labels

def train_and_save_model():
    # Get the project root directory (one level above this script)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Define the absolute path to the training CSV data
    csv_path = os.path.join(project_root, 'data', 'phishing_data.csv')

    print("📦 Loading training data...")
    urls, labels = load_training_data(csv_path)

    print("🔍 Extracting features...")
    X = [extract_features(url) for url in urls]
    y = labels

    print("🧠 Training model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Define absolute path to save the model in project_root/model/
    model_dir = os.path.join(project_root, 'model')
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'phishing_model.pkl')

    print(f"💾 Saving model to {model_path}...")
    joblib.dump(model, model_path)

    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_and_save_model()
