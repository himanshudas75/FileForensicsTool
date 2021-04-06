import modules
import concurrent.futures

def pngfile(location):
	t=[]
	output=[]

	with concurrent.futures.ThreadPoolExecutor() as executor:
		t.append(executor.submit(modules.pngcheck,location))
		t.append(executor.submit(modules.exiftool,location))
		t.append(executor.submit(modules.binwalk,location))
		t.append(executor.submit(modules.xxd,location))
		t.append(executor.submit(modules.strings,location))
		t.append(executor.submit(modules.stegextract,location))
		t.append(executor.submit(modules.zsteg,location))

	for thread in t:
		output.append(thread.result())

	f=open('REPORT.md','a')
	for i in output:
		f.write(i+'\n')
	f.close()

	