import modules

def passcheck(location):
	import zipfile
	zf=zipfile.ZipFile(location)
	for zinfo in zf.infolist():
		encrypt=zinfo.flag_bits & 0x1
		if encrypt:
			return True

def zipfile(location):
	if(passcheck(location)):
		output='The Zip file is encrypted'
	else:
		output=modules.unzip(location)

	f=open('REPORT.md','a')
	f.write(output+'\n')
	f.close()