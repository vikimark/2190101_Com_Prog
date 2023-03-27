def overlap_occurence(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

dna = input().upper()
command = input()
if command == 'D':
    pair = input()
valid = True
for ch in dna:
    valid &= ch in ['A', 'T', 'C', 'G']
if not valid:
    print("Invalid DNA")
elif command == 'R':
    dna = dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
    dna = dna.upper()[::-1]
    print(dna)
elif command == 'F':
    occur = []
    chs = ['A', 'T', 'G', 'C']
    for ch in chs:
        occur.append(dna.count(ch))
    print("A={}, T={}, G={}, C={}".format(*occur))
elif command == 'D':
    print(overlap_occurence(dna, pair))