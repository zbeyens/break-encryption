#-*- coding: utf-8 -*-
#!/usr/bin/env python3

tt = """Kryptografie je umenie komunikovať v pr�\xadtomnosti protivn�\xadka. Táa je základom modernej po�\�\xadta�\x8dovej bezpe�\xBezpe�\x8dnostné výskumn�\xadci vytvoriť bezpe�\x8dnostné algxistuje mnoho takých algoritmov, najznámejš�\xad je šifroie. �\xa0ifrovanie nám poskytuje spôsobko preniesť dôverné informácie."""

cc = "latin-1"

file = open("_" + cc + ".txt", "w", encoding=cc)
file.write(tt)
file.close()
