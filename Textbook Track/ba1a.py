
problem = "ba1a"
input = open("data/rosalind_%s.txt" % problem, "r").read().split("\n")

a = input[0]
b = input[1]

def Count(text, pattern):
    k = len(pattern)
    dict = {}

    # s = start; e = end
    for s in range(len(text)-k+1):
      e = s + k
      window = text[s:e]
      if window in dict.keys():
        dict[window] += 1
      else:
        dict.update({window:1})

    return dict[pattern]

print(Count(a, b))
