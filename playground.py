a = 2
b = 'Test'
c = True
print(a, b, c)

d = b + 'Hello'
print(d)

print(f'c is {c}, => fstring')

l = [1, 2, 3, '4']
print(f'list is {l}')

t = (1, 2, 3, 4)
print(f'tuple is {t}')
dt = {
    'name': 'SS',
    'team': 'ODDS',
}
print(f'dt is {dt}')

print(f'list at Index 0 is {l[0]}')
print(f'tuple at Index 1 is {t[1]}')
print(f'dt at key team is {dt["team"]}')

a = 2
if a == 1 and b == 3:
    print(a)
elif a == 2:
    print('equal 2')
else:
    print('not 1')
# else if == else แล้ว if อยู่ข้างใน
# elif == else if

for item in l:
    print(item)
    if item == a:
        print('yeah')

for it in dt:
    print(dt[it])
    print(it.key)
    print(it.value)
