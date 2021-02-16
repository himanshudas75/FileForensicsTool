import subprocess
import re

def identify(location):
	data=subprocess.run(['file',location],capture_output=True,text=True)
	text=re.findall(r'\w+',data.stdout)
	print(text)

	if('PNG' in text):
		import filetypes.png
		print('PNG\n')
		filetypes.png.pngfile(location)

	elif('JPEG' in text):
		import filetypes.jpeg
		print('JPEG\n')
		filetypes.jpeg.jpegfile(location)

	elif('text' in text):
		import filetypes.txt
		print('TXT\n')
		filetypes.txt.txtfile(location)

	else:
		print("File type not recognised by the tool!")
