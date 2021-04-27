# clickjacking-vulnerability-detection
Detects if the given URL is vulnerable to clickjacking vulnerability or not

This tool detects whether a given url is vulnerable to clickjacking vulnerability, and also creates a POC to verify the same.

Usage:

python3 clickjacking-detection.py -u test-website 

This will just print if the website is vulnerable or not.

OR

python3 clickjacking-detection.py -u test-website --create-poc

When --create-poc optional flag is used, it creates website.html file as POC.
We can then just open this file in browser and verify the contents of given url are rendered in iframe of created poc page.
This shows the vulnerability.

Reference: https://www.imperva.com/learn/application-security/clickjacking/

