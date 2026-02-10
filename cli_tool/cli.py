# filepath: cli_tool/cli.py

import argparse
from phishing_detector.model import predict_url

PROFESSOR_OWL_ASCII = r"""
  ___________________________
 / Let me analyze that URL! \
 \ Knowledge is power. 🦉    /
  ---------------------------
         \
          \
            ___
           (o,o)
           { "`"}
           -"--"-
"""

def print_welcome_message():
    print(PROFESSOR_OWL_ASCII)
    print("Welcome to the Phishing URL Detector CLI!\n")

def print_result(result, url):
    print(f"\n Analyzing: {url}")
    print(f" Result: {result}\n")

def main():
    print_welcome_message()

    parser = argparse.ArgumentParser(description="Phishing URL Detector")
    parser.add_argument("url", nargs="?", help="URL to check")
    args = parser.parse_args()

    if args.url:
        result = predict_url(args.url)
        print_result(result, args.url)
    else:
        print("No URL provided.\n")
        parser.print_help()

if __name__ == "__main__":
    main()
