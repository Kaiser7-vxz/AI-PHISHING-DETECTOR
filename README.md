# AI Phishing Detector CLI

A simple yet powerful AI-based phishing URL detector that helps identify whether a URL is legitimate or malicious directly from your terminal.

---

## 🚀 Features

- Detect phishing URLs using machine learning  
- Fast and lightweight CLI tool  
- Model trained using URL-based features  
- Easy-to-use command-line interface  
- Fully installable Python package  

---

## 📂 Project Setup

1. Clone the Repository
```
git clone https://github.com/Kaiser7-vxz/AI-PHISHING-DETECTOR.git
cd AI-PHISHING-DETECTOR
```

2. Create a Virtual Environment
 ```
   python -m venv venv
```

Activate The Environment
For Linux / macOS
```
- source venv/bin/activate
```
For Windows
```
- venv\Scripts\activate   
```

3. Install Dependencies
```
pip install -r requirements.txt
```
Or install manually:
```
pip install scikit-learn joblib tldextract pytest click black flake8 pre-commit pandas whois
```
5. Install the Package
```
pip install .
```

7. Train the Model
```
cd model
```
then
```
python -c "from phishing_detector.train_model import train_and_save_model; train_and_save_model()"
```

9. Verify Model Creation
```
ls -l model/phishing_model.pkl
```

11. Move Model into Package
```
cp model/phishing_model.pkl phishing_detector/model/
```

13. Reinstall Package (Editable Mode)
```
pip install -e .
```

15. Final Verification
```
ls -l model/phishing_model.pkl
ls -l phishing_detector/model/phishing_model.pkl
```

17. Usage
```
phishing-detector -h
phishing-detector https://github.com
 ___________________________
/ Let me analyze that URL! \
\ Knowledge is power.     /
 ---------------------------
      \
       \
         ___
        (o,o)
        { "`"}
        -"--"-

Welcome to the Phishing URL Detector CLI!

Analyzing: https://github.com  
Result: Legitimate
```

⚙️ Tech Stack

1. Python
2. Scikit-learn
3. Pandas
4. Click (CLI interface)
5. Joblib (model persistence)

🛠️ Development Tools

1. Black (code formatting)
2. Flake8 (linting)
3. Pre-commit hooks
4. Pytest (testing)

---

## 🐳 Docker Setup (Alternative Method)

### Quick Start with Docker

1. **Build the Docker Image**
   ```bash
   docker build -t phishing-detector .
   ```

2. **Run the Container**
   ```bash
   # Check help
   docker run --rm phishing-detector

   # Analyze a URL
   docker run --rm phishing-detector "https://example.com"

   # Analyze a suspicious URL
   docker run --rm phishing-detector "http://secure-bank-login.suspicious-site.com"
   ```

### Using Docker Compose

1. **Build and Run**
   ```bash
   docker-compose up --build
   ```

2. **Run Commands**
   ```bash
   # Interactive mode
   docker-compose run --rm phishing-detector

   # Direct command
   docker-compose run --rm phishing-detector "https://github.com"
   ```

### Docker Image Details

- **Base Image**: Python 3.11 slim
- **System Dependencies**: whois, curl
- **Model Training**: Automatically trains the model during build
- **Security**: Runs as non-root user
- **Size**: Optimized for minimal footprint

### Docker Build Context

The `.dockerignore` file excludes:
- Development files (`.git`, `__pycache__`, IDE files)
- Build artifacts (`build/`, `dist/`, `*.egg-info/`)
- Test files and cache
- Temporary files

This ensures faster builds and smaller image sizes.
