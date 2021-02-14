import subprocess
import FileType
import os.path

inploc=input("Enter file location: ")
outloc=input("Enter output report location: ")

if os.path.isfile(inploc) and os.path.isdir(outloc):
	print("Locations are CORRECT")
	outloc+='/REPORT.md'
	subprocess.run(['touch',outloc])
	FileType.filetype(inploc,outloc)
else:
	if not os.path.isfile(inploc):
		print("WARNING! Input Location is not a FILE")
	if not os.path.isdir(outloc):
		print("WARNING! Output Location is not a DIRECTORY")

