
# The function should return True if the number is between 10 and 20 (inclusive), but it doesn't. Find the bug.
# l9ogic error you forgot to make it "or equal to"
def is_between(num):

     if num >= 10 and num <= 20:

          return True

     return False