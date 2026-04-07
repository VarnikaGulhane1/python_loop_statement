l1 = list(range(1, 100))

# l2 = even list 
# l3 = odd list

l2 = []
l3 = []

for val in l1 :
    if val % 2 == 0:
        print(f"val = {val} is even")
        l2.append(val)
    else:
        print(f"val = {val} is odd")
        l3.append(val)

print(l2)
print('')
print('')
print('') 
print(l3)

# problem statement + logic = result