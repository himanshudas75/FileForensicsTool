import subprocess

def identify(inploc):
	p1=subprocess.run(['file',inploc],capture_output=True,text=True)
	print(p1.stdout)