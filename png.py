import subprocess

def strings(inploc):
	data = subprocess.run(['strings',inploc],text=True,capture_output=True)
	