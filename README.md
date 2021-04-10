# FileForensicsTool
File Forensics Tool Project for CyberLabs Infosec division<br\>

**About**<br\>
This tool automates the forensics analysis of a file. Various linux tools are used in this tool for analysing the given file. After analysing the file it gives a detailed REPORT showing all the results from the tools used which can be further analysed manually, if required. This is a Command-Line-Interface (CLI) tool and needs a Linux environment and can be run using the terminal.

**Usage**<br\>
1. Make sure python and the linux tools used in this are installed in your system (their names are given below).
2. Download the tool.
3. Make sure to note down the location of the file you wish to be analysed (say, /home/file.jpeg)
4. Open the terminal and navigate to the directory of the tool.
5. Run: <br\>
	<!--Code Blocks-->
	'''bash
	python3 app.py <file_location>
	''' <br\>OR<br\>
	'''bash
	python app.py <file_location>
	'''<br\>
	depending on if you have python3 installed or not.
6. The tool will generate a REPORT file named REPORT.md in the same directory as the tool (if you are confused, the location of the REPORT.md file will be displayed on your terminal).

