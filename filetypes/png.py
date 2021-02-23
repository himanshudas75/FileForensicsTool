import modules

def pngfile(location):
	modules.binwalk(location)
	modules.exiftool(location)
	modules.strings(location)
	modules.stegextract(location)
	modules.zsteg(location)
	