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

def strings(location):
	#PNG, JPEG, BMP, PDF
	output='**strings:** \n\n'
	data=subprocess.run([f'strings {location} | grep "......*" > temp.txt'],shell=True,capture_output=True,text=True)
	if(data.returncode==0):
		out=data.stdout
		if(os.path.isfile('temp.txt')):
			f=open('temp.txt','r')
			lines=f.readlines()
			for l in lines:
				boolean=False
				l=l.strip()
				l+='\n'
				ans=re.findall('\w*',l)
				if(not ans==[]):
					for i in ans:
						if(not i==''):
							if(len(i)==1 and not (i=='a' or i=='A')):
								boolean=True
					if(boolean):
						continue
					c=l[len(ans[0])]
					if(c==' '):
						output+=l+'\n'
			f.close()
			subprocess.run(['rm','temp.txt'],capture_output=True)
		else:
			output+='Some error occurred\n'
	else:
		output+=data.stderr+'\n'
	return output
	'''data=subprocess.run(['xxd','-p',location],text=True,capture_output=True)
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
	return output'''

def binwalk(location):
	#PNG, JPEG
	output='**binwalk:** \n\n'
	data=subprocess.run(['binwalk','--extract',"--dd='*'",location],text=True,capture_output=True)
	out=data.stdout
	out=re.findall('.*',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n'
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
	#PNG, JPEG, TXT, BMP, EXT34
	output='**exiftool:** \n\n'
	data=subprocess.run([f'exiftool {location} | grep -v -E "Luminance|Viewing Cond Illuminant Type|Red Matrix Column|Green Matrix Column|Blue Matrix Column|Resolution Unit|Profile Connection Space|Profile Date Time|Profile File Signature|Red Tone Reproduction Curve|Green Tone Reproduction Curve|Blue Tone Reproduction Curve|Profile Version|Profile Class|Profile CMM Type|X Resolution|Y Resolution|Y Cb Cr Sub Sampling|Permissions|MIME|Subject|Title|Description|ExifTool Version Number"'],shell=True,text=True,capture_output=True)
	out=data.stdout
	out=re.findall('.*',out)
	for i in out:
		i=i.strip()
		output+=f'{i}<br \>'
	return output

def stegextract(location):
	#PNG, JPEG, GIF
	output='**stegextract:**\n\n'
	data=subprocess.run(['stegextract',location],text=True,capture_output=True)
	out=data.stdout
	out=re.findall('.*',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n'
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
		output+=f'Outguess output stored in {pwd}/outguess_extracted\n'
		return output
	output+=f'{data.stderr}\n'
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
	data=subprocess.run([f'olevba -c {location} | grep -v -E "olevba|===="'],shell=True,text=True,capture_output=True)
	if(data.returncode==0):
		output+=f'\n{data.stdout}\n'
		return output
	output+=f'\n{data.stderr}\n'
	return output

def sox(location):
	#WAV
	output='**sox:**\n'
	data=subprocess.run(['sox',location,'-n','spectrogram'],text=True,capture_output=True)
	if(data.returncode==0):
		output+=f'\nSpectrogram of the audio file has been stored in {pwd}/spectrogram.png\n'
		return output
	output=f'\n{data.stderr}\n'
	return output

def mraptor(location):
	#Office
	output='**mraptor:**\n'
	data=subprocess.run([f'mraptor {location} | grep -v -E "MacroRaptor|issues at|Flags: A=|Exit code"'],shell=True,text=True,capture_output=True)
	if(data.returncode==0):
		output+=f'\n{data.stdout}\n'
		return output
	output+=f'\n{data.stderr}\n'
	return output

def pyxswf(location):
	#Office
	output='**pyxswf:**\n'
	data=subprocess.run([f'pyxswf -o {location} | grep -v -E "pyxswf|report any issue"'],shell=True,text=True,capture_output=True)
	if(data.returncode==0):
		output+=f'\n{data.stdout}\n'
		return output
	output+=f'\nNot an OLE2 structured storage file'
	data=subprocess.run([f'pyxswf -f {location} | grep -v -E "pyxswf|report any issue"'],text=True,capture_output=True)
	if(data.returncode==0):
		output+=f'\n{data.stdout}\n'
		return output
	output+=f'\nNot an RTF file\n'
	return output

def extundelete(location):
	#EXT34
	output='**extundelete:**\n'
	data=subprocess.run(['extundelete',location,'--restore-all'],capture_output=True,text=True)
	if(data.returncode==0):
		output+=f'The recovered deleted files have been extracted to {pwd}/RECOVERED_FILES\n'
		return output
	output+='No files recovered\n'
	return output

def foremost(location):
	#EXT34
	output='**foremost:**\n'
	data=subprocess.run(['foremost','-t','all','-v','-i',location,'-o','./RECOVERED'],capture_output=True,text=True)
	if(data.returncode==0 and os.path.isdir(f'{pwd}/RECOVERED')):
		output+=f'The recovered files have been extracted to {pwd}/RECOVERED\n'
		return output
	output+='No files recovered\n'
	return output
