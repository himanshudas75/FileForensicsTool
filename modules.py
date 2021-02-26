import subprocess
import os.path
import re

def filename(location):		#for finding filename
	filename=re.findall(r'[^/]+',location)[-1]
	return filename

pwd=subprocess.run(['pwd'],text=True,capture_output=True)	#finding present working directory
pwd=pwd.stdout[:-1]

def cat(location):
	#TXT
	f=open('REPORT.md','a')
	f.write('**cat:** \n\n')
	data=subprocess.run(['cat',location],text=True,capture_output=True)
	data=data.stdout
	f.write(data+'\n')
	f.close()

def strings(location):
	#PNG, JPEG, BMP
	f=open('REPORT.md','a')
	f.write('**strings:** \n\n')
	data=subprocess.run(['strings',location],text=True,capture_output=True)
	data=data.stdout
	data=re.findall(r'.+',data)
	f.write('First four lines:\n')
	for i in range(4):
		f.write(data[i]+'\n')
	f.write('\nLast four lines:\n')
	for i in range(-4,0):
		f.write(data[i]+'\n')
	f.write('\n')
	f.close()

def binwalk(location):
	#PNG, JPEG
	f=open('REPORT.md','a')
	f.write('**binwalk:** \n')
	data=subprocess.run(['binwalk','-e',location],text=True,capture_output=True)
	data=data.stdout
	f.write(data)
	extdir=pwd+'/_'+filename(location)+'.extracted'
	if(os.path.isdir(extdir)):
		f.write('Embedded files extracted to: '+extdir+'/\n\n')
	f.close()

def zsteg(location):
	#PNG
	f=open('REPORT.md','a')
	f.write('**zsteg:** \n\n')
	data = subprocess.run(['zsteg','-a',location],text=True,capture_output=True)
	data=data.stdout
	text = re.findall(r'text: ".*"',data)
	for i in range(len(text)):
		text[i]=text[i][7:-1]
		f.write(text[i]+'\n')
	f.close()


def xxd(location):
	#PNG, JPEG, TXT, BMP
	f=open('REPORT.md','a')
	f.write('**xxd:** \n\n')
	subprocess.run(['xxd',location,'hexdump'])
	subprocess.run(['xxd','-p',location,'hexdump_plain'])
	extfile1=pwd+'/hexdump'
	extfile2=pwd+'/hexdump_plain'
	if(os.path.isfile(extfile1)):
		f.write('Hexdump stored in file: '+extfile1+'\n')
	if(os.path.isfile(extfile2)):
		f.write('Plain hexdump stored in file: '+extfile2+'\n\n')
	f.close()

def exiftool(location):
	#PNG, JPEG, TXT, BMP
	f=open('REPORT.md','a')
	f.write('**exiftool:** \n\n')
	data=subprocess.run(['exiftool',location],text=True,capture_output=True)
	data=data.stdout
	f.write(data+'\n')
	f.close()

def stegextract(location):
	#PNG, JPEG, GIF
	f=open('REPORT.md','a')
	f.write('**stegextract:** \n\n')
	data=subprocess.run(['stegextract',location],text=True,capture_output=True)
	data=data.stdout
	f.write(data+'\n')
	f.close()

def pngcheck(location):
	#PNG
	f=open('REPORT.md','a')
	f.write('**pngcheck:** \n\n')
	data=subprocess.run(['pngcheck',location],text=True,capture_output=True)
	data=data.stdout
	f.write(data+'\n')
	f.close()

def stegseek(location):
	#JPEG
	f=open('REPORT.md','a')
	f.write('***stegseek:*** \n\n')
	data=subprocess.run(['stegseek',location,'/usr/share/wordlists/rockyou.txt'],text=True,capture_output=True)
	data=data.stdout()
	f.write(data+'\n')
	f.close()
