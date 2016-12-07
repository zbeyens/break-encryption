# CryptoProject

#Encrypt:
```
openssl enc -aes-128-ctr -kfile secret.key -nosalt -iv DEADBEEFCAFEBABEDEADBEEFCAFEBABE -in lorem.txt -a -out lorem.enc
```
#Decrypt:

```
openssl enc -aes-128-ctr -d -kfile secret.key -nosalt -iv DEADBEEFCAFEBABEDEADBEEFCAFEBABE -in lorem.enc -a -out loremDEC.txt
```

#Interface:
```
#argv[1] = team number
#argv[2] = # files to decrypt (increasing order)
#argv[3] = mode 1 or 2
#Example: decrypt files a, b, c, d, e of team2 in mode 1:

python input.py 2 5 1
```
