t1 = int(input('Primeiro termo: '))
r = int(input("Razão da PA: "))
tf = t1 + 10 * r
for a in range(t1, tf, r):
    print(a)
