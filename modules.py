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
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
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
		else:
			output+='Some error occurred\n'
	else:
		output+=data.stderr+'\n'
	return output

def binwalk(location):
	#PNG, JPEG
	output='**binwalk:** \n\n'
	data=subprocess.run(['binwalk','--extract',"--dd='*'",location],text=True,capture_output=True)
	out=data.stdout
	out=re.findall('.+',out)
	output+='| DECIMAL | HEXADECIMAL | DESCRIPTION |\n'
	output+='| --- | --- | --- |\n'
	for i in range(2,len(out)):
		k=0
		output+='| '
		for j in range(len(out[i])):
			if(out[i][j]==' ' and not out[i][j-1]==' ' and not k==2):
				output+=' | '
			if(not out[i][j]==' ' and out[i][j-1]==' ' and not k==2):
				k+=1
			if(not out[i][j]==' ' or k==2):
				output+=out[i][j]
			if(j==len(out[i])-1):
				output+=' |\n'				
	output+='\n'

	extdir=pwd+'/_'+filename(location)+'.extracted'
	if(os.path.isdir(extdir)):
		print(True)
		output+=f'\nEmbedded files extracted to: {extdir}/\n\n'
	return output

def zsteg(location):
	#PNG
	output='**zsteg:** \n\n'
	data = subprocess.run(['zsteg',location],text=True,capture_output=True)
	out=data.stdout
	text = re.findall(r'text: ".*"',out)
	for i in range(len(text)):
		text[i]=text[i][7:-1]
		output+=f'{text[i]}\n\n'
	return output

def xxd(location):
	#PNG, JPEG, TXT, BMP, PDF, Office
	output='**xxd:**\n\n'
	subprocess.run(['xxd',location,'hexdump'])
	extfile=pwd+'/hexdump'
	if(os.path.isfile(extfile)):
		output+=f'Hexdump stored in file: {extfile}\n'
	return output

def exiftool(location):
	#PNG, JPEG, TXT, BMP, EXT34, PDF, Office, WAV
	output='**exiftool:** \n\n'
	data=subprocess.run([f'exiftool {location} | grep -v -E "Luminance|Viewing Cond Illuminant Type|Red Matrix Column|Green Matrix Column|Blue Matrix Column|Resolution Unit|Profile Connection Space|Profile Date Time|Profile File Signature|Red Tone Reproduction Curve|Green Tone Reproduction Curve|Blue Tone Reproduction Curve|Profile Version|Profile Class|Profile CMM Type|X Resolution|Y Resolution|Y Cb Cr Sub Sampling|Permissions|MIME|Subject|Title|Description|ExifTool Version Number"'],shell=True,text=True,capture_output=True)
	out=data.stdout
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output

def stegextract(location):
	#PNG, JPEG, GIF
	output='**stegextract:**\n\n'
	data=subprocess.run(['stegextract',location],text=True,capture_output=True)
	out=data.stdout
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output

def pngcheck(location):
	#PNG
	output='**pngcheck:**\n\n'
	data=subprocess.run(['pngcheck',location],text=True,capture_output=True)
	if(data.returncode==0):
		out=data.stdout
	else:
		out=data.stderr
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output

def stegseek(location):
	#JPEG, BMP
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
	out=data.stderr
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output

def pdfid(location):
	#PDF
	output='**pdfid:**\n\n'
	data=subprocess.run(['pdfid',location],text=True,capture_output=True)
	out=data.stdout
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output

def pdf_parser(location):
	#PDF
	output='**pdf-parser:**\n\n'
	data=subprocess.run([f'pdf-parser {location} | grep -v -E "Should you encounter problems|This program has not been tested"'],shell=True,text=True,capture_output=True)
	out=data.stdout
	output+=f'\n{out}\n'
	return output

def unzip(location):
	#Office, ZIP
	output='**unzip:**\n\n'
	data=subprocess.run(['unzip','-o',location,'-d',pwd+'/ArchiveExtract'],capture_output=True,text=True)
	if(data.returncode==0):
		output+=f'Extracted to {pwd}/ArchiveExtract\n'
		return output
	out=data.stderr
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output

def olevba(location):
	#Office
	output='**olevba:**\n\n'
	data=subprocess.run([f'olevba -c {location} | grep -v -E "olevba|===="'],shell=True,text=True,capture_output=True)
	if(data.returncode==0):
		out=data.stdout
	else:
		out=data.stderr
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output

def sox(location):
	#WAV
	output='**sox:**\n'
	data=subprocess.run(['sox',location,'-n','spectrogram'],text=True,capture_output=True)
	if(data.returncode==0):
		output+=f'\nSpectrogram of the audio file has been stored in {pwd}/spectrogram.png\n'
		return output
	out=data.stderr
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output

def mraptor(location):
	#Office
	output='**mraptor:**\n'
	data=subprocess.run([f'mraptor {location} | grep -v -E "MacroRaptor|issues at|Flags: A=|Exit code"'],shell=True,text=True,capture_output=True)
	if(data.returncode==0):
		out=data.stdout
		out=re.findall('.+',out)
		output+='| Result | Flags | Type | File |\n'
		output+='| --- | --- | --- | --- |\n'
		for i in range(3,len(out)):
			output+=f'| {out[i].strip()} |\n'
		return output
	out=data.stderr
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output

def pyxswf(location):
	#Office
	output='**pyxswf:**\n'
	data=subprocess.run([f'pyxswf -o {location}'],shell=True,text=True,capture_output=True)
	if(data.returncode==0):
		out=data.stdout
		out=re.findall('.+',out)
		for i in out:
			i=i.strip()
			output+=f'{i}\n\n'
		return output
	output+=f'\nNot an OLE2 structured storage file\n'
	data=subprocess.run([f'pyxswf -f {location} | grep -v -E "pyxswf | report any issue"'],text=True,capture_output=True,shell=True)
	if(data.returncode==0):
		out=data.stdout
		out=re.findall('.+',out)
		for i in out:
			i=i.strip()
			output+=f'{i}\n\n'
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

def stegsnow(location):
	#TXT
	output='**stegsnow:**\n\n'
	data=subprocess.run(['stegsnow','-C',location],capture_output=True,text=True)
	if(data.returncode==0):
		out=data.stdout
	else:
		out=data.stderr
	out=re.findall('.+',out)
	for i in out:
		i=i.strip()
		output+=f'{i}\n\n'
	return output