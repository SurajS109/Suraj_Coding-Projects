"""
word = 'banana'
count = 0
for letter in word:
    if letter == 'n':
        count = count + 1
print(count)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
"""

text = "X-DSPAM-Confidence:    0.8475"
x = text.find('0.8475')
print(x)