FileName: image.png
FileType: PNG

pngcheck: 

OK: /home/v1per/image.png (800x600, 32-bit RGB+alpha, non-interlaced, 88.1%).

exiftool: 

ExifTool Version Number         : 12.16
File Name                       : image.png
Directory                       : /home/v1per
File Size                       : 223 KiB
File Modification Date/Time     : 2020:09:27 00:41:27+05:30
File Access Date/Time           : 2021:02:26 19:35:18+05:30
File Inode Change Date/Time     : 2021:02:26 19:35:12+05:30
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 800
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 800x600
Megapixels                      : 0.480

binwalk: 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 800 x 600, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed

Embedded files extracted to: /home/v1per/work/FileForensicsTool/_image.png.extracted/

**strings:** 

First four lines:
IHDR
zBIDATx^
v=k\#
SF !

Last four lines:
\oU"!
tzi(D<
8p'"@
IEND

stegextract: 

Detected image format: PNG
No trailing data found in file
Performing deep analysis
Done

zsteg: 

''\n\n88\n\n,,
