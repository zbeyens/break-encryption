import base64
encodings = ["utf-8", "ascii", "latin"]
initial_encoding = "latin"
#Mettre ici l'encodage qu'on devine du fichier de départ
#Si c'est pas le bon ça plante -> suggestion faire un try-except

def xoring(s1,s2):
	return "".join(chr(ord(x) ^ ord(y)) for x,y in zip(s1,s2))

f= open("m3.enc")
m1_64 = f.read()
f.close()
m1 = base64.b64decode(m1_64).decode(initial_encoding)
#print("\nm3.enc\n"+m1)


f= open("m2.enc")
m2_64 = f.read()
m2=base64.b64decode(m2_64).decode(initial_encoding)
f.close()
#print("\nm2.enc\n"+m2)

print("\nm1.enc ^ m2.enc")
m1m2 = xoring(m1,m2)
print(m1m2)


f=open("m3.txt")
p1 = f.read()
f.close()

print("\nplaintext1")
print(p1)
print("\nm3.enx ^ m2.enc ^ plaintext1 === plaintext2 ???")
print(xoring(m1m2,p1))