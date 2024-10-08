def vowelsToUpper(s):
    vowels = "aeiou"
    return ''.join([char.upper() if char.lower() in vowels else char for char in s])

user_input = input("Enter a string: ")

print(vowelsToUpper(user_input))
