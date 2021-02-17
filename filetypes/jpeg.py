import modules

def jpegfile(location):
	modules.exiftool(location)
	modules.xxd(location)
	modules.strings(location)