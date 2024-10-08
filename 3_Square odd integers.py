def square_odd_integers(lst):
    return [x**2 for x in lst if x % 2 != 0]

user_input = input("Enter a list of integers separated by spaces: ")
user_list = list(map(int, user_input.split()))

print(square_odd_integers(user_list))
