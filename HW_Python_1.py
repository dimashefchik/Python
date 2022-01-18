a = str('Hello')
a1 ='Hello'
print(type(a))
b = int(11)
b1 = 12
print(type(b1))
c = float(124.1234)
c1 = 123.55
print(type(c1))
d = bytes(b"it's my python homework")
d1 = (b"it's my python homework")
print(type(d1))
e = list([1,25,57,'one','twenty five','five'])
e1 = [1,25,57,'one','twenty five','five']
print(type(e1))
f = (10, 2.13, "square", 89, 'C')
print(type(f))
g = ('hello', 'group', 'hello', 'group26')
g1 = set(g)
print(g1)
set.remove(g1,'group26')
print(g1)
g2 = frozenset(g)
print(g2)
# set.remove(g2,'group26')
# print(g2)

h = dict(name='Dima', age=29, group=26)
print(h)

k = 'Hello '
m = 'Everybody'
n = k + m
print(n)

v = 50
q = 12
w = v + q
print(w)
w_1 = v/q
print(w_1)
w_2 = v * q
print(w_2)
w_3 = v//q
print(w_3)
w_4 = int(v%q)
print(w_4)
t = 'dima'
print(v,',', t)
print(v,'+', t)
