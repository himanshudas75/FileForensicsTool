import FileType
import argparse
import os.path

if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("inploc", help="Location of the file")
	args=parser.parse_args()

	if os.path.isfile(args.inploc):
		ftype=FileType.identify(args.inploc)
		if ftype == 'PNG':
			print("PNG")
		elif ftype == 'JPEG':
			print('JPEG')
	else:
		print("WARNING! File Does Not Exist!")