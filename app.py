import FileType
import argparse
import os.path

if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("inploc", help="Location of the file")
	args=parser.parse_args()
	location=args.inploc

	if os.path.isfile(location):
		ftype=FileType.identify(location)
		
		if ftype == 'PNG':
			import png
			print("PNG")
			png.zsteg(location)

		elif ftype == 'JPEG':
			print('JPEG')
	else:
		print("WARNING! File Does Not Exist!")