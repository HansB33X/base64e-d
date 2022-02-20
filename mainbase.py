import base64
import os
import pyfiglet

os.system('pip install pyfiglet')
os.system('clear')

def main():
	logo = pyfiglet.figlet_format("BASE64")
	print(logo)
	print("decode / encode by HansB33X\n")
	inputpilihan = input("[1]Decode [2]Encode> ")
	if inputpilihan == "1":
		inputcode = input("code> ").encode()
		decode = base64.b64decode(inputcode)
		print(decode)
	if inputpilihan == "2":
		inputtext = input("text> ").encode()
		encode = base64.b64encode(inputtext)
		print(encode)
main()
