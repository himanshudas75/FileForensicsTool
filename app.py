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
		ftype=FileType.identify(location)
		outloc=subprocess.run(['readlink','-f','REPORT.md'],text=True,capture_output=True)
		outloc=outloc.stdout
		print('REPORT.md created at: '+outloc)

	else:
		print('WARNING! File Does Not Exist!')

finish=time.perf_counter()

print(f'\nFinished in {round(finish-start,2)} second(s)' )

#Without Threading, 5.68 seconds
#With Threading, 4.8 seconds