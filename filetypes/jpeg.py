import modules

def jpegfile(location):
	modules.exiftool(location)
	modules.binwalk(location)
	modules.xxd(location)
	modules.strings(location)
	modules.stegextract(location)
	modules.stegseek(location)