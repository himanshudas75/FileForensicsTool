import modules

def pngfile(location):
	modules.pngcheck(location)
	modules.exiftool(location)
	modules.binwalk(location)
	modules.strings(location)
	modules.stegextract(location)
	modules.zsteg(location)
	