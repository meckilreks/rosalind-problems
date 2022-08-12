
problem = "ba1b"
input = open("data/rosalind_%s.txt" % problem, "r").read().split("\n")

a = input[0]
b = int(input[1])


def FreqPattern(text, k):
    dict = {}

    # s = start; e = end
    for s in range(len(text)-k+1):
      e = s + k
      window = text[s:e]
      if window in dict.keys():
        dict[window] += 1
      else:
        dict.update({window:1})

      most_freq = ""
      max = 0
      for mer in dict.keys():
        if dict[mer] > max:
          max = dict[mer]
          most_freq = mer
        elif dict[mer] == max:
          most_freq += " " + mer

    return most_freq

print(FreqPattern(a, b))
