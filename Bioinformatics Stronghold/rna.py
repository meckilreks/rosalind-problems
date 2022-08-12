
problem = "rna"
input = open("data/rosalind_%s.txt" % problem, "r").read()


def rna(seq):
    return seq.replace("T", "U")

print(rna(input))
