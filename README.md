``` A simple AI phishing Detector CLI```

```Installation Procedure```


# git clone htttps://github.com/username/AI-PHISHING-DETECTOR.git
# cd AI-PHISHING-DETECTOR


``` Create a Virtual environment```
# python -m venv venv
``` For Linux & mac```
# source venv/bin/activate
``` For Windows```
# venv\scripts\activate


```Install the Following packages Using```
# pip install -r requirements.txt
```you can install all this at once by using```
# pip install scikit-learn joblib tldextract pytest click black flakes8 pre-commit
```another package``
# pip install .

```After these The Phishing detector is good to go```
# phishing-detector -h  // It will show the cli interface with help menu
# phishing-detector <the url> // After the Scan it will show whether it is Legit Or phishing

```Sample```
# phishing-detector https://github.com
  ___________________________
 # / Let me analyze that URL! \
 #  \ Knowledge is power. 🦉    /
   ---------------------------
   #      \
   #       \
   #         ___
   #        (o,o)
   #        { "`"}
   #        -"--"-

# Welcome to the Phishing URL Detector CLI!

```🔍 Analyzing: https://github.com
🧠 Result: Legitimate