import modules

def pdffile(location):
	modules.strings(location,'PDF','EOF')
	modules.pdfid(location)
	modules.pdf_parser(location)