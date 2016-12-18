'''
Solution for OWASP WebGoat, Authentication Flaws, Password Strength exercise.
Takes a list of passwords, submits them to a website that verifies their strength,
and returns the output.

NOTE: Doesn't work for the exercise website, but would work for a website that allows post requests.
'''

import requests

print("[+] Reading Wordlist")

wl = open("wordlist.txt", "r")
words = wl.readlines()
wl.close()

print(words)

target = "https://howsecureismypassword.net/"

cookieName1 = "something"
cookieValue1 = "something"
cookieName2 = "something"
cookieValue2 = "something"
cookies = {cookieName1: cookieValue1, cookieName2: cookieValue2}

req = requests.get(target, cookies=cookies)
if req.status_code != requests.codes.ok:
	raise ValueError('Poof! Unable to connect to target t(X_X)t')
else:
	print('+++ Connected to target. Starting operation...\n')

for word in words:
	word = word.rstrip("\n").rstrip("\r")
	data = word
	req = requests.get(target, cookies=cookies, data=data)
	print('+++ Successfully sent information.\n') 
	print(req.content)


