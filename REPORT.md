FileName: jpeg.jpg
FileType: JPEG

**exiftool:** 

File Name                       : jpeg.jpg<br \><br \>Directory                       : /home/v1per/work/files<br \><br \>File Size                       : 142 KiB<br \><br \>File Modification Date/Time     : 2021:03:04 13:06:18+05:30<br \><br \>File Access Date/Time           : 2021:04:10 11:55:14+05:30<br \><br \>File Inode Change Date/Time     : 2021:03:06 19:01:20+05:30<br \><br \>File Type                       : JPEG<br \><br \>File Type Extension             : jpg<br \><br \>JFIF Version                    : 1.01<br \><br \>Image Width                     : 1024<br \><br \>Image Height                    : 768<br \><br \>Encoding Process                : Progressive DCT, Huffman coding<br \><br \>Bits Per Sample                 : 8<br \><br \>Color Components                : 3<br \><br \>Image Size                      : 1024x768<br \><br \>Megapixels                      : 0.786<br \><br \><br \>
**binwalk:** 


DECIMAL       HEXADECIMAL     DESCRIPTION

--------------------------------------------------------------------------------

0             0x0             JPEG image data, JFIF standard 1.01




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


