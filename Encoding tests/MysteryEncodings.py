#-*- coding: utf-8 -*-
#!/usr/bin/env python3
import base64
import os

files = "message4_i.txt.enc","message5_i.txt.enc"

filesb = "message4_b.txt.enc","message5_b.txt.enc"
#filesrb = "message4_b.txt","message5_b.txt"

r4b = "Do you know that reading other people's letters is not very nice and not polite?\nI am not doing that knind of things! Shame on you! Shame, shame, shame!\nWho on earth gets into my personal life like that? And why are you doing it?\nIs someone forcing you? No? If not, then what the hell is wrong with you?\nWhat are you trying to do? Are you trying to break my cryptosystem?\nMy messages to Alice are strictly confidential! Only me, Alice and the NSA can read this e-mails..\nSo, dear hacker, stop it right now!\nBest regards,\nBob.\n"

r5b = "What are you trying to do? Are you trying to break my cryptosystem?\nI am not doing that knind of things! Shame on you! Shame, shame, shame!\nWho on earth gets into my personal life like that? And why are you doing it?\nIs someone forcing you? No? If not, then what the hell is wrong with you?\nDo you know that reading other people's letters is not very nice and not polite?\nMy messages to David are strictly confidential! Only me, David and the NSA can read this e-mails..\nSo, dear hacker, stop it right now!\nBest regards,\nBob.\n"

rb = r4b, r5b

cc = ["windows-1251","ascii",
 "big5",
 "big5hkscs",
 "cp037",
 "cp424",
 "cp437",
 "cp500",
 "cp720",
 "cp737",
 "cp775",
 "cp850",
 "cp852",
 "cp855",
 "cp856",
 "cp857",
 "cp858",
 "cp860",
 "cp861",
 "cp862",
 "cp863",
 "cp864",
 "cp865",
 "cp866",
 "cp869",
 "cp874",
 "cp875",
 "cp932",
 "cp949",
 "cp950",
 "cp1006",
 "cp1026",
 "cp1140",
 "cp1250",
 "cp1251",
 "cp1252",
 "cp1253",
 "cp1254",
 "cp1255",
 "cp1256",
 "cp1257",
 "cp1258",
 "euc_jp",
 "euc_jis_2004",
 "euc_jisx0213",
 "euc_kr",
 "gb2312",
 "gbk",
 "gb18030",
 "hz",
 "iso2022_jp",
 "iso2022_jp_1",
 "iso2022_jp_2",
 "iso2022_jp_2004",
 "iso2022_jp_3",
 "iso2022_jp_ext",
 "iso2022_kr",
 "latin_1",
 "iso8859_2",
 "iso8859_3",
 "iso8859_4",
 "iso8859_5",
 "iso8859_6",
 "iso8859_7",
 "iso8859_8",
 "iso8859_9",
 "iso8859_10",
 "iso8859_13",
 "iso8859_14",
 "iso8859_15",
 "iso8859_16",
 "johab",
 "koi8_r",
 "koi8_u",
 "mac_cyrillic",
 "mac_greek",
 "mac_iceland",
 "mac_latin2",
 "mac_roman",
 "mac_turkish",
 "ptcp154",
 "shift_jis",
 "shift_jis_2004",
 "shift_jisx0213",
 "utf_32",
 "utf_32_be",
 "utf_32_le",
 "utf_16",
 "utf_16_be",
 "utf_16_le",
 "utf_7",
 "utf_8",
 "utf_8_sig"]
 
 
def xoring(s1,s2):
	return "".join(chr(ord(x) ^ ord(y)) for x,y in zip(s1,s2))
 

for i in range(2):
	for c in cc:
		fname = "_"+files[i]+"_"+c+".txt"
		try:
			
			fread = files[i]
			file = open(fread,"rb")
			m64 = file.read()
			file.close()
			m = base64.b64decode(m64).decode(c)
			
			fread = filesb[i]
			file = open(fread,"rb")
			m64 = file.read()
			file.close()
			s = base64.b64decode(m64).decode(c)
			
			res = xoring(xoring(rb[i],m),s)
		
	
			file = open(fname, "w", encoding=c)
			file.write(res)
			file.close()
		except:
			try:
				file.close()
			except: pass
			try:
				os.remove(fname)
			except: pass

		try:
			if os.stat(fname).st_size == 0:
				os.remove(fname)
		except: pass