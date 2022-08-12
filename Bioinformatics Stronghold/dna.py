
problem = "dna"
input = open("data/rosalind_%s.txt" % problem, "r").read()

def dna(seq):
    count = {"A":0, "C":0, "G":0, "T":0}

    for n in seq:
        if n in count.keys():
            count[n] += 1
    return " ".join(str(i) for i in count.values())


print(dna(input))
