import subprocess
import re

def strings(location):
	data=subprocess.run(['strings',location],text=True,capture_output=True)
	data=data.stdout
	text=re.findall(r'\w+',data)
	ctf=re.findall(r'\w+[ctf]{.+}|\w+[CTF]{.+}',data)
	print(text)
	print(ctf)