import modules

def bmpfile(location):
	modules.exiftool(location)
	modules.strings(location)
	modules.xxd(location)