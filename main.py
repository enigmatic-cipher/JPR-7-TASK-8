"""
Given a String as input, count the number of lowercase alphabets n the string. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> "x1Y2Z3qw"
Output-> 3
"""

def countLower(st):
  ln = len(st)
  if (ln==0):
    return 0

  count = 0
  ch = st[0]
  if (ch>='a' and ch<='z'):
    count = count + 1
  return (count + countLower(st[1:]))

st = "x1Y2Z3qw"
print(countLower(st))
