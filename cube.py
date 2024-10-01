def cube_of_array(arr):
    return [x ** 3 for x in arr]

size = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

if len(arr) != size:
    print(f"Error: You must enter exactly {size} elements.")
else:
    cubes = cube_of_array(arr)
    print("The cube of each element is:")
    for cube in cubes:
        print(cube)