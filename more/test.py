import base64
encodings = ["utf-8", "ascii", "latin"]
initial_encoding = "latin"
#Mettre ici l'encodage qu'on devine du fichier de départ
#Si c'est pas le bon ça plante -> suggestion faire un try-except

def xoring(s1,s2):
	return "".join(chr(ord(x) ^ ord(y)) for x,y in zip(s1,s2))

f= open("m1.enc")
m1_64 = f.read()
f.close()
m1 = base64.b64decode(m1_64).decode(initial_encoding)
print("\n\tm1.enc\n"+m1)

f= open("m2.enc")
m2_64 = f.read()
m2=base64.b64decode(m2_64).decode(initial_encoding)
f.close()
print("\n\tm2.enc\n"+m2)

print("\n\tm1.enc ^ m2.enc")
m1m2 = xoring(m1,m2)
print(m1m2)


f=open("m1.txt")
p1 = f.read()
f.close()

print("\n\tplaintext1")
print(p1)
print("\n\tm1.enx ^ m2.enc ^ plaintext1 === plaintext2 ???")
print(xoring(m1m2,p1))
