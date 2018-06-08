# Given a string, return a string where for every
# char in the original, there are two chars.
def double_char(str):
  dbl = ''
  for i in range(len(str)):
    dbl += str[i] * 2
  return dbl
