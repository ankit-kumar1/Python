"""
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits."""

s = input()
odd=[]
lower=[]
upper=[]
even=[]

for elem in s:
    if elem.isdigit():
        if int(elem) % 2 == 0:
            even.append(elem)
        else:
            odd.append(elem)
    elif elem.islower():
        lower.append(elem)
    elif elem.isupper():
        upper.append(elem)

print(''.join(sorted(lower))+''.join(sorted(upper))+''.join(sorted(odd))+''.join(sorted(even)))
