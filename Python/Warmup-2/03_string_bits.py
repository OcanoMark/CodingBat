# Given a string, return a new string made of every other char
# starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  res = ""
  for x in range(len(str)):
    if (x % 2 == 0):
      res += str[x]
  return res
