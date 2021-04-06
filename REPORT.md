FileName: garden.jpg
FileType: JPEG

**exiftool:** 

File Name                       : garden.jpg

Directory                       : /home/v1per/work/files

File Size                       : 2.2 MiB

File Modification Date/Time     : 2020:10:27 00:09:31+05:30

File Access Date/Time           : 2021:04:06 20:26:29+05:30

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

Red Matrix Column               : 0.43607 0.22249 0.01392

Green Matrix Column             : 0.38515 0.71687 0.09708

Blue Matrix Column              : 0.14307 0.06061 0.7141

Device Mfg Desc                 : IEC http://www.iec.ch

Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB

Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1

Viewing Cond Illuminant         : 19.6445 20.3718 16.8089

Viewing Cond Surround           : 3.92889 4.07439 3.36179

Viewing Cond Illuminant Type    : D50

Luminance                       : 76.03647 80 87.12462

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



DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
382           0x17E           Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"


**xxd:**

Hexdump stored in file: /home/v1per/work/FileForensicsTool/hexdump

**strings:** 

mntrRGB XYZ
IEC sRGB
Copyright (c) 1998 Hewlett-Packard Company
sRGB IEC61966-2.1
sRGB IEC61966-2.1
IEC http://www.iec.ch
IEC http://www.iec.ch
CRT curv
A l
_x ?s<
rDk 8
h_ p+
cFY5 aB
RrH w
I 1=q\
q r3^<
C ,@
UW `c
o3 ~u
aSc ;
IT8 W
Sqi \
i1 L3
SwTr F
R 1	7
_ )>
I4m Q
h "a4C~
dA u#=r
O {We7V
w >rO
4o kh
y >j&
I8 /9
G _2?
Tg z}k
A kr>wF
7lU c
Wo s\
c pzb
o (T,
K1 e
Bw !G
fG ,p3
o :id
Cm 0#
vY +0Ul
5x K)t
v >X/
pu g>
yo hG
cx p>
n0Ys @q
9U dz
qU p6
Mm Ica
K  m;
98 W1
c +!$
K ;@Q
V I0\3g
hw PT
G du=k
_4Owuq 2
swo ~W,
C ?&w
t3_Ms S.
V7O A
m `Wy
Gf {W@
0A {W
u V<2.
m7OX X
m u30
dg zf
A #pb
Mzo t
a "?@1
ac "FeP9$
A RILr>
W nObk
GpO {U
G $7^
Ewa a(8%I
HbH )8
ZFTq <qV
Kia 2
Twd ~
0 dWO
V 	Tq
O nsm
_ ,j7?5
o @#$I.
ZkulQIC #
m m%d
bd B7
9 pEnh
l l	$
K ,F8
FY_ d
xR1 7r
703 *
Isq E
syO op1
_ k51
G m=3
W n9c
v yj:
B wnYx
km2 U
g <	;
B 8Nx
2n q
208 c
F >G^k
Ry zW
m o5Xex#
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

