# Find All Occurrences of a Pattern in a String

problem = "ba1d"
input = open("data/rosalind_%s.txt" % problem, "r").read().split("\n")

input1 = input[0]
input2 = input[1]

def FindOccurances(pattern, text):
    k = len(pattern)

    occurances = []
    for s in range(len(text)-k+1):
      e = s + k
      window = text[s:e]

      if window == pattern:
        occurances.append(str(s))

    output = " ".join(occurances)
    return output

print(FindOccurances(input1, input2))
