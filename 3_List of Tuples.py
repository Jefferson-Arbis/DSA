def list_of_tuples(list1, list2):
    return [(list1[i], list2[i]) for i in range(min(len(list1), len(list2)))]

user_input1 = input("Enter the first list of integers separated by spaces: ")
list1 = list(map(int, user_input1.split()))

user_input2 = input("Enter the second list of strings separated by spaces: ")
list2 = user_input2.split()

print(list_of_tuples(list1, list2))
