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
	out=data.stdout
	f.write(out+'\n')
	f.close()

def strings(location,begin,end):
	#PNG, JPEG, BMP, PDF
	f=open('REPORT.md','a')
	f.write('**strings:** \n\n')
	data=subprocess.run(['xxd','-p',location],text=True,capture_output=True)
	out=data.stdout
	out=out.replace('\n','')
	out=out.replace(end,'\n'+end)
	last=re.findall('.+',out)
	out=out.replace('\n','')
	out=out.replace(begin,begin+'\n')
	first=re.findall('.+',out)
	if(len(first)):
		first=first[0][:-len(begin)]
		f.write(bytearray.fromhex(first).decode()+'\n')
	if(len(last)):
		last=last[-1][len(end):]
		f.write(bytearray.fromhex(last).decode()+'\n')
	f.close()

def binwalk(location):
	#PNG, JPEG
	f=open('REPORT.md','a')
	f.write('**binwalk:** \n')
	data=subprocess.run(['binwalk','-e',location],text=True,capture_output=True)
	out=data.stdout
	f.write(out)
	extdir=pwd+'/_'+filename(location)+'.extracted'
	if(os.path.isdir(extdir)):
		f.write('Embedded files extracted to: '+extdir+'/\n\n')
	f.close()

def zsteg(location):
	#PNG
	f=open('REPORT.md','a')
	f.write('**zsteg:** \n\n')
	data = subprocess.run(['zsteg','-a',location],text=True,capture_output=True)
	out=data.stdout
	text = re.findall(r'text: ".*"',out)
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
	out=data.stdout
	f.write(out+'\n')
	f.close()

def stegextract(location):
	#PNG, JPEG, GIF
	f=open('REPORT.md','a')
	f.write('**stegextract:** \n\n')
	data=subprocess.run(['stegextract',location],text=True,capture_output=True)
	out=data.stdout
	f.write(out+'\n')
	f.close()

def pngcheck(location):
	#PNG
	f=open('REPORT.md','a')
	f.write('**pngcheck:** \n\n')
	data=subprocess.run(['pngcheck',location],text=True,capture_output=True)
	out=data.stdout
	f.write(out+'\n')
	f.close()

def stegseek(location):
	#JPEG
	f=open('REPORT.md','a')
	f.write('**stegseek:** \n\n')
	data=subprocess.run(['stegseek',location,'/usr/share/wordlists/rockyou.txt'],text=True,capture_output=True,input='y')
	outputpath=pwd+'/'+filename(location)+'.out'
	if(os.path.isfile(outputpath)):
		f.write('Valid passphrase found\n')
		f.write('File extracted to: '+outputpath+'\n\n')
	else:
		f.write('No valid passphrase found\n\n')
	f.close()

def pdfid(location):
	#PDF
	f=open('REPORT.md','a')
	f.write('**pdfid:**\n\n')
	data=subprocess.run(['pdfid',location],text=True,capture_output=True)
	out=data.stdout
	f.write(out+'\n')
	f.close()

def pdf_parser(location):
	#PDF
	f=open('REPORT.md','a')
	f.write('**pdf-parser:**\n\n')
	data=subprocess.run(['pdf-parser',location],text=True,capture_output=True)
	out=data.stdout
	f.write(out+'\n')
	f.close()

def unzip(location):
	#Office files, ZIP
	f=open('REPORT.md','a')
	f.write('**uzip:**\n\n')
	data=subprocess.run(['unzip','-o',location,'-d','./OfficeExtract'],capture_output=True,text=True)
	out=data.stdout
	f.write(out+'\n')
	f.close()
