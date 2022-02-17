infile = open("AI.txt", "r")
import string

freq_dict = {}

removetable = str.maketrans("", "", string.punctuation)
infile = [s.translate(removetable) for s in infile]

for line in infile:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")


for w in words:
    if w in freq_dict:
        freq_dict[w] = freq_dict[w] + 1
    else:
        freq_dict[w] = 1

print(freq_dict)
