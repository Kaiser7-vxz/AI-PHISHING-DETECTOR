import os
import joblib
from phishing_detector.features import extract_features

def predict_url(url: str) -> str:
    """
    Let's find out if a URL is trying to trick us (phishing) or if it's safe to visit.

    Args:
        url (str): The website address you want to check.

    Returns:
        str: Either "Phishing" if it's suspicious, or "Legitimate" if it looks safe.
    """
    # First, let's locate our trusty model that knows how to spot phishing attempts.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, 'model', 'phishing_model.pkl')

    # Check if the model file is actually there.
    if not os.path.exists(model_path):
        return f"Oops! I couldn't find the model file at {model_path}. Please double-check that it exists."

    # Now, let's try to load the model. Fingers crossed it’s not corrupted!
    try:
        model = joblib.load(model_path)
    except EOFError:
        return f"Uh-oh, the model file at {model_path} seems to be corrupted. Try re-downloading it."
    except Exception as e:
        return f"Something went wrong while loading the model: {e}"

    # Next, we need to pull out features from the URL so the model knows what to look at.
    try:
        url_features = extract_features(url)
    except Exception as e:
        return f"Whoops! I couldn't extract features from the URL you gave me: {e}"

    # Finally, let's ask the model if the URL is phishing or safe.
    try:
        prediction = model.predict([url_features])[0]
        if prediction == 1:
            return "Phishing"
        else:
            return "Legitimate"
    except Exception as e:
        return f"Oops, the model couldn't make a prediction: {e}"
