import FileType
import argparse
import os.path
import subprocess
import time

start=time.perf_counter()

if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("inploc", help="Location of the file")
	args=parser.parse_args()
	location=args.inploc

	if os.path.isfile(location):
		print('Analysing the given file...')
		ftype=FileType.identify(location)
		outloc=subprocess.run(['readlink','-f','REPORT.md'],text=True,capture_output=True)
		outloc=outloc.stdout
		print('\nREPORT.md created at: '+outloc)

	else:
		print('\nWARNING! File Does Not Exist!')
	subprocess.run(['rm','-rf','__pycache__','./filetypes/__pycache__','temp.txt'])

finish=time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)' )