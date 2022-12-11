#print("Hola mundo".find('13'))
tup = ('16-12-2005',) #('A', 'B', 'C')
s = ''.join(tup)
print(s) 
print(type(s))# AB
nacimiento=s.split('-')
print(nacimiento)
dia_nac=int(nacimiento[0])
print(type(dia_nac))

tup = (3,) #('A', 'B', 'C')
s = tup[-1]
print(s) 
print(type(s))# AB

a='>13'
print(int(a[1:3]))
print(type(int(a[1:3])))