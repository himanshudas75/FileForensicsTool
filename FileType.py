import subprocess
import re

def fnwrite(location):
	location+='/'
	filename=re.findall(r'[^/]+',location)[-1]	
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

	elif('bitmap' in text):
		import filetypes.bmp
		ftwrite('BMP')
		filetypes.bmp.bmpfile(location)

	elif('PDF' in text):
		import filetypes.pdf
		ftwrite('PDF')
		filetypes.pdf.pdffile(location)	

	elif('Microsoft' in text and not 'WAVE' in text):
		import filetypes.office
		ftwrite('Office File')
		filetypes.office.officefile(location)

	elif('Zip' in text):
		import filetypes.zip
		ftwrite('ZIP')
		filetypes.zip.zipfile(location)

	elif('WAVE' in text):
		import filetypes.wav
		ftwrite('WAV')
		filetypes.wav.wavfile(location)

	elif('ext4' in text or 'ext3' in text):
		import filetypes.ext34
		if('ext4' in text):
			ftwrite('EXT4')
		elif('ext3' in text):
			ftwrite('EXT3')
		filetypes.ext34.ext34file(location)
		
	else:
		f=open('REPORT.md','a')
		f.write('File type not recognised by the tool!')
		f.close()
