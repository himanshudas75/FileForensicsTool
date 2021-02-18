import subprocess
import re

def fnwrite(location):
	filename=re.findall(r'[\w,\.]+',location)[-1]	
	f=open('REPORT.md','w')
	f.write('FileName: '+filename+'\n')
def ftwrite(filetype):
	
	f=open('REPORT.md','a')
	f.write('FileType: '+filetype+'\n\n')
	f.close()

def identify(location):
	fnwrite(location)
	data=subprocess.run(['file',location],capture_output=True,text=True)
	text=re.findall(r'\w+',data.stdout)

	if('PNG' in text):
		import filetypes.png
		ftwrite('PNG')
		filetypes.png.pngfile(location)

	elif('JPEG' in text):
		import filetypes.jpeg
		ftwrite('JPEG')
		filetypes.jpeg.jpegfile(location)

	elif('text' in text):
		import filetypes.txt
		ftwrite('TXT')
		filetypes.txt.txtfile(location)

	else:
		f=open('REPORT.md','a')
		f.write('File type not recognised by the tool!')
		f.close()
