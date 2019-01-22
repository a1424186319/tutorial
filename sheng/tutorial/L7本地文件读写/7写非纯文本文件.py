#写图片信息到新图片

# 上一节课读出了一张图片的二进制信息。这节课假设从其它电脑或网络获得了一张图片的二进制信息，你需要把信息写入到一个空jpg文件中，这样图片软件打开这张已经写入的jpg文件，就能看到图片。
# 计算机原理：这些文件经过各自特定的编码存储在计算机上都是二进制。双击打开这个文件时，系统根据后缀选择相应的程序、程序依赖对应的解码方式解码二进制，最终呈现信息。。编码和解码不一致会导致无法打开或出错，所以谨慎修改文件后缀。

# 二进制写入硬盘

content = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xdb\x00C\x01\t\t\t\x0c\x0b\x0c\x18\r\r\x182!\x1c!22222222222222222222222222222222222222222222222222\xff\xc0\x00\x11\x08\x01,\x01M\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02w\x00\x01\x02\x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\xf0\x15br\xd1\n\x16$4\xe1%\xf1\x17\x18\x19\x1a&\'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xf7\xfa(\xa2\x80\n)3Fh\x01h\xa4\xcd\x19\xa0\x05\xa2\x934f\x80\x16\x8aL\xd2\xd0\x01E!4n\x14\x00\xb4Rn\x1e\xb4n\x14\x00\xb4QI\x9a\x00Z(\xcd!4\x00\xb4Rn\xa3<f\x80\x16\x8a@A\xa5\xa0\x02\x8a3HZ\x80\x16\x8aM\xc2\x80s@\x0bE\x14P\x01E&i\x0bb\x80\x1dE&x\xa34\x00\xb4Rf\x8c\xd0\x02\xd1E\x14\x00QE\x14\x00QE\x14\x00QE\x14\x00R\x1aZC@\x05\x14Q@\x05\x14Q@\x05\x14PN(\x00\xa4\xefF})\x8e\xfbGP?\x1a\x00~M5\x87s\\\xce\xb9\xe3}\x1fA`\xb7w8oD\x19\xfeU\xce7\xc6\x1f\x0e\xab\x90.d#\xfd\xc3@\x1e\x8f\xc0<\xd2\x8cW\x15\xa6\xfcM\xd15\x16\t\x14\xdf7\xfbC\x15\xd6\xdaj\x16\xf7\xb0\x89a\x95\\\x1fC@\x16\xc7JZ\x88L\x9c\xf5\x18\xf5\xe2\xabM\xaci\xf6\xecV[\xa8\x95\x87PXP\x05\xea\x8c\x86\xfe\xf6+\x9f\xbb\xf1\xd6\x83g\xfe\xb2\xf5\x0f\xfb\xbc\xd7\x1b\xaa\xfcg\xd2\xe0\xbc\x96\xda\xce9%*F\x0f\x96y\xe2\x80=@\x03\x9f\xbf\x9f\xc2\x8c\xc83\x80\x08\xaf\x12\x7f\x8b:\xe5\xc3\x11c\xa5\xbb\x8e\xc4\xab\x0f\xe9U\x9b\xe2\x0f\x8e\xa6r\xe9\xa7\x15\x07\xa0\xc9\xe3\xf4\xa0\x0fx\x1b\xf1\x9d\xbf\xad4\xbbz\xe2\xbc!\xbco\xf1\t\xb1\xb7O8\xfa\xd3[\xe2\x17\x8f-\x807\x1ag\xcb\xdc\xee\xcf\xf4\xa0\x0f{\x0eB\x8c\x9ehF,\t\xaf\x14\xb3\xf8\xc7{n\xb9\xd4leP:\x81\x19#\xf9Wu\xe1\xff\x00\x88\x9a.\xb7\x12$s\x98\xa6p\x0e\xc9\x17o\xf3\xa0\x0e\xbd\xa6\x08\xa4\xb7\x00u5\xcb\xeb\x1f\x10\xb4m#r\xcbr\xa5\xd7\xa8\xacO\x89~0]\x0bGh\xe2\x97\x12\xba\x9cb\xbe[\xd4\xb5[\x9dN\xe6I\xae\x1c\xb3\xb9\xc9\xe6\x80>\x93\xb8\xf8\xed\xa2@H\xc6y\xf44\xeb?\x8ez\x1d\xdc\x81\x0f\xcb\xcfpk\xe5\xc4`:\x8c\xd2\xb3\x83\xd1@\xa0\x0f\xb7\xf4\x9f\x12XkV\xfee\x9c\xea\xc4\x8e\x95\xaa\xae\x19Fz\xd7\xc6~\x15\xf1\x9e\xa1\xe1\xdb\x951\xcc\xde^G\x1e\x95\xf5?\x84<Oc\xe2]2;\x8bi\x8b6\xc0_+\x8e{\xd0\x07T\r-F\xbc\xf4\xa9(\x00\xa2\x8a(\x004\xb4\x94\xb4\x00QE\x14\x00QE\x14\x00QE\x14\x00R\x1aZC@\x05\x14Q@\x05\x14Q@\x05!\xa5\xa6>FM\x00\x05\x80>\xd5\xe6_\x13<wo\xa3\xdaIi\x1c\x80O\x8c\xf1\xd6\xbbo\x10\xeak\xa5\xe8\x93\xdd6x\x1cc\xd6\xbeA\xf1\x7f\x88\x1f[\xd6\xe7\x99\x8b\x10\x18\xa8\xcf\xa5\x00g\xea\xda\xd5\xee\xabr\xd2O3\x11\x9c\x8c\xd6ic\x9e\\\x9aFl\xd3h\x02\xd4w3Bs\x14\xac\xbfC^\x83\xe0/\x88\xf7Z\x0c\xe9\x15\xd4\xb2I\x10\'\x03\xady\xbcj\xce\xc1Td\x9e\x82\xbd[\xe1\xd7\xc3;\x9dk\xca\xbe\xbcD[V<\x03\xf7\x85\x00v\xba\x8f\x8b\xbcE\xe2\x99\x16=\x19$H[\x8c\x8c\x8a\x96\xdf\xe1f\xab\xaa\xaa\xddjW\xcf\xe6\xbf$n\xce+\xd44]\x0e\xd7C\xb4X-\x10\x05\x1d\xeb]F\x01\xa0\x0f.\x87\xe0\xc6\x94\x07\xef\xee\x0b7\xd3\xbdn\xe9\xff\x00\x0f|;\xa4\xc6\x81t\xf8\xe5t\xfe2\xbc\x9a\xec\x88\x1d\x974\xd5\x85\xb7\xee\xde@=\x85\x00Q\xb6\xb3\xd3\xe1M\x90\xdbG\x10\x03\x03\x0b\x8a\xb4\xb1*\xa8\x00!\x1f\x85N`C\xd5A\xa5XU\x06\x14\x00=(\x02,\xb0\x18\n\xb5]\xa0\x13\xbf\xef\xad\xa3+W\xbc\xb1M1\x92x8\x14\x01\x91u\xe1\xcd*\xe9v\xbd\x9c\x7f\x95p\xfe"\xf8Sis\'\xdbt\xb7\xf2.\xd3%1\xc7?Z\xf5\x01\x17\xa9\xa8d\xdd\x9d\xaa8\xe9\x9a\x00\xf9\x1f\xc7\x91\xf8\x96\x0b\xa4\xb4\xd6\xdaI\x16>\x15\xb3\x91\\+\x8c9\x15\xf6W\x8a|\x1do\xe2\x0b\x07\x8aE\r)\x07\xe65\xf2\xf7\x8c<\x13\xa8xcR\x9d%\x8f0\x86\xf9\x19rF(\x03\x94\xa2\x8eh\xe6\x80\x1e\xb5\xea\xdf\x06\xfcE%\x9e\xb2\xb6//\xee\xdd\xba\x13^Q\xda\xba/\x04\xdc}\x93\xc5\x16m\x92\x0bH\x07\x14\x01\xf6\xacl\x19\x14\x8fJ\x92\xaaX6\xeb8I\xcf(\x0f\xe9V\xb3@\x0bE\x14f\x80\nZni\xc3\xa5\x00\x14QE\x00\x14QE\x00\x14QE\x00\x14\x86\x96\x90\xd0\x01E\x14P\x01E\x14P\x01H\xc3*ii\x92\xc9\xe5\xaeq@\x1cO\xc4\xeb\x8f\xb2\xf8Bs\x9cn\x15\xf2\x15\xd3\x06\xba\x95\xbd\\\x9a\xfa\xc7\xe2\xd6\xe9<!"\xa8\xcb\x11_%\xcc\x08\x99\xc1\xeb\x93@\r\xe2\x90\x8eiB\x93RA\x0b\xcf2\xc4\x83,\xc7\x02\x80;_\x87^\x15\x97[\xd6"s\x191\x06\xe7\x8e+\xea\xdd3I\xb5\xd2\xed#\x86\xdd\x02\x80:W\x11\xf0\x9f\xc3\'H\xd1\x12i\xe2P\xec\x0f\xe7\x9a\xf4p\xa4\x1c\xd0\x03\x80\xc8\xa5\x0b\x8aZ(\x00#\x03\x8a\x05)\xe9Q\x91\xcd\x00I\x9aB\xc0u4\xce@\xebQ\x92p\xc4\x9e\x05\x00O\x9ahbMa\xbe\xae\x8bt#\xdf\x92N0+e\te\r\xd8\xd0\x04\xa4\x81\xde\x98\xd8\x06\x83\xce*)\xa5H\xfa\xb8\xfc\xe8\x02A\x8a\xe5\xbcm\xe1K\x7f\x11i3G\xe5\x8f4\xa9\xc1\xef\x9a\xdfK\xe8Y\xc2\xabg\'\xb5Zb\xb89\xa0\x0f\x89<O\xa0\xcd\xa0\xebSYJ\xb8\xc1\xe0\xfe5\x88Wk\x91\xe9_K|b\xf0\x85\xbd\xde\x9b.\xab\x0cy\x9c\x0c\xf0>\xa6\xbekx\xca9\x0c0A\xe4P\x03{V\xd7\x85\xa4\x8a?\x10\xd9\xc93\xedD\x90s\x9a\xc5\xc1\xe9]\xf7\xc3\xff\x00\x047\x88\xe6\xdf)\xf2\xe3S\xdf\x8a\x00\xfagM\xf1>\x8d%\x9c\n\xb7\xf0\xee\x088.+C\xfbv\xc0\x9c-\xe5\xb9\xff\x00\x81\x8a\xf2\xb1\xf0\xb9c*a\xbfu\x03\xfe\x9aVd\xbf\r\xb5\x98\x98\x9b}V^\t\xc7\xefj\x94nc)\xd8\xf6\xd5\xd4!q\x95\x9e"=\x9a\x8f\xed+S\xff\x00/\x11\xfe\r^\x16|-\xe3[c\x88\xb5\x1d\xca}e?\xe1N\xff\x00\x84K\xc6\x88\xbb\x97R\x8c\x91\xce<\xd3\xfe\x15J\x04\xfbC\xddV\xee\'\xfb\x92!\xfcjx\xdbp\xe4\x8f\xc2\xbe}\x92\xcf\xc7\xb6@\x95\xba\x0e\x07\xf7X\x92\x7fJ\xf4_\x86Z\x9e\xbb\xa8G\xa8\x8dn6F\x8c\xc6"\xdc\x08\xc8\xf9\xb3\xd7\xe8*e\x1b\x15\t\xdd\xd8\xf4,\xd1\x9aJ*M\x85\xcd\x19\xa4\xa2\x80\x174f\x92\x8a\x00ZCKHh\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa4l\x1e\xa2\x96\x90\xd0\x075\xe3\r;\xfbK\xc3\xf7\x11m\x04\x858\xe35\xf1\xde\xb7a-\x86\xafs\x0c\xa8\xcb\x89\x0e21_rO\x12\xc9\x0b!\x19\x04`\xd7\xcf\xff\x00\x16\xfc\x12c\x9aMJ\x14\x1bv\xf2\x15y\xcd\x00x`5\xdb\xfc6\xf0\xf3\xeb>!\x85\x8af%a\xce+\x8a\xf2\x88<\xf5\xce\x08\xaf\xa5>\t\xe8\x0bg\xe1\xd5\xbd\x9a0]\xdc\x8eW\xa5\x00z\xbd\x95\xbaZ\xda\xc7\x0c`\x05P:U\xa1\xe9L\x8c\x12*J\x00RqP\xcb0L`\xe4\x9a\x91\xbaV6\xb2n#\xb5f\xb5\x8d\x9eLq\xb4P\x05\x89\xf5{kv\xc4\xf2"\x1fv\xc5F5\xab6@\xcbs\t\xf6\xde+\xc95\x9d\x0f\xc4\x9a\x98\x92[\x8b\x9f\xb3\x8e\xcb\x96\x06\xb8}OM\xf1\x0e\x9fk\xe6%\xf4\xc4\xf3\x9f\x9c\xd0\x07\xd1\x17>*\xd3\xa0\x07}\xc4y\x1e\x8e+\x9a\x1f\x12,e\xbd{5pI\xc8\x1f0\xe6\xben\x97R\xd6e\xe1\xa6\x99\x9b\xa1\xc9&\xa7\xd1\xe1\xd4\x8e\xac\xb2\xeec&\xe0H\xe6\x813\xdbu\x8dm\xb4\x9dN\x19\xd9\x18\xc6\xc3v\x7f\x1a\x8a_\x8aO\xe6m\x8f\x80;\x13In\x17\xc4w6\xb6wV\xec\x02.\t#\xads\xff\x00\x12|\'g\xa0\xba\xb5\xab\xb0.7c\x02\x80E\xfb\x8f\x8cw0\xee\n\xb9#\xb8\xff\x00\xf5\xd6}\x8f\xc5+\xad^\xf9\xa2c\xb7\'\x19\'\x8f\xe7^k\x7f\xa4]\xc9o\x1d\xc4/\xb9[\xf8Fs]\xcf\x82\xfe\x1f\xbe\xa7h\xd33y\x0cW\'wSI\x0c\xf5\xcf\r\xc9\x0c\xb1\xf9\xf3\xea\x08Oa\xe6\n\xec\xa0\xbc\x86\xe5\x0f\x96\xc1\xb1_4j\x1a\x9b\xf8K[K_\xb4O1f\x03\x1b\xb8\xeb^\xdb\xe0\xeb\xe3}\xa7\xc7pQ\x93p\xce\r\x00t:\xae\x9d\x16\xab`\xd6\xb2\x80\xca\xdd\x88\xcd|\x95\xe3\xef\r\xbf\x87\xfcAp\x8c0\x8f!*\x00\xe3\xad}\x85\x11\x1d\xcdy\x0f\xc6\x8f\x0b\x9b\xdb1\xa8A\x1e\xe2\x83\x90\x06y\xe6\x99(\xf0\x9d\x07@\x97W\xd4R\x15?)#\x9a\xfa;@\xb3\xd3|9e\x1ch\xf0\t\n\x8c\xfc\xc39\xc5x\xd7\x82t\rf\xf0\xb5\xce\x9e\xc8\x9eY\xc1\x0e\x0ex4kZo\x88m\xfcQ\x06\x9d6\xa1\'\x9b9\x04mv\xda3M\nG\xbf\xc5}\x04\xa4\xfe\xfa<c\xfb\xc2\x9c$\xc9\xf9dR;s^z>\x1ax\xa9-\x96E\xd5\xd3\xee\x83\xcb\xb5V\xba\xd1\xfcm\xa3\xda\xbd\xd4\xb7\x90<q.p\x0bd\xd6\xb0\xb1\xcf(\xb6z\x92\x89v\xe4.EG\x96S\x9d\xa4\xd7\x8fX\xf8\xf3\xc4\xafm$\xbff\x92E\x88\x90v\xee?\xd6\xb4\xb4\xff\x00\x8a\xe8\xe7\x176\xd2\xa7l\x9a\xb5b9dz\x87\x99\x91\x86\x8c~"\xb6\xf4r\x87\xcd\xd8\x81G\x1d?\x1a\xe24\xcf\x15iZ\xaa)K\xb8\x90\x9e\xcc\xe0Wm\xa2\xc6\x166p\xe1\x83\xe0\xf1\xf8\xd4\xd4\xb7)t\xd3\xe6W5\xe9(\xa5\xaes\xacJ(\xa2\x98\x05\x14Q@\x0bHii\r\x00\x14QE\x00\x14QE\x00\x14QE\x00!\x1cVf\xaf\xa4[\xeb\x16\x0fo:\x02\x08\xadJ\x87y\xf3Yq\xc0\x19\xa0\x0f\x99>&|>\x87\xc3\xd7\x96\xefg\xb7\xf7\xacN\x05{\x8f\xc3\xcb\'\xb5\xf0\x9d\xb4r!V\xeb\xc8\xc5p?\x16\x19\xef\xbc]\xa4i\x91\x90\x1aB9=:W\xb0i\x91\xf9:u\xbcX\x03d`\x1ct\xce(\x02\xe8\\\n\\P)h\x01\x08\xe2\xb3\xb5)\xa7\x82\xceF\x81r\xc0qZG\x9a\x86D\xc8"\x80<\x1b\\\xd4\xf5\xb9\xefXM;\xa0\x07\x85\xc9\x15\xc7x\xba\xfbU\x82\xd1@\x96BH\xe83_G\xde\xf8n\xc2\xf1\x8c\x92B\xbb\xfd\x80\xac\xab\xbf\x01\xe9\x97\xd1\xb7\x9d\x1a\xb3}(\x03\xe6-/K\xd4\xef\xe0\x12F\xb2\xb1\xeaz\xd7\xa8\xf8\x1f\xc1\xb7\x02\xe0]]\xc4\xdf0\xee\xbd+\xd3\xf4\xaf\x04\xd8\xe9\x8aV(\x93o\xa6+\xa2\xb6\xb5\xb7\x85v\xa4j\x07\xb5\x00eYh\xd6\xd0]$\xd1\xa8\xdc\xbe\xd5\x17\x89|+o\xe28\xc0\x99~`0\t\xae\x8f\xca@\xd9\x00\x0f\xa5\x0cM\x02<SY\xf0\x1c\x9a"~\xe4\x19\x00`B\xf5\xabZe\xc5\xc5\xacQG\x86\x88\x91\xc8\xc6+\xd7$\x8e9\x88\xf3Q_\x1e\xa35J}\x13N\x9eM\xcd\x1a\xa9_\xee\x81@\xce"?\x02h\xba\xe5\xda\\\xdd\xa13\x0eA\xc8\xae\xee\xcfJ\xb7\xd3\xed\x12\xde\xdd@D\x18\x154V\x90@\x9f\xbaA\xc7B\x075e\x1f \x1d\xb8=\xe8\x021\x19\x00\x0fJ\xa5\xaaX\xc7\xa8Y\xcdc*\x82$S\xd7\xd6\xb4\xf6\xe7\x9a\x81\xe1!\xb7\x9e[=h\x11\xe0\xbe\x1a\xb9\x9f\xc3^5\xb9\xd2\x1cm\x8aW\xcag\x8e\xaci\xfa\xd9\xfbO\xc4\xfb\x0ca\x88+\xd3\xf1\xad\x0f\x8b\x9ai\xb0\xd5mu\xaba\xb0\xa0\x05\x88\xeaq\\\xd7\x87/[Y\xf1\xe6\x9b1\xc8\xda\xa8N\xe3\xd6\x81=O\xa3\xa3Pm\x90\x11\xfc#\xf9W=\xe3%\xdb\xe1\x8b\xb3\x1a\x8e\x135\xd1\xa1>Z\x8fj\xe7<i(\x83\xc2W\xaeF~J\xab\x88\xf3\x0f\x05\x10\xfe\x1a\xbey-\xd5\xb1\xbf\x92=\xea/\x86\xde\x13\xd3|Amr\xfa\x8c`\xe1\xdb\x18\x1f\xed\x1a_\x08\xdc4^\x04\xd4f=\x83\x1e?\xde5\xd2\xfc\x14\x84K\xe1\xe9n\x08\x1f;\x1c\x7f\xdfF\x9f0\xacW\xd6~\x12@W\xcc\xd2\'\x9229\xc0l\x7fJ\xd9\xf8].\xab\xe6k6\xba\xa3\x176\xf2D\xb1\x93\x9e\x98o\xf0\x15\xdf\xaa\xa8\xca\x80\x06\x06x\xaeo\xc31\x98\xbcK\xe24\xe0\x01$8\xc7\xfb\xadI\xca\xe8i\x1de-%-A@i)M%1\x85\x14Q@\x0bHii\r\x00\x14QE\x00\x14QE\x00\x14QHX\x03@\x0bU\xf1\x8b\x87\xf7Z\xb0\x0ej\xad\xd4\xa2\x14\x92R8Q\x9a\x00\xf1\x1do~\xad\xf1r\xcf\x19"\xdd\x86}\xba\x8a\xf78?\xd4\xaf\xb0\xc5x\xa7\x82bmg\xe2\x16\xa5\xa8\x05\xca\xc4\xe4m\xef\xf7\x8d{TJ\xca\xbc\xfa\xd0\x04\xd4f\x8e\xd4P\x02\xd2\x11E\x06\x80\x18\xc0\x11\xd2\x98\xab\xc1\xa9i8\x19\xa0\x08\xc2\xf5\xa6*l\xefK\xcf5\x8b\xadx\x92\xd3E\x8c4\xf2.M\x02f\xcbM\xb7\xf8I\xaa\xed0\x95\xc0!\x96\xb8=K\xe2\xa5\xad\x9d\xb9\x928\xc3\x0fc[\xfe\x1b\xf1<~ \xd1\xc5\xe2\xa0\x0cA P\x07C\xca\xab\x1e\xd8\xaa_l[XY\xa6t\x04\x9f\x97#\xb5q\xf3x\x93[\x1a\xc0\xb7\x11\xaa\xdb\xee\xeb\xb7\xb5t\xf7\xdag\xf6\x8d\x80\x1f2\xb9\\\x82;P2\xf4s\x0b\x98VB\xc0g\x91\x8a\xb6\x18g\xe5\xcf\xe3^_oq\xaa\xe8\x9a\x92\xa4\xac\xf2\xc5\x9c\x0eN+\xd1\xec\xae\r\xcd\xbaI\xb7\x04\x8a\x00\xd0Pq\xc9\xa8\xdf&m\xb9\xc7\x19\xa7+\x0c`\x1c\xd3\n\x13)|\xf6\xc5\x00p\xbf\x154\xcf\xb7xRvQ\x93\x1a\x92k\xc4\xfe\x19\xb3^x\xd2\x11\xbbo\x94B\x9f\xc3\x8a\xfaK[\xb0k\xbd\n\xee\xd9\x98\x16\x91H\x04\xf6\xaf\x93\xb4\xbdU\xbc)\xe39d#r\xc71\xdd\xb7\x8e\x86\x81X\xfb\x19F\xd5Q\xec+\x8f\xf8\x977\x95\xe1\x0b\x95\xce\tSO\xf0w\x8d\xec|Ib\x19Ycu\xfe\x12y5\x97\xf1j\xe0E\xe1i\x1c\x8e\x1b"\x93\x0b\x1cV\x87\x8bo\x85\xd7\xf2\x91\x9c\x86\xfeu\xd9|\x19\x88G\xe0\xe4l\xfd\xe6o\xfd\x08\xd7#n\xbe_\xc2\t\xcf\xfc\xf4V\xc7\xb75\xda|$B\x9e\x0f\x81s\xea\x7fSB\x0b\x1d\xf2s+\xfd\x05`\xe8%O\x8a<E\xb7\x9f\x9e\x0c\xff\x00\xdf&\xb7\x93\x87s\xfe\xcdr\xbe\x12\x90\xc9\xe2\xbf\x13\xe4\x93\x89 \xff\x00\xd0Z\x98\xce\xca\x8a(\xa0\x00\xd2R\x9aJ\x00(\xa2\x8a\x00ZCKHh\x00\xa2\x8a(\x00\xa2\x8a(\x00\xa4n\x06ik7Y\xd5a\xd2m\x1a{\x83\xb65\x19,{P\x01\xa9j\xb0i6mur\xe1Q}k\x9e>3\xd2\xf5}:\xe5-\xa6]\xf8#\x83\\\x9f\x8a\xbcQ\xa6\xf8\xcf@\xb9\xb1\xd3ocI\x939\xcey\xaf\x17\xd2\xe7\xbc\xd0\xee\'I\'.\xc1\x8a\x98\xc19\xeb\xd7\x9a\x00\xf6/\x83Q\xe3X\xd6\xdf;\xb3!9\xff\x00\x81\x1a\xf65\xce1^+\xf0*_0\xea\xb7\x0eH\xdc\xdd\x0f\xfb\xc6\xbd\xa62J\xe4\x9c\xd0\x03\xe8\xa2\x8a\x00))M%\x00\x14\x1a)\xad\xd2\x80\x10\xaf\xca}k\x9c\xd7</o\xad\x84\x13\xbe6\x9fZ\xe8\x99\xc2\x81\x91\x9a\xe4\xfcG\xe2\xd8\xf4\x88\t\xd9\x87\xce\x06h\x03\'W\xf0%\xb1\xd3\xfe\xc9\x12\xa9\xcf\x01\x88\xff\x00\xebS\xfc1\xe1\x9b\xdd\x1a\xdf\xc8^\x11zdW\x19\xac\xfcE\xb8\xf3\xd1\xf9#\xb61X\xd7?\x13o\xd8mIB\x0fq@\x1e\xf5\x16\x9d\x1e\x15\xde52\x0e\xf8\x15h\xbe\xcf\x95P\x93\x8a\xf0\x18\xbe\'\xce\x96L^\xe5|\xd5\x1e\x95\x99a\xf1\xbbQ\xb7\xba>r\x19#<\x0c\x01@\x1fC\xcbl%!\x9a\xdds\x9e\xe0U\x8bx\xccj\xc3\x00\x01\xc7\x15\xc8xW\xc6\xf6\xde&\xb4VH$/\xe9\x9a\xec\xa0P\xab\x9c\x10Obh\x02P}\xb1N\xa4\x00\x1e\xf4\xacB\xc6O\xa5\x00Av\x9b\xed\\{\x1a\xf8\xd3\xc6P,>,\xbcQ\xdd\xdb?\x99\xaf\xb1u+\xc8\xedl$\x9aBv\xed=>\x95\xf1\xaf\x88n\x06\xab\xe2\xa9\xcclr\xd32\x8f\xce\x80-xg^\xbd\xf0\xf5\xc8\xb8C\'\x95\x9e\x80\xd7\xa8x\xcf\xc7\xf6^!\xf0\xc4\x16\xfd\x1c\x81\xd7\xf0\xae\xb3\xc1?\r\xf4\xf8t\x18N\xa2\x16v\x91r1\x91\x8e\xfd\xe9|Q\xf0\xaa\xcfU\xd3\x88\xd3Ym\xdd\x18\x90\x1f\'4\x01\x81\xa9\xc3\xe5|#C\x0b}\xe4\'\xf9Wk\xf0\xaa#\x1f\x84m\xf2:\x83\xfc\xeb\xca\xfcW{\x7f\xa2x[\xfb\nx\\\x04\x05|\xef\xe1\xfc\xab\xd5>\x19\\\x84\xf0\xb4\x08~\xea\xa6Kv\xeb@\x1d\xb182\x9fE\xae\x17\xe1\xf4\xff\x00h\xf1_\x8b\x9b9\xc4\xd6\xe3\xff\x00\x1dj\xed\x1ep\xf1K$C\xcc\x1bH\xc0\xaf>\xf8T\xfef\xbf\xe2\xd91\x8d\xf3\xc0q\xe9\xf2\xb8\xa0\x0fP\xa2\x8a(\x004\x94\xa6\x92\x80\n(\xa2\x80\x16\x90\xd2\xd2\x1a\x00(\xa2\x8a\x00(\xa2\x9a\\\x02\x07z\x00uy\xb7\xc5\xcd+R\xbf\xd0\x1d\xec\x1c\x90\x17\xe6A\xe9^\x89$\xe9\x167\x9cf\xa1\x91!\xbaL\xe0:\xb0\xdaA\xe6\x80>f\xd1<=\x0bi\x9e}\x9d\xc1\x8e\xfe,\xf9\x91n=GZ\xcf\xd4\xae\xa2\xb8\xbf\x8e\xe2x|\x9b\x88[\xcb\x99O\xf1(\xef^\xa9\xe2\xaf\x02\xcfa\xa9I\xaai-\xb7?3\xa6:\xd7\x9bj\x8d\x0f\x88\xdd\xe1 Yj11V\x8f9\xf3@\xff\x00\xeb\xd0\x06\x8f\x85|F\x9e\x1c\xbf\x93Q\x80\xe3Kc\x87\x19\xee:\xff\x00:\xfa\x0bN\xd5\x13Q\xb1\x8a\xe6&]\x92("\xbeO\xd3\xee\xc6\x95x\xdaN\xa3\x11\x16r\x9f\x98\x1e\xc7\xb9\xcdo>\xb1\xe2-6\xf6\xde\xce\xc6\xf8\xbd\xb3\x91\xb0\x91\xf7F8\xef@\x1fRF\xd9^M=Nk\xc4\xfc%\xe3}_\xfe\x12\x98\xb4[\x95\x13\x06\x00\x99r\x0623\xd2\xbd\x92\xdeY\x1ca\xe2+\xef\x9a\x00\xb2i(\xceh\xe2\x80\nk\xe7o\x14\xee\xd4\x1e\x94\x01\x99\xaaO\xe4Y\xb3\x06\xf9\xeb\xe7\xbf\x1aA\xae\xebW\x0e\x91\x92\x11O\x06\xbe\x88\xbc\xb2[\x82\t\x1d+\x9a\xbd\xf0\xb8`\xed\x1au\xf6\xa0\x0f\x9d\xad<\x05\xae\xea\xd7Io\xe7\x11\xd7\x9f\xf2k\xaa\xb5\xf8\x11\xab9Cqv\x02\x9e\xbf\xe75\xe8\xf1h\x1a\xad\xad\xc3Il\x98o]\xb5\x16\xa6\xfe\'\x865\x01\x19\x88\xeb\x8e3@\x1c\xcd\x97\xc0tI\x87\xda/\x01_L\x9f\xf1\xae\x8a\x0f\x82\x9a\x08\x8c\xa3\x8c\x95\xe8Fk6\xd6\xeb\xc5Mx\xa1\xe0r\xb9\xe9\x9c\xd7\xa4\xe8\x93\xdf\xbcAn\xe2\n\xdf\xad\x003@\xf0\xae\x9f\xe1\xdbq\x15\x9cx\xc0\xc6O5\xb9\xda\x9c8\x14m\xe34\x00\x8b\xc5,\xa0\x98\x98\x0e\xb4\xdd\xca\xbcf\xa2\xb9\xb8\x16\xd6\xef;}\xd5\x19\xc5\x00y\xef\xc5o\x11\xc7\xa5xm\xa0\x8d\xf1+)\xe8k\xe7o\x08Z\xff\x00j\xf8\xaa\x00\xcb\x9d\xd2\x06#\xf1\xae\x8f\xe2\xbf\x88\xce\xb3\xae\x98\xe0s\xb5>R\x99\xf75\x1f\xc1\xfb\x13u\xe2\xf8\x89^\x10\x83\xfa\xd0\x07\xd5:|\x02\x1b\x08\x11F\x02\xa0\xfeUd\x8c\x0e\x05:!\x88\xd4z\x0cS\x88\xa0\x0e{\xc4>\x18\xb0\xf1\x05\xa9\x8a\xe6\x15\xcf<\xe3\x15\xe7rA\xac\xfc=\x99LHg\xd3I\xe4\x0cp?\xc9\xafc+\xc5Q\xba\xd3\xa2\xbc\x85\xa1\x9c+\xc4\xdf\xc2\xc34\x01\x8f\xa4k\xd0x\x83N2\xda\x11\x17\xcaw)\xed\\\xa7\xc2#\xbbW\xf1gr\'\x80~\x8fX>"\xb3\xd4<\x13\xabIyi\xba{&\x04\xf9\x0b\xc7\xeb\xf8\xd5\xff\x00\x81\x17\xbf\xda\x12x\x9a\xe7n7\xcd\x01\xc7\xa7\x0f\xc5\x00{%\x14Q@\x01\xa4\xa54\x94\x00QE\x14\x00\xb4\x86\x96\x90\xd0\x01E\x14\xd2\xe0}h\x01\xd5\x1c\x8b\x9f\x9b\x19#\xa5Cu\xa8[\xd9\xc7\xbey\x02\x01\xeb\\g\x88~)h\x9aR\x18\xa0\x98\xdc\\\x91\xc4j:\xfe4\x01\xd6\xdd\x98\x9a0\xf3J\xaa\xab\xeak\x16\xf3\xc6\x1a\x06\x8c\x85..\xd5\x18\x0c\x85\xeb\x9f\xca\xbc\xb5\xe7\xf1\x87\x8e\xae\t\xb6V\xb0\x83\xdf\x07"\xba\r3\xe1\x0b\xdcD\xb2kW\x9et\xa0\xfa\x11\xc5\x00A\xe2\x1f\x8cv\x11Y\xca\xb6\x91\x99\x14\x8c\x02G\xff\x00Z\xbc\xf3G\xf0\xce\xb7\xe2\xa9$\xf1-\x94L\x92\t\t\x0b\x8e\xa35\xdf|N\xf0\x96\x89\xa1xA^\xd6\xd4,\xaaq\xbb=x\xae\xbb\xe1\xad\x80\xb7\xf0m\x8b\xc6\xc1|\xcf\x9c\xe0u\x04t\xa0\x0f\x1d\xbc\xf8k\xe2=j\xe85\xcc,\x92\xbf\x00\xe0\x0cT\xf3|+\xf1\\\xac\xb2\x96e1|\xaa1\xe9_F\xbd\xbe\xf1\x91\x80\xe3\xa1#\xa56\xe1\xcc\x103\xe3%F~\xb4\x01\xf3\xc5\xa7\xc3_\x19i\xd7_\xda\xb0\x963\xa8\xf5\x19\xf4\xad\x88\xbcy\xe2\x7f\r_\xa2kp\x9f#8\xdcqZ\xda\xd7\x8e\xfcSm\xab\xb2Y\xe92\xc9\x07\x18\x1b\x80\x07\x8a\xf3\xef\x18\xea:\xee\xb7\xa8C6\xa7j- -\xfe\xac\xb0=\xa8\x03\xe9-\x0fU\x8fW\xd3"\xbc\x8c\x8d\xae*\xebd\x9a\xc0\xf0rB\x9e\x16\xb4H\x1dH\x0b\xce+\xa0Q\x95\xa0\x05Zv(\xc5\x02\x80\x02\xa0\x8a\x88\xa6EMI\xc6(\x02\xb9\x84\x8eCR\x88\xc1\xfb\xca\x0f\xd4T\xc7\x8aN\x7f\xbah\x02\x11o\x18}\xc1\x14\x1f\xa5M\xb4\x0e\x82\x82[\xfb\xb4\x9b\xbdG4\x00\xb8\x14\xd6lq\x91CJ\xa8\tb\x14{\xd7/\xaex\xd7G\xd2`\x99\xda\xed^X\xf2\n\x0fZ\x00\xda\xbd\xbc\xb6\xb0\x8c\xcb<\xca\xa3\xdc\xd7\x8f|F\xf8\xac\x91Z\xb5\x96\x98\xc0\x92J\xb1S\\?\x8e>%\xcd\xadO,V\xb9\x8d3\x8c\x83\x9e\xe6\xbc\xd2i\xa5\x9d\xcb\xc8\xc5\x899\xc94\x015\xc5\xd3\xdc]=\xc36dc\x93\x9a\xf5\xef\x81\x16\xa2]Vi\xcfPz\xfe5\xe3\x00w\xcd{\xa7\xc05\x01\xe5b{\xff\x00\x85\x00}\x06\x9d1\xda\x9fLC\x9a}\x00\x07\xa5BV\xa6\xa44\x01\x8d\xadipj6\xe69c\r\x91\x8a\xc6\xf0\x17\x84\x13\xc2\x83Q\xf2\xd7h\xbat|}7\x7f\x8du\xc6=\xddi\xea1@\x0f\xa2\x8a(\x004\x94\xa6\x92\x80\n(\xa2\x80\x16\x91\x8e\x05-As/\x96\x9d3\x9a\x00]\xc7\xaeq\\\xff\x00\x88<S\xa7h\x10<\xb3N\x1aP\xbf*\x0es\\\xe7\x8e\xbc{\x16\x93\x10\xb3\xb2\xc4\xd7-\xc6\xd5?\xe1\\o\x87|\x1b\xa9\xf8\xaa\xf8j\x9a\xe4\xb2D\x91\xb6\xd5\x81\xb9\x04P\x02I\xad\xeb\x9f\x10\xf56\xb6\xb5G\x8a\xd7=s\x8e+\xb0\xd0\xbe\x13i6,./\x87\xdan2\x0eOj\xed\xb4\xad\x16\xcbJ\xb6X\xed-\xd2,\x0c\x1d\xbd\xebE"U$\x81\xd6\x80*Ah\x96\xb1\x08\xed\xa3\x11\xa8\xe3\xa5Y\x84\xb0S\xb9\xb7\x1c\xd4\x84\x1c\xd3\x04A\t\xc0\xc6y\xa0\x0f5\xf8\xd8\x8d\'\x83\x8e\xde\x81\xb2k\xa1\xf8p\xc1\xfc\x11\xa7`\xe7\x11(\xfd\x05S\xf8\x95\xa7\xb6\xa3\xe1\x99\xa0\x1d\x0f9\xac\xcf\x84\xda\xd2\x9f\x0e\xff\x00g\xcb\xb5e\x82FNO$\x0e\x05\x00zn8\xaeS\xc6^!\xb9\xd0\xed<\xcb[s+\x00N=k\xa4\xf3\xce\xf2\x9by\x14\xd7\x86)\xc1\xf3\xa3\x07>\xb4\x01\xe1\xba\xb7\xc5\xbda,\xd9\xbf\xb1\x02\x15\xfe/\xf2+\xc9\xfcO\xe3mC\xc4wFYI\x88\x0c|\xa3\xb1\xafx\xf8\xa7\xe2\x1b\r\x1bJ\x96\xda(!y\x1cc\xa6\x08\xaf\x99]\x96k\x87\x91\xfeP\xc7<\x1a\x00\xf4?\x08\xfcX\xd4|?\x1a\xdb\xb9-\x08\xf5\xafY\xd2>5\xe8\xf7\xc9\x18\x97\xe4\x91\xba\x83\x9a\xf9x\x8f\x98\xed\xce\xdfZ\x99b+\xb1\xf2\xc1[\xa3\n\x00\xfbb\xcb\xc5\x1ae\xfc\x02X\xaeT\x02;\xd2_x\x9bK\xd2\xe1\x13]^*\xa9\xe9\xde\xbes\xf0o\x81\xbcI\xafZ\x99-\xaf\xde({\x10\xe0\xd6\xcd\xb7\xc3}f]fHu\xeb\xb9\x1a\xca\x1e\x03\xb9\x18<g\xd6\x80=j\xe3\xe2w\x87\xa2\x19\x17cos\xb6\xb0\xae\xfe6\xf8~\xda\xe1\xa3@\xf2\xe3\xa7\x06\xbc\xdb\xc5\xfaW\x85\xf4\xa9\xe2\x86\xd4\xa4\xea8`\t\xfe\x86\xb4\xad\xad\xfc\tc\xa1\xc5z\xee\xa6\xe1\x97>AB@4\x01\xd1K\xf1\xee\xcbv!\xb0v\x03\xd8\xff\x00\x85*\xfc}\xb2\xc0\xdf\xa6\xb8=\xfa\xff\x00\x85dh>4\xf0T\xb0\xb2_h\xd0\xdb\x95\xe1\x08V;\xaa\xe4\x9e-\xf8|I\x12\xe9q\x87\xcf F\xc6\x805c\xf8\xf3\xa32\xfc\xf0:\x1f\xa3\x1f\xe9WO\xc6\x1d\x1e\xea\xd8\xb5\xbc\x80;\x0f\x97 \x8f\xe7\\\xe2\xf8\x83\xe1\xa4\xe32Y$x\xf4\x89\xab\x9a\xf1\x06\x87\xe1\x1dj\xee\xdc\xe8r\x88\x0c\xae\x03\xfc\xa4w\xf7\xa0\x05\xf1W\xc4\rv\xf4\xb0\xb5\xbb\xdb\x1e{\x11^_{}{u3\x9b\x8b\xa6wf\xcb`\xf7\xaf]\xd6\xbe\x11\xc5a\xa0\xf9\xf0\xeam7 \x1c\xa8\x1d\xab\xca\xaf\xb4!c.\xd6\xb8\x04\xe7\x8d\xa4\x1c\xd0\x06u\xbd\x9c\xb7\x17+\x1a!\x91\x89\xa7^ZOk)Y\xa2)\xcfq]\x9f\x81\xac^\xcb\xc4\x96\xb2]\x00m\xd8\x8f\x9d\xc8\x00W\xb9x\x8b\xe1\xf6\x99\xe2\r-\x1e\x08\xd1\x18\xa6w\xa8\xces\xde\x80>N<7\xb5{w\xc0i1q*\x9f\xefq\\G\x89\xfe\x1cj\xba%\xc3yP\xbc\x90s\xf3\x91\x8cW[\xf0<H\xba\xbb\xc7\xf2\xe0\x1c1\xcfC@\x1fI\'\x06\xa4\xa8\x16L!c\xf7Gz\x98\x10T\x11\xd0\xd0\x02\xd1E5\\7J\x00\\R\x8aB\xc0u4\xa0\xd0\x02\xd1E\x14\x00\x1aJSI@\x05\x14Q@\x0b^\x7f\xf17\xc5\x8f\xe1\xfb(\xad\xad\x86n\xae>\xe0\x19\xce3\x8f\xeb^\x80k\x83\xf1\x96\x82\x9a\xbf\x8a4\x99e\x19Hcn1\xc7Q\xd6\x809O\x03x\x0emNd\xd7u\xbd\xc6G\x19U5\xeb\xb1\xc6\x91(D@\xaa:\x00*;x|\xa5H\x93\x84Q\xc0\xabaE\x00"\x9c\xd3\x87ZM\xb8\xa5\x02\x80\x16\x98\xf99QO\xa4#\x9c\xd0\x05\x1b\x9bD\xbb\xb5\x96\t\x07\x0c1\xcdx\xf6\xb3\xe1mk\xc3\x1a\xa4\xba\x8e\x93\x1bH\xae\xdb\x8a\x0f\xaf\xe7^\xdaS\x9c\x8a\x8d\xa3\'\xa9\xc8=\xa8\x03\xc7\xa1\xf8\xb5\xab[[\xb2\xdch\xceg^3\x86\xff\x00\n\xc0\xd4\xfe8\xeaH\xad\x19\xb30\xc9\xd9I?\xe1^\x9d\xe3;\xfd\'\xc3\xfas\xcd41\x99\x9b%}k\xe5o\x11\xebM\xacj\xf2\xdd`\x05<\x0e:P\x04\x9e"\xf1=\xe7\x88\xa72]7|\xe35\x8f\r\xbc\x93\xb8H\xc6\xe6=\x05BX\x9a\xb1gv\xf6s,\xa9\xd4P\x07\xa3\xf8g\xe1N\xa5\xa8\xda\x8b\xeb\xc8\xc2\xda\xe3=A\xfd)\xdfb\xd0\xa3\xd6[E6\x8f$jq\x1b\xec={\xd6\xe7\x80\xfe\'\xc9\r\x91\xb5\xd4\x9d\xa5\x84\x0cl\xfc\xeb\xa0\xb6\xf1O\x80\x93R7\x92)\x8a\xe0\x1c\xf9~_\n}\xb9\xa0\x0c-+X\xd4\xbe\x19\xeaK\x15\xc4R\xbd\x8c\xa4`\x05<~C\xde\xa6\xf1\xa7\xc4\xc9\xb5\x98V\xc7O\xb7uG\x1f\x7f\x04z{WQy\xf1\x13\xc0\xda\xc4\x82\x1b\xf6y\xb1\xf7wE\xd2\xb9]\x7fJ}F\xe6\x16\xf0\xb4QMo ;\x19\x9fn:v\xe7\xde\x80<\xf6\xd3O\x8a\xdf_\x82-Kt\x8b3`\xf5>\x9f\xe3^\xbb?\xc3/\t\x80.\xe6\xd4\x04Q\x12\x19b8\x18\xfdk\x87\xf1\x1f\x81\xf5\xef\x0eMk\xab\xea2y\xeb\xf7\x98\x06\xce\xde\x95\xbf\xad&\x95\xaf\xf8z\xcbR{\xc7\xb72.\xe6T\\\xf7\xa0\x0c\xaf\x88\xd6^\x17\xb3\x97M\xfe\xcd\x99Y\x90\x8d\xdb}7V\xee\x9f}\xf0\xf2x#\x176\xdb\xae\xb1\xfb\xc1\xb1\xba\xd7(\xba\x7f\x82\x96T\x92\xebQ\x9eB\xa7\xa7\x91\xff\x00\xd7\xae\xdf\xc3K\xf0\xff\x00R\x95m\xaca\xdf8\xfb\xce\xf1\x95\xe7\xf3\xa0\x0ecY\xd6|\x1d\x15\xef\xd9\xec\xb4\xe0O\xa6\x1a\xb9\x9dv\xe2\x08\xe7\xb4\xba\xb6\xb2\x92\xd6\x18\xa4]\xec\x14\xf3\xcf\xbdZ\xf1\xde\x9b\x06\x99\xe3H\xd3MC*\x93\xc0Q\xef\xed^\xa1\xae\xf8b]S\xe1\xfd\x9cp\xda\xe6f\x88;\xe4\x11\x83\x83@\x17t\xbb\xcb?\x1ax"H\xa3\x90\xc7o\x1b\x80\xee?\xdd\xe6\xbc\xf3\\\xf0\x87\x83\xf4\xad2{\x98uo\xb4]\xc7\x92#\xd8:\xfe\x06\xb2t\x8f\x10\xea~\x0e\xb2\xba\xd1\xa5\xb7_*i\t\'wN1\xe9]/\x85to\t\xeb\xd0\xcb4\xaf\x1cw!Ien\x037\xd74\x01\xcci\x90.\xbb\xa0\xcf"\\y\r\x0eB\x8c\x0c\xe0\x0f\x7f\xadv\x1e\x06\xf8\xact\xd3\x1e\x93\xab11\xc5\x88\xd5\xc8\xeb\x8e3^{x"\xd2\xfcWsdn|\x8b\x12\xe4~\xe8\x06\x18\xcdI}\x04:\x94/o\xa6\xe9\xe6f^\x93\xb0*~\xb8\xa0\x0f\xa7\xcbi\xde)\xd2\x7fv\xc8\xf18\xea1\xc5xN\xa1\xa7\xea?\x0e|V\xb7\xb6\xd1\xbf\xf6{\xc9\x97lq\xd6\xba/\x83Z\xed\xcd\xbc\x92\xe9\x17\x80\x99\x0b`\x02zv\xae\xf7\xe2\x16\x86\xba\xdf\x86\xaeb\xce\x19\x14\x91\xc6s@\x1a\x96\x1e\'\xd2\xef\xb4x\xef\r\xe4i\x1b\x00[,\x07j\x9d<S\xa2\xb0\x01u\x18\xbf1_8\xf8\'\xc3w\xfe\'\xb9\xbb\xd3\x86\xa7-\xb2\xdb\x8f\xf5j\x01\x07\x9cWh~\x08\xdf.?\xe2s/\xe0\xa2\x80=\x85u\xcd6O\xbb\xa8\xc4\x7f\xe0B\xadEul\xe7\xf7s\xc6\xd9\xf4a^,\xbf\x07ux\xbf\xd5\xebsg\xdc\n\xcf\xbc\xf0\x9f\x8ft\x06\xf3m\xaf\x9e\xed\x14\xf0\xa5\x80\xa0\x0f\xa03\xb8t\x04}jE\xaf\x08\xd3>"\xf8\xabJ)\x05\xfe\x91#\xf2\x06w\x13\xfd+\xd9\xf4\x8b\xf7\xd4!2:l\xc0S\x8f\xa8\xa0\r:(\xa2\x80\x03IJi(\x00\xa2\x8a(\x01Ms\xfa\xbd\xdc6\xfa\xcd\xa4rc{\xa3\x15\xcf\xb1\x15\xd0\x1a\xf2\xcf\x8a\x17W\xba^\xb9\xa5jV\xf1\x97\x86(\xd8I\xe9\xc9\x14\x01\xe9\x89\xd7\x8az\xf5o\xads\xbe\x1c\xf1\x14^ \xd2\xd2\xe6\xdfa\x93\x1f2g\xa5o\xc1\'\x99\x1eO\x04u\x14\x015\x14f\x98d\x0b\xd6\x80\x1fE4043\xe3\x81\xd6\x80\x15\x98(\xc9\xacm\x7f_\xb7\xd1t\xd7\xba\x91\x81\x0b\xda\x9f\xackv\xfaU\x84\x93\\J\x8a@\xc8\x04\xf5\xaf\x98\xbe#\xfc@\xba\xd75Y\xad\xed\xdc\x0b`\xa0\x02\xacq@\x10\xfcF\xf1\xe4\x9e\'\xbd\t\x130\x892\x08\xaf=l\xe6\x94\xe4\x9c\x9ai4\x00R\x81\x9am(4\x01\xab\xa3\xdfGep\x1ah\xf7%{_\x87<\'\xe1\x1f\x15i\xf1O\xf2\xa5\xe3\xe7z\x908\xe4\xe2\xbc\x041\xcdj\xe9Z\xed\xde\x95t\xb3\xc1+)S\x9c\x03\xc1\xa0\x0f\xa4\xcf\xc1/\r\xb5\xbf\xcb\x83!\xfe-\xa2\xb9\x9b\xaf\x02\xf8\x93\xc3W\x8e\xba%\xc16\xcb\xfe\xacn\xe9\x9f\xc2\xb5|\x0f\xf1Z\xca\xf2\xd9a\xd4]RA\xc6{\xd7\xa9\xd8j\x16\x9a\x85\xaa\xcbo:H\x8d\xd3\x91\x9a\x00\xf0MP\xf8\xe7R\xb2\xfb.\xa6\x86T#\x18.O\xf4\xae^\xc6\xc7V\xd3\x91\xed/,\x1d\xed\xe2\xe0`\x121_V\xf9\x11\x95\x1b\x86\xe1\xefU\xa6\xd3\xed.>W\x89q\xe9\x8a\x00\xf9\x92=O@\x802\xdc\xe8.\xcd\xed\x13\x1a\xb9g\xe2\x8f\x0eiV\xd25\x9e\x97,\x17\x0c\x0e1\x11\xeb_C?\x85\xf4Y\x1b-a\x01\xfa\xa5V\x9b\xc1>\x1c\x94\xe5\xb4\x9bl\x9e\xa7`\xa0\x0f\x9at\x8f\x14\x88\xb5\xd3\xa9\xdd\xd8\xbc\xea\x0e@*zW\xa1\xdd|f\xbb\x96\xd0\xc7g\xa5>\x19p\xa3cW\xa9/\x82t%\x1bWN\x80/\xa6\xc1Va\xf0\xc6\x8bnF\xcd:\x01\x8f\xf6\x05\x00|\xcdq\xe1\xbf\x13\xf8\xba\xf9\xae\xde\xdfb\xb1\xc8\x1c\xf7?J\xdd\xd2>\x0ek\xa2\xe8\x14\xb90\x16\x1c\x90q\xfd+\xe8\xe8m\xa0\x81v\xc5\x12 \xf4\x02\x9cF\xd3\x9c\n\x00\xf1\xcd\x1b\xe0\x8c+p\xd3j\xd7>{\x13\xcfC\x9a\xe85=7C\xf06\x83r\xe9o\x19\x94\x8f\x90c\x9a\xec5\xadz\xcbC\xb2{\x9b\xb9U\x02\x8c\xf5\xaf\x06\xd5um[\xe2?\x89<\xabde\xb1\x8eM\xaaW8+\xce(\x03W\xe1F\x9bq\xa8\xeb\xf7z\xd4\xc9\xb1\x04\x84\xa8\xfck\xdbn\xe3I\xec\xe7\\\xf0\xc8k+\xc2\xfa\x0c:\x16\x94\x90F2\xc5F\xec\x81\xd7\x02\xa7\xd6\xb5Ht\xad\x0e\xe6\xf2\xe1\x82*#u\xef@\x1e1\xf0\xb6#\x17\xc4\xadI\x15\xf0\xb8#\x03\xfd\xea\xf7\xfc\x13^\x19\xf0\x83M7\x9e\'\xbe\xd6C\xbe\xd7-\x80G\x1fz\xbd\xd8t\xc5\x00 \xc9\x18\xaa\xfb\x86N\x11\x8f\xd4U\xba0(\x036]:\xde\xe8\x96\x96\xdd?\x11V\xed\xed\xd6\x05!z\x1cT\xc5A\xedB\xf1@\x0f\xa2\x8a(\x004\x94\xa6\x92\x80\n(\xa2\x80\x16\xb25\xdd"\xdfY\xb4{Y\xd4\x10\xc3\x83\xe9Z\xf4\xc6@\xcd\x93@\x1e\x07\xa8i~$\xf0\x16\xa8[JI%\xb2-\x93\x82\x7f\xa5v\x9a\x1f\xc5->\xee5\x86\xf70N\x0e\x1bp\xc0\xcf\xe2k\xd0\xa7\xb5\x86\xe2"\x93F\xae1\xd0\x8a\xf3\xdf\x10\xfc+\xb0\xd5e3\xda1\xb7\x90\xf5\xf2\xf8\xe6\x80;[mJ\xd6\xea1,7q\x15?\xed\n\xb1\xe7\xee\x00\xac\xb1\xe3\xd9\xab\xc6\x9b\xe1\xd7\x89t\xc5\xc5\x8e\xa9;\xa8\xe8\x19\xcf\x1f\xa5U\x1e\x1b\xf8\x82\x84\x84\xbco\xc5\xcf\xf8P\x07\xb8=\xf5\xb4)\xbaY\xe3\x1e\xfb\xab\x94\xf17\xc4\r7G\xb4\x7f"A5\xc1\x1f(^k\x83\x83\xc1>2\xbf;o/\x9dW\xa0\xda\xe7\xfc+\xa8\xd0\xfe\x16Z\xd9\xa0\x97S\xb9\x96\xeem\xc4\xe2C\x91\x8a\x00\xe05]?\xc4\x1e3\xd2\xee5\x13$\x90\xc02\xc0\x16##\xf1\xaf\x13\xbb\x89\xad\xae\xa5\x85\xceY\x18\xa9\xaf\xb3\xf5\xbd&\x18\xfc5=\xb5\xaem\xe3T<%|m\xac&\xcdf\xf13\x9d\xb30\xc9\xfa\xd0\x05<\xd2\x13E%\x00\x14QE\x00(\xa7\xed\xc2\x86=\xea1N$\x91\x8e\xd4\x01ad1a\xe2r\x0f\xadu>\x1c\xf1\xfe\xa9\xa2M\x187\x124*~\xee\xea\xe3A\xe2\x94\x1cP\x07\xd5>\x18\xf8\xb7\xa4\xdf\xc0\x89u>\xd7\x03\x9f\xf3\x9a\xee\xac\xb5m>\xfd\x16\xe2\x0b\xa8\xca\xc88\x05\x85|C\x14\xcf\x1be\x1d\x94\xfa\x83]\x0e\x91\xe2=~\xdeh\xa2\xb2\xbb\x9eNxBI\x14\x01\xf6z\xca\xa4|\xac\x1b\xe8i\xdea\xf4\x15\xf3\xdd\x97\x8e<q\xa5\xc2\x86m-\xe5\x8f\x19\xce\xc6&\xb4\xe1\xf8\xbf\xe2\x18\xff\x00\xd7hr\xec\x1d\xcc-@\x1e\xe8\t"\x98\xc4\xd7\x9a\xf8[\xe2U\xfe\xb7x!\x97L\x91\x17\xa6|\xb2+\xaf\xd7\xbcOe\xe1\xfb3qz\xc5r\tP\x07Z\x00\xdb\xf3\x15\x06]\x82\x8fs\\\xaf\x88\xfck\xa7\xf8~\'\xdf:I)\x19US\x93\xf4\xaf5\xd5>"\xeb\xda\xec\xa6=*\xd3\xf7=\x9c\xa9\xfe\x95kA\xf8_\x7f\xad\xdcE\xaax\x82\xeeL?\xcc"V\xe0\x0fL\x11@\x19\x12\xa6\xaf\xf1\x17V1\xba<vL}\xc7\x1f\x8dz\xf7\x87</e\xe1\xfb\x18\xa0\xb5\x8dw\xa2\x05f\xc7$\xf7\xab\xf6\x9av\x97\xa1[$H"\x85Tcq \x1a\xe5|C\xf1GA\xd1\x92H\x92W\x96pH\xfd\xd0\x07\x9f\xce\x80;\x89$[u\xdd+*\x0cw5\xe2?\x10\xfcX\xde#\xba]\x03O\xcb)\x93k\x95\xaa\xd3\xf8\x97\xc5^;v\xb6\xd3\xa16\xf6\xe4\xe3\xccl\xa9\xc5u\xde\x0c\xf8_\x06\x89z\xb7\xd7S<\xf7\x1c\x13\xe6`\x8c\xd0\x07S\xe0\xbf\x0eC\xe1\xdd\x12\xde\x08\xd7\xe7a\x96?\\WR\xabLH\xc2\xa8\x15 \xa0\x02\x8eh\xa5\x14\x00\x9c\xd0\x05-\x0b\xd2\x80\x16\x8a(\xa0\x00\xd2R\x9aJ\x00(\xa2\x8a\x00ZCKHh\x00\xa8]\x0ex$\n\x9a\x823@\x15\xbea\xc6\xf3K\xb1\xf3\xc3T\xfbG\xa0\xa0\x00:P\x04@9\xeeE8\xa9\xc7\'5%\x07\xa5\x00f\xeb)\x9d\x1a\xeb\xfd\xc3_\x12\xeb\xeb\xb3\xc4\x17\xe3\xfe\x9b\xbf\xf3\xaf\xb6\xb5\x162\xe9w#\xfd\x92+\xe2\xef\x15Bb\xf16\xa0\x08#31\xe7\xeb@\x18\xa6\x92\x9cE&(\x01)E\x14P\x01E\x14P\x01E\x14P\x01Z\x1a}\xfd\xc6\x9d<W\x118\xca\x9c\xe2\xb3\xe9\xca\xd8\x04c9\xa0\x0fY\xb6\xf8\xd3z\x96\x89\x04\xb6\x90\xc9\xb4`\xe5?\xfa\xf5+|i2\x00\xb2iv\xc5q\x8e#\xff\x00\xeb\xd7\x91\x02W<u\xa6\x9c\xd0\x07\xb2C\xf1\xa5-\x06\xebm:8\xdf\xd4G\xff\x00\xd7\xaek\xc4\xbf\x11\xaf<Myn\xd7X\xf2T\xe5\x97\x1d\xb3\xf5\xaf?\xa7g\xd6\x80=\xf3F\xf8\x93\xe1\xad\x1bM\x85b\xb5O0(\r\xf2\x0e\xbf\x9dE\xab|tt\x8d\x92\xc1p\xdf\xc3\xf2\xf4\xfdk\xc2(-\x928\xa0\x0e\xcf\\\xf8\x95\xafk{\x96k\xa7D?\xdd$Vf\x87\xac[[\xea\x02}IM\xc2g\'p\xdd\\\xf7zZ\x00\xfa\x9b\xc1\xde:\xf0\xcd\xed\xb2\xc1\x0cihp\x06@\x0b\xcf\xe7]\xed\xbe\xa5e.\xdf*\xea6\xc8\xe3\xe6\x06\xbe!\x8a\xeah\x87\xee\xa5d\xc7\xf7N+V\xc7\xc5Z\xd5\x8b\xabG\x7f9\x0b\xd1Y\xc9\x1f\xce\x80>\xdb\x8d\xd5\x97\x86\x07\xe8jQ_-h\x9f\x1bu\x8d<\x04\x9d#p09\x04\xff\x00Z\xf4}\'\xe3\x8e\x9dq\x087h\x11\x88\xed\x81\xfdh\x03\xd7\xe8\xcdp\x96\xbf\x15|=r\x99Y\xfen\xe3r\xff\x00\x8dY\x8f\xe2W\x87\xa4R\xc2\xed\x00\x1e\xae\xbf\xe3@\x1d\x86\xe1N\x06\xb8\xd7\xf8\x8f\xe1\xd0\x9b\x96\xf6&\xf6\x0e\xbf\xe3Z\xda\x07\x89\xec<D\'k\t7\x08\n\x87\xe9\xdf8\xe9\xf44\x01\xbbE\x14P\x00i)M%\x00\x14QE\x00-!\xa5\xa44\x00QE\x14\x00QE\x14\x00S\x1d\xb0E>\xa3p\xac\xc3,2(\x029#\x0f\x04\x89\x81\x86\xaf\x0b\xf1?\xc1{\xfd\x7f]\x9e\xfa\xd6X\xa3\x8d\x8f\xddc\x8e\x7f*\xf7\x93\x8cphU\x00\x1e\xd4\x01\xf3o\xfc3\xee\xb2?\xe5\xe6\x1f\xfb\xec\xff\x00\x85\x1f\xf0\xcf\x9a\xd9?-\xdd\xb0\x1e\xec\x7f\xf8\x9a\xfaS\xf1\xa0P\x07\xcd\x7f\xf0\xcfZ\xf7\xfc\xfeZ\xff\x00\xdfg\xff\x00\x89\xa4?\xb3\xce\xbf\x9f\xf8\xfc\xb4\xfc\\\xff\x00\x85}!\x1d\xd5\xbc\xb2\xbcQ\xcd\x1b\xc8\x9c:\xab\x02W\xea*_\xc2\x80>i\xff\x00\x86y\xf1\x07\xfc\xfeY\xff\x00\xdfG\xfc)\x7f\xe1\x9d\xf5\xf3\xff\x00/\xb6\x7f\xf7\xd9\xff\x00\n\xfaP\xb0\x1e\x94\x06\x04d`\xd0\x07\xcd_\xf0\xce\xfe \xff\x00\x9f\xdb/\xfb\xed\xbf\xc2\x94~\xce\xfe \xff\x00\x9f\xdb?\xfb\xec\xff\x00\x85}#%\xc40\xe3\xcd\x91\x13\'\x03s\x01\x93Rd\x1a\x00\xf9\xab\xfe\x19\xdf_\xff\x00\x9f\xdb/\xfb\xec\xff\x00\x85\x03\xf6}\xd6\x97\xad\xdd\xb6G\xa3\x1f\xf0\xaf\xa5r)\x86T\x0f\xb0\xb0\xdf\x8c\xed\xcf4\x01\xf3q\xfd\x9f\xf5\xa2\x7f\xe3\xea\x0f\xfb\xe8\xff\x00\x85\x07\xf6}\xd6G\xfc\xbd[\xff\x00\xdfG\xfc+\xe9\t\'\x86\x15\r,\x89\x18\'\x00\xb3\x01\x93R\x02\x08\xc89\xa0\x0f\x9a\x7f\xe1\x9f\xb5\x9f\xf9\xf9\xb7\xff\x00\xbe\x8f\xf8R\x1f\xd9\xef_\'\xe5\xbc\xb4\x03\xfd\xe3\xfe\x15\xf4\x9c\x97\x10B\xca\xb2\xca\x88[\xa0f\xc6jL\x8fj\x00\xf9\xa3\xfe\x19\xef\xc4\x1f\xf3\xfbg\xff\x00}7\xf8S\x87\xec\xf9\xad\x05\xf9\xae\xad\xcb{1\xc7\xf2\xaf\xa5s\xefFh\x03\xe6\xa1\xfb?k\'\xfe^ \x1f\xf03\xfe\x14\x1f\x80\x1a\xb0<\xdc\xc5\xf81\xff\x00\n\xfaI\xe5D ;*\x968\x19=ME%\xd5\xbcR\xa4rM\x1a\xbb\xfd\xc5f\x00\xb7\xd0w\xa0\x0f\x9c\xc7\xc0\x1dXt\xb8\x8b\xf1c\xfe\x14\xc3\xf0\x07Z\x1f\xf2\xf3\x07\xfd\xf4\x7f\xc2\xbe\x96\xc8\xa5\xc8\xa0\x0f\x9a\x07\xc0-h\xb770\x7f\xdfG\xfc)_\xf6~\xd7\xbc\xd1\x8b\xcb@\xbd~\xf3g\xf9W\xd2\xa7\x14\xc0\x988\x04\x9a\x00\xf0=+\xe0n\xa3c0i\xae\xed\x88?\xed\x1f\xea+\xa8\xd4\xbe\ri\x93\xd8\x15\xb7\x92A&\xdep\xc3\x04\xfeU\xea\x86 \xcb\x86\x14\xa20\x06\x01\xa0\x0f\x1b\xf0\xff\x00\xc1;+g&\xf2IX\x13\xd3p?\xd2\xbd\x0f\xc2~\x11\xb5\xf0\xa2\xdd\xa5\xa9$\\2\x96\xcf\xfb9\xc7\xf3\xae\x84\xc5\x9f\xe2"\x9c\xab\x8e(\x01\xf4QE\x00\x06\x92\x94\xd2P\x01E\x14P\x02\xd2\x1aZC@\x05\x14Q@\x05\x14Q@\x08\xdc\xd7\x97\xf8\xe3\xc3^&\xb7\xf1%\xbf\x8a|+},\x97ClS\xd8J\xff\x00\xbbu\xc8\x19\x00\xf1\x8f_\xce\xbdA\x8e\x06k\xc3~&G\xe3\xaf\x0b\xc1y\xe2\x08|T\xc2\xc1\xeeB\xc5h\x89\x82\x8a\xc7\x81\x92;P\x06\xff\x00\x88~\x1ek\xfa\xe6\xa9>\xac\xbe0\xba\xd2\xd2UWkh\x8b\x14\x88\x85\x01\x80;\x86FA\xe7\x15\xe6\x9e\x16\xd35o\x13\xea\xba\xa4?\xf0\x9e^Z\xd8\xd9\xca\xb0\xc5s$\xac\x0c\xec\xc4\x81\x81\xbb\x8c\xe3\xd6\xba\xcf\x10\xf8\x97_\xf1\xed\xe2x+@\x82h\x14F\x83Q\xbe\x94\x15\xfe\x10O\xd0\x1f\xd6\xb9\x8f\x04x\n?\x11i^.\xd1\x12b\xb7v7q\xfd\x96\xe3\x1d\x1dw\x8eG\xbe?\n\x00\xf6O\txWW\xf0\xae\x95\xa8\xc3>\xbb6\xads?\xcd\x03\xdc)\x1b\x08R\x00\xe4\x9e3\x8a\xe0u\xedw\xe2\xef\x874\x89\xb5=J\xebH\x8a\xd6/\xbd\xf2\xa1\'\xd8\x0e\xe6\xba\x7f\x86^7\xb8\xd4\xfc?}i\xaeG$Z\x86\x8a6\\\xb9RK(\x07\x9f\xf7\xb8 \xd7\x93\xfcB\xf1\x1e\xb1\xf1\x06\xd6\xebW\xb6\x86K\x7f\x0ei\xae\x117\xff\x00\xcbWc\x8c\xfd\x7f\x90\xa0\r\x1f\x03\xe9_\x12]g\xf1F\x8a\xd6%\xb5RY\xe4\xbae\xdc\xd8c\xc8\x07\xa0\xcdv;\xbe7\x1e\x16m\x1b\xf0\xf2\xff\x00\xc2\xbc\xca\xcc\xf8\x19l\xa0\x13\xdd\xf8\xade\xf2\xd7z\xc2\x06\xc0p3\xb7\xda\xae\xf8v}\x1d~$\xf8j=\x06\xebZx\x9e\xe3\x13.\xa0\xd8\xcf\xa6\x00\xed@\x1e\xede\xa5kz\xc7\x81\x9fN\xf15\xc0\x87S\xb8GI\xa5\xb3`6\xe4\x9c\x11\x8flW+\xe1\x83\xe3\x8f\x07\xe8\xda\xd5\xae\xa3hux\xb4\xf0\xbf\xd9\xed\xbb\xe7\x9cz\x0e\t\xc6=zWm\xe2\xfd+[\xd5\xb4O\xb3h:\xa0\xd3o|\xc5o<\xae\xef\x97\xb8\xc5p?\x0b\xf5/\x10\xdcx\xb3\xc4\xba\x16\xbb\xacI~t\xf0\xb1\xab\xf4\x00\x92rG\x14\x01\xc8\xf8\xe7]\xf1\x7f\x8dl-\xe1o\x03\xdf\xd9\xdc[K\xe6\xc5:31_Q\x8c\x0fj\xdc\xd3\xfe3x\x99\xaf\x93Fo\x06\xc9.\xa3\n/\x9b\x18\x91\xb7\xe3\x03,Wo\x1dA\xfcj-Vo\x12\xfc\x1e\xd4\xcd\xfa]\xcb\xacxr\xf2R^9\xdb\xe7\x8d\x8f\xb9\xef\xee85\xb1\xf0j\xd3\xfbY\xf5\xaf\x19\xdeI\x1c\x97\xda\x8d\xcb(P\xc0\x98\x90v>\x9d\xbf\x00(\x03_\xe2>\x99y\xa8\xc5o5\xaf\x8b\x0e\x89\xe4A#\xc9\x08|\x19\xb8\xc8\xee=\x08\xfck\x87\xf8M\x1d\x84Z]\xd7\x8c\xb5=Z\xe6\xebT\x81g_\xb3\xbd\xc6K"\xaeO\xcay5\xd1\xfcm\xd24\x06\xd0?\xb65\x18\x9e]I\x10[Y"\xcaW$\x9c\xf4\x1dq\xc9\xaf-\xf8x<:4\xcdD\xdf\xdb\xcf\x0e\xb1\xf6K\x83gp\xd2\x1f.Q\xe5\x90T\x0fQ\xcf\xe7@\x1b\x1f\x11>)\xda\xf8\xbfD\xb0\x8a\xcfG\xbe\xb6\x11^$\xbel\x98\xda\xe0g\xe5\x04w\xe6\xbd\'\xc2_\x17,\xbcC\xaf\xdbh\x0b\xa3\xdfZ\\I\x19!\xa7\xc0\x1c\x0c\xf4\xaf\x1f\xb8\xd64\xdf\xf8Sz\x06\x9c.\xe17\xb0\xeafI"\xcf\xcc\xab\xb9\xb9>\xd5\xdcZ\xea\xb6\x1a\xbf\xed\x03\xa4\xdc\xe9\xd7\x91\\\xc0\xba~\xc2\xf1\x1c\x80\xc1NE\x00e|Z\xf1\xee\x9f\xa8\xf8\x97K\xb5\x82+\xa4}\x1e\xf8\xfd\xa0\xb2\x80\x1f\x04}\xdey\xe8z\xd7A\xf1\x1f_\x9f\xc4\xde\x07\xd0\xf5}\x0e=I \x9e\xf0\x99\x12\x0c\xac\xbb\x00 \xe7i\xf6\xac\x9f\x8c\xfe#\xd1&\xd645\xb0\x9e\x1b\xab\xab\x1b\xb6{\x98a\x19l\x828\'\x1dr1Y\x9a\xaa\xebZ\xef\x88\xaeu[\xaf\x0e\xeb\xf1\xd9\xdc\xda\xa1\x82\xde\xc5\xd9\x04O\x81\x82{\x11\xeb@\x14\xb5\x93n\xdaT\xa3G\xb2\xf1\xacw\xc7\x1e[\\H\xc5:\xf3\x9cW\xd0~\x122\x8f\x08\xe9\x02s!\x9b\xec\x91\xf9\x9ea\xf9\xb7m\x19\xcf\xe3^\x00\xf6z\xcd\xc5\xb7\x86\xa1\xb8\xb5\xd6n\xd6\xda\xdaQ\x7f\x05\x94\xa4L\xacdm\xa1\xbd\x0fN\xb5\xde|=\xb1\xf1\r\xaf\x81\xbcO\x1cP_Z\xde\xbc\xf2\x1b\x05\xbd\xc9\x90\r\x83o_\xf3\x9a\x00\xa5\xe3\x9b\xf9|q\xf1GI\xf0\x8e\x9fr\xc9k\xa7\xbf\x9fx\xf1\xb60\xc3\x93\xc8\xf4\x1c}Z\xb8\xff\x00\x1bx\xd6[\x8f\x89?\xdb\x16\xb6F\xf3N\xd0\x1c[ ,v\x16\xc9\xf9\x89\xf7o\xcf\x15\x0f\x86|-\xafY|B\xd5\xf4X\xb5\x00\x9a\xd4\xda[\xb3L{;\x84b3\xeb\xce3]\x1f\x8d<\x17\x1f\x82\xbe\x08=\xa3\x10\xf7\xb3^E-\xd4\xa3\xf8\x9c\x93\xc0\xf6\x14\x01\xb1\x07\xc4\xff\x00\x1f\xdcB\x93C\xe0)\x1e)\x1422\xb3\x10\xc0\xf2\x0fJ\xdd\xd5\xbe#_h>\x00\x87[\xd5\xb4\x93m\xab\\Ha\x8a\xc4\x9f\xe2\xc9\xc19\xed\x81\x9a\xe6\xb4S\xf1\x8b\xfb\x1a\xc7\xec?\xd9?d\xfb:y%\xf6gf\xd1\x8c\xfe\x15\xea/\xe1\xebM{K\xd3\xcf\x88\xec\xa0\xba\xbc\x81U\xdb#\xe5Ip7\x15\xc7\xb8\xa0\x0f,\xbf\xf1/\xc5\x8d\x0bJ_\x11\xeaPX>\x9c\xbb^[UU\xdc\xa8}q\xc8\xafW\xf0\x9f\x88 \xf1O\x86\xec\xf5\x8bt(\x97\t\x92\x84\xe4\xa1\xe8F~\xb5\xe6\xdf\x12\xfcOw\xaej\r\xf0\xfb\xc3\xb6\xde}\xe5\xc0Qu)\xfb\xb1/q\xfc\xb2k\xd1<\x19\xe1\xc5\xf0\xaf\x85,t\x85\x7f1\xa0O\x9d\xc7FbrH\xfcM\x00t\x14QE\x00\x14\n(\x14\x00\xb4QE\x00\x06\x92\x94\xd2P\x01E\x14P\x02\xd2\x1aZC@\x05\x14Q@\x05\x14Q@\x08N\x075\xe3_\x1d\xfcCe.\x84\x9e\x1a\x83|\xda\x94\xb2\xa4\xe6(\xd7v\xc4\\\x9c\x9ct\xc8\xe6\xbd\x95\xbaW5k\xe0\xbd"\xd3\xc5W\x9e#X\x19\xf5\x0b\xa4\x08\xed#\x16\x0b\xc6\x0e\xd0zdP\x04>\x12\xf1\x16\x83\xa8\xe8\x16w67\xd6\x9b\x9a\x04Y\x06\xf0\xaf\xb8(\x18`y\xc8\xc6+\x8c\xf8Km6\x95\xafx\xc2[\xe8\xfe\xcf\x1d\xcd\xf6\xe8ZB\x14H7?#=z\x8a\xda\xd4\xbe\x0bx;S\xbc\x96\xe4\xd9\xcfm$\xa7s\x0bi\x8a.~\x878\xaa_\xf0\xa0\xfc!\xff\x00=uO\xfc\t\xff\x00\xebP\x07\xa1\xdb-\x89\x92ajm\xcb\xb1- \x8c\x8c\x92{\x9cW\x9e\xfcb\xb0\xb5\xd3>\x12\xdd\xdb\xd9\xc1\x1c\x10\xa4\xd1mH\xd7\x00e\xff\x00\xfa\xf5\xd2x?\xe1\xf6\x8d\xe0\x99\xae\xa4\xd2\xcd\xc9{\x90\xa1\xcc\xf2o\xe0t\xc7\x03\xd6\xae\xf8\xc3\xc2\xf0x\xbf\xc3\xd3h\xf7SI\x0c2\xb2\xb1x\xf1\x91\xb4\xe7\xbd\x00y\xbe\x8f\xa4\xfcR\x93D\xb0{MC@[c\x02\x18\x84\x90e\xb6\x95\x18\xcf\xcb\xd7\x15\x8d}i\xe2\xab_\x8a^\x0f\x1e\'\xb8\xd3\xe6v\x99\x8c?cM\xb8\x1d\xf3\xc0\xafn\xb6\xd3\x12\xdfD\x8bL\xcb\xb4)\x00\x80\x12pJ\x85\xdb\x9f\xadq\xba/\xc2-\x1bH\xd7\xed\xf5\x86\xbe\xd4onm\x8ea\x172\xe5P\xfeT\x01\xde__\xdb\xe9\x963^\xdeJ\xb1[\xc2\xa5\xdd\xcf@\x05|\xf7\xe1\x8f\x1aGg\xe2\xff\x00\x17j\xd6\x01\x16}T\x194\xd1v\n$\xe5[\xa6\xee\x80\xfas^\xeb\xe2O\x0fZx\x9fB\x9fJ\xbf2y\x13\x0eLlT\x829\x06\xb3u\x0f\x87\xfe\x1d\xd54\x1b]\x1a\xf3NI--P$;IVOpG4\x01\xe6\xfaW\x835_\x1b\xeaQk\x1e=\xd5`\xf2\xa2l\xc3\xa6\xc5*m\x03\xdfi\xc0\x1f\xa9\xab\x07\xc2:\x8f\x83|yo\xa8xF\xf6\xd4i\x17\xaf\x8b\xcbifP\x90\x8e\xfd\xf3\x8fLr\x0f\x15\xb0~\x02x79S\xa8\xa0\xf4\x17?\xfdj?\xe1BxCn<\xddO\xaf{\x81\xff\x00\xc4\xd0\x06\x8f\x8a|$\xda\xd7\x88\xa1\xd7\xee.<\xcb\x0b\r:o*\xdf\xaa\x89\x888o\xc8\xfe\x82\xb9\x7f\x83\x9e\x1b\xd3u\xef\x87;\xaf \r"\xdc\\\xc5\x1c\x9f\xc4\x81\xc0V\xc7\xe1^\xb2\xd6\t\xfd\x98l\x10\x95\x87\xc90\x8c\x0eB\xed\xc5ex+\xc26\xfe\n\xd0\xbf\xb2\xad.e\x9e/5\xa5\xdd(\x00\xe4\xe3\xd3\xe9@\x1eA\xf1?\xe1\xd7\x87\xfc!\xe1=3\xfb>\xd9\x9aw\xbfH\xdey\x1b.\xe8s\xc1\xafI\xd1\xfe\x17\xf8wG\xf1\x05\xae\xbb\xa6\xc3%\xb4\xf1E\xb4F\x8f\xfb\xbeF\t\xc1\xe7<\xfa\xd6\x9f\x8c\xbc\x1bo\xe3M>\xda\xce\xee\xeaX\x12\x0b\x85\x9c4`\x12H\xecs\xf5\xae\x92$1\xc4\xa9\x9c\xed\x00f\x80<+\xe2\xbe\x81\xa4\xe9^\'\xf0\xdd\xe5\x85\xacq\\\xdej[\xee$RIs\xb9\x7f\xfa\xf5O\xe24k7\x8a\xa5\xb7\xf0\xff\x00\x895K\xbdf\xee`\xbf\xd9\xd6\xb2\x11\x1d\xbf@rG\xf2\xafH\xba\xf8Q\xa0\xdfx\xa8\xf8\x82\xeaK\xb9n<\xe1:\xc2e\xfd\xda\xb8\xc7A\xf5\x19\xae\x8e\xc7\xc2\xfa>\x9b\xab^j\x96\x96\x11G}xs4\xc0d\xb7\xf8~\x14\x01\xf2\xed\xb7\x86\xbcC\x16\xa7\xe2\x13a\x7fy$\xfa\\\xaa/|\x87+$\xa9\x93\xb9\x87<\xe3\x15\xee\x1f\t\xbf\xb2\xdfK\xba\xb8\xd3\xfcGw\xab4\xc5\x0c\x91]\x9f\xde[\x90\x0f\xcaG\xe3\xd7\xda\xba\x1d\x03\xc1\x16z\x0f\x885\x8d^\x1b\x89\xa4\x9bT}\xd2\xa4\x98\xda\xbc\xe7\x8cV\x9e\x93\xe1\xad\'C\x9e\xeem6\xc2+g\xbb\x7f2b\x83\x1b\x8f\xf4\x1e\xd4\x01\xe6:X\xc7\xed9\xaa\x7f\xd7\x8f\xfe\xca\x95\xad\xf1\xeb?\xf0\xac\xe7\xff\x00\xaf\xa8\x7f\x99\xae\x86\xdf\xc0\xb6\xd6\xff\x00\x10n<^.\xe5\xfbL\xf0y&\x02\xa3`\xe0\x0c\xe7\xf0\xab>4\xf0\x94>4\xd0\x1fG\xb9\xb9\x92\xde&\x95d\xde\x8a\t\xca\xf6\xe6\x80<\xff\x00C\xf0\x97\xc4\xa9\xf4M>kO\x1b\xdbCn\xf6\xd1\x98\xe36\xf9\xda\xa5A\x03;{\n\xf5\xad>+\x9b}:\xde+\xc9\x84\xf7)\x18\x12\xca\xa3\x01\xd8\x0eN=\xe8\xd2\xec\x86\x9b\xa5\xda\xd8\xab\x97[x\x96 \xc4`\x90\xa0\x0c\xd5\xba\x00\xf1\xff\x00\x04\xea\xb6\x17\xff\x00\x16\xf5\xd1\x0f\x87n,\xee\xf0\xe2K\xc7\x99\x9b~\x08\xea\xa4as\xd4W\xaf\xafJh\x89\x15\xd9\x82\x00\xcd\xd4\x81\xd6\x9f@\x0bE\x14P\x01@\xa2\x81@\x0bE\x14P\x00i)M%\x00\x14QE\x00-!\xa5\xa2\x80\x12\x8aZ(\x01(\xa5\xa2\x80\x12\x8cR\xd1@\tE-\x14\x00\x94R\xd1@\tE-\x14\x00\x94R\xd1@\tE-\x14\x00\x94R\xd1@\tE-\x14\x00\x98\xa2\x96\x8a\x00J)h\xa0\x06\xd1\xf8S\xa8\xa0\x04\xa2\x96\x8a\x00J)h\xa0\x04\xa2\x96\x8a\x00J1KE\x00\x14QE\x00\x06\x92\x94\xd2P\x01E\x14P\x07\xff\xd9'

with open('7img.jpg','wb') as file:
    file.write(content)


# 场景：网络请求传输图片，电脑与电脑之间传输图片，本质上传的都是二进制。