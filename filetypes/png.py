import modules

def pngfile(location):
	modules.pngcheck(location)
	modules.exiftool(location)
	modules.binwalk(location)
	modules.strings(location,'IHDR','IEND')
	modules.stegextract(location)
	modules.zsteg(location)
	