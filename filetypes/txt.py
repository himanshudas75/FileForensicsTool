import modules

def txtfile(location):
	modules.exiftool(location)
	modules.cat(location)
	modules.xxd(location)