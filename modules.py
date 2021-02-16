import subprocess
import re

def zsteg(location):
	#PNG
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
	data=subprocess.run(['strings',location],text=True,capture_output=True)
	data=data.stdout
	text=re.findall(r'\w+',data)
	ctf=re.findall(r'\w+[ctf]{.+}|\w+[CTF]{.+}',data)
	print(text)
	print(ctf)