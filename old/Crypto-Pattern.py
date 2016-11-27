import sys
			
def xorStrings(s,t):
    """xor two strings together"""
    return hex(int('0x'+''.join(hex(ord(a))[2:] for a in s), 16) ^ int('0x'+''.join(hex(ord(b))[2:] for b in t), 16))

def main():
	listOfXORMess = []
	for x in range(1,len(sys.argv)):
		for y in range(x+1,len(sys.argv)):
			with open(sys.argv[x], 'r') as file1, open(sys.argv[y], 'r') as file2:
				cyphertext1 = (file1.readlines())[0].splitlines()[0]
				cyphertext2 = (file2.readlines())[0].splitlines()[0]
				xorText = xorStrings(cyphertext1, cyphertext2)
				listOfXORMess.append(xorText)
	for hexMess in listOfXORMess:
		print(hexMess)

main()