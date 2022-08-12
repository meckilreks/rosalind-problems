
problem = "ba1c"
input = open("data/rosalind_%s.txt" % problem, "r").read().split("\n")[0]


def PatternCount(seq):
  map = {
    "A": "T",
    "G": "C",
    "C": "G",
    "T": "A"
  }

  output = ""
  for n in seq[::-1]:
    output += map[n]
  return output

print(PatternCount(input))
