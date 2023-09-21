'''
compress
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.
'''

# My Solution

def compress(s):
  j = 0
  i = 0 
  compressed = []
  
  while True:
    if j == len(s):
      num = j - i
      if num == 1:
        compressed.append(s[i])
      else:
        compressed.append(str(num) + s[i])
      return "".join(compressed)
    
    if s[i] == s[j]:
      j += 1
      continue
    
    else:
      num = j - i
      if num == 1:
        compressed.append(s[i])
      else:
        compressed.append(str(num) + s[i])
      i = j

# Instructors Solution
# Note the removal of the additional conditional logic above with the additional special char at the end of the string
'''
n = length of string
Time: O(n)
Space: O(n)
'''

def compress(s):
  s += '!'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1  
    else:
      num = j - i
      if num == 1:
        result.append(s[i])
      else:
        result.append(str(num)) 
        result.append(s[i])
      i = j
    
  return ''.join(result)