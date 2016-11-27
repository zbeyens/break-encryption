#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

####CE PROGRAMME DECODE TOUS LES FICHIERS grâce au fichier b sauf le j

import base64
encodings = ["utf-8", "ascii", "latin"]
initial_encoding = "latin"
textes = []
sorties = []
letters = "abcdefghij"
for i in (letters):
	textes.append("message7_"+i+".txt.enc")
	sorties.append("message7_"+i+".txt")

#Mettre ici l'encodage qu'on devine du fichier de départ
#Si c'est pas le bon ça plante -> suggestion faire un try-except

def xoring(s1,s2):
	return "".join(chr(ord(x) ^ ord(y)) for x,y in zip(s1,s2))

enc = []
for t in textes:
	f = open(t)
	m64 = f.read()
	f.close()
	m = base64.b64decode(m64).decode(initial_encoding)
	enc.append(m)

listing = []
for i,tt in enumerate(enc):
	#print(letters[i], len(tt))
	listing.append((len(tt),letters[i]))
listing.sort()
print(listing)
	
problem = "message7_h.txt.enc"
f = open(problem)
m64 = f.read()
f.close()
m = base64.b64decode(m64).decode("latin_1")
print(len(m),"problem h")

sol = xoring(enc[1],enc[7])
aa="""Делать нечего: бояре,\nПотужив о государе\nИ царице молодой,\nВ спальню к ней пришли толпой.\nОбъявили царску волю -\nЕй и сыну злую долю,\nПрочитали вслух указ\nИ царицу в тот же час\nВ бочку с сыном посадили,\nЗасмолили, покатили\nИ пустили в Окиян -\nТак велел-де царь Салтан."
aa="Делать нечего: бояре,\nПотужив о государе\nИ царице молодой,\nВ спальню к ней пришли толпой.\nОбъявили царску волю -\nЕй и сыну злую долю,\nПрочитали вслух указ\nИ царицу в тот же час\nВ бочку с сыном посадили,\nЗасмолили, покатили\nИ пустили в Окиян -\nТак велел-де царь Салтан.\n\nВ синем небе звезды блещут,\nВ синем море волны хлещут;\nТуча по небу идет,\nБочка по морю плывет.\nСловно горькая вдовица,\nПлачет, бьется в ней царица;\nИ растет ребенок там\nНе по дням, а по часам.\nДень.прошел - царица вопит...\nА дитя волну торопит:\n"Ты, волна моя, волна?\nТы гульлива и вольна;\nПлещешь ты, куда захочешь,\nТы морские камни точишь,\nТопишь берег ты земли,\nПодымаешь корабли -\nНе губи ты нашу душу:\nВыплесни ты нас на сушу!"\nИ послушалась волна:\nТут же на берег она\nБочку вынесла легонько\nИ отхлынула тихонько.\nМать с младенцем спасена;\nЗемлю чувствует она.\nНо из бочки кто их вынет?\nБог неужто их покинет?\nСын на ножки поднялся,\nВ дно головкой уперся,\nПонатужился немножко:\n"Как бы здесь на двор окошко\nНам проделать?" - молвил он,\nВышиб дно и вышел вон."""
aa = aa[:478]
aaa = aa.encode("utf-8").decode("latin")
sol = xoring(sol,aaa)
print(sol)
print(len(sol))

tt = "What are you trying to do? Are you trying to break my cryptosystem?\nSo, dear hacker, stop it right now!\nWho on earth gets into my personal life like that? And why are you doing it?\nDo you know that reading other people's letters is not very nice and not polite?\nI am not doing that knind of things! Shame on you! Shame, shame, shame!\nIs someone forcing you? No? If not, then what the hell is wrong with you?\nMy messages to Alice are confidential! Only me, Alice and the NSA can read this e-mails..\nBest regards,\nBob\x00\x00\x00\x00"

kk = "Helsinki is the capital of Finland, it is one of the largests cities in the country.\nMore than 600 tousand people live there. The city is 715 square kilometers,\nit is standing on the shore of the golf of Finland in the South of the country.\nHelsinki is in the UTC+2 time zone.\nAmong the most famous views of Helsinki you can find  Helsinki Cathedral, Parliament House,\nview of central Helsinki, beaches at Aurinkolahti,  Sanoma building and Kiasma and Suomenlinna.\nDo you think you'll meet polar bears in Helsinki?\n"

kk = xoring(xoring(enc[1],enc[7]),tt)
"""
print(repr(kk))
print(len(tt),len(kk),len(enc[0]),len(enc[1]))
##keystream = xoring(xoring(xoring(enc[0],enc[1]),kk),tt)
print(repr(xoring(enc[0],kk)))
keystream = xoring(enc[1],tt)
print(repr(keystream))"""

for i,fname in enumerate(sorties):
	res = xoring(xoring(enc[1],enc[i]),tt)
	if(i==7 or i==8 or i==9):
		file = open(fname,"w",encoding="latin")
		print(fname)
	else:
		file = open(fname,"w",encoding="utf-8")
	file.write(res)
	file.close

