import subprocess
import re

def strings(location):
	data = subprocess.run(['strings',location],text=True,capture_output=True)

def zsteg(location):
	data = subprocess.run(['zsteg',location],text=True,capture_output=True)
	data = re.findall(r'text: ".*"',data.stdout)
	for i in range(len(data)):
		data[i]=data[i][7:-1]

	