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
	output='**cat:**\n\n'
	data=subprocess.run(['cat',location],text=True,capture_output=True)
	out=data.stdout
	output+=f'\n{out}\n'
	return output

def strings(location,begin,end,ftype):
	#PNG, JPEG, BMP, PDF
	output='**strings:** \n\n'
	data=subprocess.run(['xxd','-p',location],text=True,capture_output=True)
	out=data.stdout
	if(ftype=='bitmap'):
		output+=f'\n{out}\n'
		return output
	out=out.replace('\n','')
	out=out.replace(end,'\n'+end)
	last=re.findall('.+',out)
	out=out.replace('\n','')
	out=out.replace(begin,begin+'\n')
	first=re.findall('.+',out)
	if(len(first)):
		first=first[0][:-len(begin)]
		output+=f'\n{bytearray.fromhex(first).decode()}\n'
	if(len(last)):
		last=last[-1][len(end):]
		output+=f'\n{bytearray.fromhex(last).decode()}\n'
	return output

def binwalk(location):
	#PNG, JPEG
	output='**binwalk:** \n\n'
	data=subprocess.run(['binwalk','--extract',"--dd='*'",location],text=True,capture_output=True)
	out=data.stdout
	output+=f'\n{out}'
	extdir=pwd+'/_'+filename(location)+'.extracted'
	if(os.path.isdir(extdir)):
		output+=f'\nEmbedded files extracted to: {extdir}/\n\n'
	return output

def zsteg(location):
	#PNG
	output='**zsteg:** \n\n'
	data = subprocess.run(['zsteg','-a',location],text=True,capture_output=True)
	out=data.stdout
	text = re.findall(r'text: ".*"',out)
	for i in range(len(text)):
		text[i]=text[i][7:-1]
		output+=f'{text[i]}\n'
	return output

def xxd(location):
	#PNG, JPEG, TXT, BMP
	output='**xxd:**\n\n'
	subprocess.run(['xxd',location,'hexdump'])
	extfile=pwd+'/hexdump'
	if(os.path.isfile(extfile)):
		output+=f'Hexdump stored in file: {extfile}\n'
	return output

def exiftool(location):
	#PNG, JPEG, TXT, BMP
	output='**exiftool:** \n\n'
	data=subprocess.run(['exiftool',location],text=True,capture_output=True)
	out=data.stdout
	output+=f'\n{out}\n'
	return output

def stegextract(location):
	#PNG, JPEG, GIF
	output='**stegextract:**\n\n'
	data=subprocess.run(['stegextract',location],text=True,capture_output=True)
	out=data.stdout
	output+=f'\n{out}\n'
	return output

def pngcheck(location):
	#PNG
	output='**pngcheck:**\n\n'
	data=subprocess.run(['pngcheck',location],text=True,capture_output=True)
	if(data.returncode==0):
		output+=f'\n{data.stdout}\n'
	output+=f'\n{data.stderr}\n'
	return output

def stegseek(location):
	#JPEG
	output='**stegseek:**\n\n'
	data=subprocess.run(['stegseek',location,'/usr/share/wordlists/rockyou.txt'],text=True,capture_output=True,input='y')
	outputpath=pwd+'/'+filename(location)+'.out'
	if(os.path.isfile(outputpath)):
		output+=f'Valid passphrase found\nFile extracted to: {outputpath}\n\n'
	else:
		output+='No valid passphrase found\n\n'
	return output

def outguess(location):
	#JPEG
	output='**outguess:**\n\n'
	data=subprocess.run(['outguess','-r',location,pwd+'/outguess_extracted'],capture_output=True,text=True)
	if(data.returncode==0):
		output+=f'\n{data.stdout}\n'
		return output
	output+=f'\n{data.stderr}\n'
	return output

def pdfid(location):
	#PDF
	output='**pdfid:**\n\n'
	data=subprocess.run(['pdfid',location],text=True,capture_output=True)
	out=data.stdout
	output+=f'\n{out}\n'
	return output

def pdf_parser(location):
	#PDF
	output='**pdf-parser:**\n\n'
	data=subprocess.run(['pdf-parser',location],text=True,capture_output=True)
	out=data.stdout
	output+=f'\n{out}\n'
	return output

def unzip(location):
	#Office files, ZIP
	output='**unzip:**\n\n'
	data=subprocess.run(['unzip','-o',location,'-d',pwd+'/ArchiveExtract'],capture_output=True,text=True)
	if(data.returncode==0):
		output+=f'\n{data.stdout}\n'
		return output
	output+=f'\n{data.stderr}\n'
	return output

def olevba(location):
	#Office
	output='**olevba:**\n\n'
	data=subproces.run(['olevba','-c',location],text=True,capture_output=True)
	if(data.returncode==0):
		output+=f'\n{data.stdout}\n'
		return output
	output+=f'\n{data.stderr}\n'
	return output