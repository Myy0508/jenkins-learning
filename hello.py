age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

    sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum

for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'
