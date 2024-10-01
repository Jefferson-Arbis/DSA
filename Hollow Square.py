n = int(input("Enter the side length of the square: "))

for i in range(n):
    if i == 0 or i == n - 1:
        print('x' * n)  # Print the top and bottom rows of the square
    else:
        print('x' + ' ' * (n - 2) + 'x')  # Print the middle rows with spaces in between
