import subprocess
def filetype(inploc,outloc):
	with open(outloc,'w') as f:
		subprocess.run(['file',inploc], stdout=f, text=True)


