# Return the sum of the numbers in the array, except ignore sections of
# numbers starting with a 6 and extending to the next 7 (every 6 will
# be followed by at least one 7). Return 0 for no numbers.
def sum67(nums):
  sum = 0
  i = 0
  while i < len(nums):
    if (nums[i] != 6):
      sum += nums[i]
      i += 1
    else:
      i = nums.index(7, i) + 1
  return sum
