import subprocess
import re

def zsteg(location):
	#PNG
	f=open('REPORT.md','a')
	f.write('zsteg: \n')
	data = subprocess.run(['zsteg','-a',location],text=True,capture_output=True)
	data=data.stdout
	'''text = re.findall(r'text: ".*"',data)
	ctf=re.findall(r'\w+[ctf]{.+}|\w+[CTF]{.+}',data)
	for i in range(len(text)):
		text[i]=text[i][7:-1]
	f.write(text+'\n')
	f.write(ctf+'\n')'''
	f.write(data+'\n')
	f.close()

def strings(location):
	#PNG, JPEG
	f=open('REPORT.md','a')
	f.write('strings: \n')
	data=subprocess.run(['strings',location],text=True,capture_output=True)
	data=data.stdout
	'''text=re.findall(r'\w+',data)
	ctf=re.findall(r'\w+[ctf]{.+}|\w+[CTF]{.+}',data)
	f.write(text+'\n')
	f.write(ctf+'\n')'''
	f.write(data+'\n')
	f.close()

def xxd(location):
	#PNG, JPEG, TXT
	f=open('REPORT.md','a')
	f.write('xxd: \n')
	data=subprocess.run(['xxd','-p',location],text=True,capture_output=True)
	data=data.stdout
	f.write(data+'\n')
	f.close()

def exiftool(location):
	#PNG, JPEG, TXT
	f=open('REPORT.md','a')
	f.write('exiftool: \n')
	data=subprocess.run(['exiftool',location],text=True,capture_output=True)
	data=data.stdout
	f.write(data+'\n')
	f.close()