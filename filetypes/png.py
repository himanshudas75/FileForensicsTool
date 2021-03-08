import modules
import concurrent.futures

def pngfile(location):
	begin='89504e47'
	end='49454e44ae426082'
	t=[]
	output=[]

	with concurrent.futures.ThreadPoolExecutor() as executor:
		t.append(executor.submit(modules.pngcheck,location))
		t.append(executor.submit(modules.exiftool,location))
		t.append(executor.submit(modules.binwalk,location))
		t.append(executor.submit(modules.xxd,location))
		t.append(executor.submit(modules.strings,location,begin,end))
		t.append(executor.submit(modules.stegextract,location))
		t.append(executor.submit(modules.zsteg,location))

		for thread in t:
			output.append(thread.result())

	f=open('REPORT.md','a')
	for i in output:
		f.write(i+'\n')
	f.close()

	