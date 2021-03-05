import modules

def pngfile(location):
	modules.pngcheck(location)
	modules.exiftool(location)
	modules.binwalk(location)
	modules.strings(location,'89504e47','49454e44ae426082')
	modules.stegextract(location)
	modules.zsteg(location)
	