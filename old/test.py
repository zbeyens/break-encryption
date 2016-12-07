

chars = words = lines = 0
with open('res2.txt', 'r') as in_file:
    for line in in_file:
        lines += 1
        words += len(line.split())
        chars += len(line)
        print(len(line))
