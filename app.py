import FileType
import argparse
import os.path
import CommonModules

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
			CommonModules.strings(location)
			png.zsteg(location)

		elif ftype == 'JPEG':
			import jpeg
			print('JPEG')
			CommonModules.strings(location)
	else:
		print("WARNING! File Does Not Exist!")