# Find Patterns Forming Clumps in a String

problem = "ba1e"
input = open("data/rosalind_%s.txt" % problem, "r").read().split("\n")

input1 = input[0]
input2, input3, input4 = [int(i) for i in input[1].split(" ")]


def PotentialPatterns(seq, k, t):
    dict = {}

    # s = start; e = end
    for s in range(len(seq)-k+1):
      e = s + k
      window = seq[s:e]
      if window in dict.keys():
        dict[window] += 1
      else:
        dict.update({window:1})

    most_freq = []
    for mer in dict.keys():
      if dict[mer] >= t:
        most_freq.append(mer)

    return most_freq


def FindOccurances(pattern, seq):
    k = len(pattern)

    occurances = []
    for s in range(len(seq)-k+1):
      e = s + k
      window = seq[s:e]

      if window == pattern:
        occurances.append(s)

    return occurances


def FindClumps(seq, k, L, t):
    output = set()

    potentials = PotentialPatterns(seq, k, t)
    dict = {}
    for p in potentials:
      dict.update({p: FindOccurances(p, seq)})

    for p, o in dict.items():
      for i in range(len(o)-t+1):
        distance = o[i+(t-1)] - o[i]
        if distance <= L:
          output.add(p)

    return " ".join(output)



print(FindClumps(input1, input2, input3, input4))
