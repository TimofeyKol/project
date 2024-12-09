
a = int(input())
f = a
b = str(a)
m = a%10
a = abs(a//10)
c = 1  
while a > 0:
    if a % 10 > m:
        m  = a % 10
    a = a//10
    c += 1
syst_chisl = m + 1
print(int(b, syst_chisl))
