user_age = input("Enter your age : ")

print(f"user_age = {user_age}, type of user_age = {type(user_age)}") 

valid_user_age = int(user_age) #change the input type later to trap that it will be an user error and not the code error if enters wrong input

print(f"valid_user_age = {valid_user_age}, type of valid_user_age = {type(valid_user_age)}")

if valid_user_age < 0:
    print('Invalid age! Age cannot be negative.')
elif valid_user_age < 10:
    print('user is child')
elif valid_user_age < 18:
    print('user is teenager')
elif valid_user_age < 60:
    print('User is an adult')
else:
    print('User is a senior citizen')

