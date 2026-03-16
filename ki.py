nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
s = []
jok = [1]*n

for i in range(n):
    sor = input().split(' ')
    for j in range(m):
        sor[j] = int(sor[j])
    s.append(sor)

if n > 1:
    for i in range(m):
        legkisebb = 1001
        indexe = [0]
        for j in range(n):
            if s[j][i] < legkisebb:
                legkisebb = s[j][i]
                indexe = [j]
            elif s[j][i] == legkisebb:
                legkisebb = s[j][i]
                indexe.append(j)
        for k in range(len(indexe)):
            jok[indexe[k]] = 0   

p = -1
while jok[p] < 1:
    p += 1

if p < 0:
    print(p)
else:
    print(p+1)

# teso nem törölj má ki