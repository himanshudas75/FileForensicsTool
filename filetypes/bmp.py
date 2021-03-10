import modules
import concurrent.futures

def bmpfile(location):
	begin='424d'
	end='49454e44ae426082'
	t=[]
	output=[]

	with concurrent.futures.ThreadPoolExecutor() as executor:
		t.append(executor.submit(modules.exiftool,location))
		t.append(executor.submit(modules.xxd,location))
		t.append(executor.submit(modules.strings,location,begin,end,'bitmap'))
		t.append(executor.submit(modules.stegseek,location))
	
	for thread in t:
		output.append(thread.result())

	f=open('REPORT.md','a')
	for i in output:
		f.write(i+'\n')
	f.close()

	