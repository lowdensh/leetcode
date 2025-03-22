
def main():
  test_can_place_flowers()

# 605. Can Place Flowers
def can_place_flowers(flowerbed, n):
  count = 0

  for i in range(len(flowerbed)):
    # Target the success case first.
    # Only check adjacent spots if the current one is valid.
    if flowerbed[i] == 0:

      # Now check either side, accounting for the special cases at the start and end of the flowerbed list.
      # You need to check the special cases first, otherwise, IndexError: list index out of range.
      if i==0 or flowerbed[i-1]==0:
        left_empty = True
      else:
        left_empty = False

      # IMO, the 4 lines below are more naturally readable.
      # But, there is a way of writing these 4 with only 1 line instead:
      #   right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
      if i==len(flowerbed)-1 or flowerbed[i+1] == 0:
        right_empty = True
      else:
        right_empty = False

      # If both plots are empty, then we have met the success case.
      if left_empty and right_empty:
        flowerbed[i] = 1
        count +=1

  if n <= count:
    return True
  return False

def test_can_place_flowers():
  # flowerbed = [1,0,0,0,1,0,0]
  flowerbed = [1,0,0,0,1]
  n = 2
  print(can_place_flowers(flowerbed, n))

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


if __name__ == '__main__':
    main()
