

def recursive_reverse(string):
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]


a = input("Enter a string to be reversed: ")
print(recursive_reverse(a))