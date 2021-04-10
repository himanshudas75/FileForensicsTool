import modules
import os.path
import subprocess

pwd=subprocess.run(['pwd'],text=True,capture_output=True)	#finding present working directory
pwd=pwd.stdout[:-1]

def passcheck(location):
	import zipfile
	zf=zipfile.ZipFile(location)
	for zinfo in zf.infolist():
		encrypt=zinfo.flag_bits & 0x1
		if encrypt:
			return True

def zipfile(location):
	if(passcheck(location)):
		output='The Zip file is encrypted\n\n'
		data=subprocess.run(['zip2john {location} > hash'],shell=True,text=True,capture_output=True)
		if(data.returncode==0):
			if(os.path.isfile('hash')):
				output+=f'The hash of the zip file has been stored at {pwd}/hash\n'
	else:
		output=modules.unzip(location)

	f=open('REPORT.md','a')
	f.write(output+'\n')
	f.close()