import subprocess
import re

def zsteg(location):
	#PNG
	print('zsteg: \n')
	data = subprocess.run(['zsteg','-a',location],text=True,capture_output=True)
	data=data.stdout
	text = re.findall(r'text: ".*"',data)
	ctf=re.findall(r'\w+[ctf]{.+}|\w+[CTF]{.+}',data)
	for i in range(len(text)):
		text[i]=text[i][7:-1]
	print(text)
	print(ctf)

def strings(location):
	#PNG, JPEG
	print('strings: \n')
	data=subprocess.run(['strings',location],text=True,capture_output=True)
	data=data.stdout
	text=re.findall(r'\w+',data)
	ctf=re.findall(r'\w+[ctf]{.+}|\w+[CTF]{.+}',data)
	print(text)
	print(ctf)

def xxd(location):
	#PNG, JPEG, TXT
	print('xxd: \n')
	data=subprocess.run(['xxd','-p',location],text=True,capture_output=True)
	data=data.stdout
	print(data)

def exiftool(location):
	#PNG, JPEG, TXT
	print('exiftool: \n')
	data=subprocess.run(['exiftool',location],text=True,capture_output=True)
	data=data.stdout
	print(data)