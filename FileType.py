import subprocess
import re

def identify(inploc):
	p1=subprocess.run(['file',inploc],capture_output=True,text=True)
	p2=re.findall(r' {1}\w+ {1}',p1.stdout)[0][1:-1]
	return p2
