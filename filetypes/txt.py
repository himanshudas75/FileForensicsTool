import modules
import concurrent.futures

def txtfile(location):
	t=[]
	output=[]

	with concurrent.futures.ThreadPoolExecutor() as executor:
		t.append(executor.submit(modules.exiftool,location))
		t.append(executor.submit(modules.cat,location))
		t.append(executor.submit(modules.xxd,location))
		t.append(executor.submit(modules.stegsnow,location))

	for thread in t:
		output.append(thread.result())

	f=open('REPORT.md','a')
	for i in output:
		f.write(i+'\n')
	f.close()

	