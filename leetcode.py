
def main():
  test_largest_altitude()

# 1732. Find the Highest Altitude
def largest_altitude(gain):
  """
  String formatting methods, interpolation, f-strings, formatted string literals in Python
  https://realpython.com/python-f-strings/

  More string formatting with arguments
  https://note.nkmk.me/en/python-format-zero-hex/

  print("i=%s, prev=%s, gain=%s, current=%s, altitude=%s" % (i, prev, gain[i], current, altitude))
  print(f"i={i:03d}, prev={prev:03d}, gain={gain[i]:+04d}, current={current:03d}, altitude={altitude}")
  """

  altitude = [0]
  highest = 0

  for i in range(len(gain)):
    prev = altitude[i]
    current = prev + gain[i]
    altitude.append(current)
    print(f"i={i:03d}, prev={prev:03d}, gain={gain[i]:+04d}, current={current:03d}, altitude={altitude}")
    if current >= highest:
      highest = current

  return highest

def test_largest_altitude():
  # gain = [-5, 1, 5, 0, -7]
  # gain = [-4, -3, -2, -1, 4, 3, 2]
  gain = [44, 32, -9, 52, 23, -50, 50, 33, -84, 47, -14, 84, 36, -62, 37, 81, -36, -85, -39, 67, -63, 64, -47, 95, 91, -40, 65,
   67, 92, -28, 97, 100, 81]
  print(f"largest_altitude={largest_altitude(gain)}")

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
