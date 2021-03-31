import modules
import concurrent.futures

def officefile(location):
	t=[]
	output=[]

	with concurrent.futures.ThreadPoolExecutor() as executor:
		t.append(executor.submit(modules.exiftool,location))
		t.append(executor.submit(modules.xxd,location))
		t.append(executor.submit(modules.unzip,location))
		t.append(executor.submit(modules.olevba,location))
		t.append(executor.submit(modules.mraptor,location))
		t.append(executor.submit(modules.pyxswf,location))
	
	for thread in t:
		output.append(thread.result())

	f=open('REPORT.md','a')
	for i in output:
		f.write(i+'\n')
	f.close()

	