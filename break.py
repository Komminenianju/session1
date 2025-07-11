'''
s=input()
s2=s.lower()
a=s2.count('a')
e=s2.count('e')
i=s2.count('i')
o=s2.count('o')
u=s2.count('u')
print(f"number of vowels:{a+e+i+o+u}")
'''
year=int(input())
leap=false
if year%100==0 and year%400==0:
    leap=true
elif year%4==0:
    leap=true
else:
    leap=false
print(leap)
