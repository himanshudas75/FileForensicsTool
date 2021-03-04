import modules

def jpegfile(location):
	modules.exiftool(location)
	modules.binwalk(location)
	modules.xxd(location)
	modules.strings(location,'ffd8ff','ffd9')
	modules.stegextract(location)
	modules.stegseek(location)