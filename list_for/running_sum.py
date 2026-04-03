l2 = list(range(1,100))

prvValue  = 0

print('for loop started')
for l2Value in l2:
    currentAdd = prvValue + l2Value
    prvValue = currentAdd
    print(f' prvValue = {prvValue}, currentAdd  = { currentAdd } , l2Value = {l2Value}')
    print()

print('for loop ended')