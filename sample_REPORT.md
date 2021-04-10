**FileName:** jpeg.jpg

**FileType:** JPEG

**exiftool:** 

File Name                       : jpeg.jpg

Directory                       : /home/v1per/work/files

File Size                       : 142 KiB

File Modification Date/Time     : 2021:03:04 13:06:18+05:30

File Access Date/Time           : 2021:04:10 11:55:14+05:30

File Inode Change Date/Time     : 2021:03:06 19:01:20+05:30

File Type                       : JPEG

File Type Extension             : jpg

JFIF Version                    : 1.01

Image Width                     : 1024

Image Height                    : 768

Encoding Process                : Progressive DCT, Huffman coding

Bits Per Sample                 : 8

Color Components                : 3

Image Size                      : 1024x768

Megapixels                      : 0.786


**binwalk:** 

| DECIMAL | HEXADECIMAL | DESCRIPTION |
| --- | --- | --- |
| 0 | 0x0 | JPEG image data, JFIF standard 1.01 |


**xxd:**

Hexdump stored in file: /home/v1per/work/FileForensicsTool/hexdump

**strings:** 

Mu 7F

ag kh


**stegextract:**

Detected image format: JPG

No trailing data found in file

Performing deep analysis

Done


**stegseek:**

No valid passphrase found


**outguess:**

Reading /home/v1per/work/files/jpeg.jpg....

Extracting usable bits:   0 bits

Steg retrieve: seed: 24127, len: 7383

Extracted datalen is too long: 7383 > 0


