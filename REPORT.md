**FileName:** garden.jpg

**FileType:** JPEG

**exiftool:** 

File Name                       : garden.jpg

Directory                       : /home/v1per/work/files

File Size                       : 2.2 MiB

File Modification Date/Time     : 2020:10:27 00:09:31+05:30

File Access Date/Time           : 2021:04:10 20:19:16+05:30

File Inode Change Date/Time     : 2021:03:06 19:01:20+05:30

File Type                       : JPEG

File Type Extension             : jpg

JFIF Version                    : 1.01

Color Space Data                : RGB

Primary Platform                : Microsoft Corporation

CMM Flags                       : Not Embedded, Independent

Device Manufacturer             : Hewlett-Packard

Device Model                    : sRGB

Device Attributes               : Reflective, Glossy, Positive, Color

Rendering Intent                : Perceptual

Connection Space Illuminant     : 0.9642 1 0.82491

Profile Creator                 : Hewlett-Packard

Profile ID                      : 0

Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company

Media White Point               : 0.95045 1 1.08905

Media Black Point               : 0 0 0

Device Mfg Desc                 : IEC http://www.iec.ch

Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB

Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1

Viewing Cond Illuminant         : 19.6445 20.3718 16.8089

Viewing Cond Surround           : 3.92889 4.07439 3.36179

Measurement Observer            : CIE 1931

Measurement Backing             : 0 0 0

Measurement Geometry            : Unknown

Measurement Flare               : 0.999%

Measurement Illuminant          : D65

Technology                      : Cathode Ray Tube Display

Image Width                     : 2999

Image Height                    : 2249

Encoding Process                : Baseline DCT, Huffman coding

Bits Per Sample                 : 8

Color Components                : 3

Image Size                      : 2999x2249

Megapixels                      : 6.7



**binwalk:** 

| DECIMAL | HEXADECIMAL | DESCRIPTION |
| --- | --- | --- |
| 0 | 0x0 | JPEG image data, JFIF standard 1.01 |
| 382 | 0x17E | Copyright string: "Copyright (c) 1998 Hewlett-Packard Company" |


**xxd:**

Hexdump stored in file: /home/v1per/work/FileForensicsTool/hexdump

**strings:** 

mntrRGB XYZ

IEC sRGB

IEC http://www.iec.ch

IEC http://www.iec.ch

CRT curv

cFY5 aB

aSc ;

Sqi \

i1 L3

4o kh

A kr>wF

fG ,p3

vY +0Ul

yo hG

9U dz

qU p6

Mm Ica

98 W1

hw PT

V7O A

dg zf

A #pb

ac "FeP9$

A RILr>

ZFTq <qV

Twd ~

ZkulQIC #

bd B7

xR1 7r

703 *

syO op1

Ry zW

Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"


**stegextract:**

Detected image format: JPG

Extracted trailing file data:  ASCII text

Performing deep analysis

Done



**stegseek:**

No valid passphrase found


**outguess:**

Outguess output stored in /home/v1per/work/FileForensicsTool/outguess_extracted

