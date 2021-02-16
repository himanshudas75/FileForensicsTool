import subprocess
import re

def zsteg(location):
	data = subprocess.run(['zsteg','-a',location],text=True,capture_output=True)
	data = re.findall(r'text: ".*"',data.stdout)
	for i in range(len(data)):
		data[i]=data[i][7:-1]
	print(data)

	