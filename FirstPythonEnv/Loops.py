words = ['one', 'two', 'three', 'four', 'five']

n=0
print ('-------- WHILE LOOP ----------')
while (n<5):
    print(words[n])
    n += 1
print ('')
print ('-------- FOR LOOP ----------')
for i in words:
    print(i)

print ('-------- WHILE LOOP ----------')
secret = 'Swordfish'
pw = ''
while pw != secret:
    pw = input('What is the secret word.?')


