
# 1768. Merge Strings Alternately
def merge_alternately(word1, word2):
  """
  Don't use string concat for the output string.
  Python strings are immutable; every time you concatenate, a new string is created.
  Time complexity of concat is O(N^2); time taken is proportional to length of string.
  Instead, create an empty list for the output characters.
  Then return an empty string with the list joined to it.
  A string is created one time, rather than in every loop / iteration.
  Time complexity is now O(N), avoiding the quadratic. Nice! :)
  https://stackoverflow.com/questions/37133547/time-complexity-of-string-concatenation-in-python
  """

  # ret = ""
  ret = []
  i = 0

  while i < len(word1) or i < len(word2):
    if i < len(word1):
      ret += word1[i]
    if i < len(word2):
      ret += word2[i]
    i += 1

  return "".join(ret)

def test_merge_alternately():
  word1 = "SCREAM"
  word2 = "elephantboots"
  m = merge_alternately(word1, word2)
  print(m)

test_merge_alternately()
