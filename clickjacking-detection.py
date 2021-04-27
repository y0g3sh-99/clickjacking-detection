#Author: Yogesh Ingale
#Description: This script detects if the given website is vulnerable to clickjacking, and creates the proof-of-concept if --create-poc option is given from command line
#Reference and more info about this vulnerability: https://www.imperva.com/learn/application-security/clickjacking
 
import requests
import sys

def usage():
	print("\nUsage:\npython3 -u http(s)://your_test_website")
	print("python3 -u http(s)://your_test_website --create-poc")
	print("\n--create-poc optional flag is used for creating poc in html file named your_test_website.html\n\nJust run this file and you will see the contents of given url in this page in iframe.\nAnd that means given site is vulnerable to clickjacking\n")
	sys.exit(0)

def detect_vuln(url):
	tempurl = url
	if 'http' not in url:
        	tempurl = 'http://' + url
	flag = 0
	try:
		res = requests.get(tempurl, timeout=10)
		if 'x-frame-options' in res.headers:
			print("\n%s is not vulnerable\n"%url)
		else:
			print("\n%s is vulnerable to ClickJacking"%url) 
			flag = 1
	except:
		print("\nSomething went wrong, please check provided url and command line options\n")		
		sys.exit(1)

	if flag == 1 and '--create-poc' in sys.argv:
		create_poc_html_file(tempurl)

def create_poc_html_file(url):
	contents = """<html>
<head>
<title>ClickJack POC page</title>
</head>
<body>
<p>URL %s is vulnerable to ClickJacking!</p>
<iframe src="%s" width="600" height="600"></iframe>
</body>
</html>"""%(url,url)

	filename = (url + '.html').replace('http://','').replace('https://','')
	f = open(filename,"w")
	f.write(contents)
	f.close()
	print("\nCreated %s for poc.\nOpen this file in browser to verify the contents of given url are rendered in iframe\n"%filename)

def main():
	url = ''

	if '-u' not in sys.argv:
		usage()
	elif '-u' in sys.argv:
		for i in range(0,len(sys.argv)):
			if sys.argv[i] == '-u' and len(sys.argv) > i+1:
				url = sys.argv[i+1]
				break
		if url == '':
			usage()
	detect_vuln(url)

if __name__ == '__main__':
        main()
