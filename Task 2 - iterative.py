

def iterative_reverse(st):
    n = len(st)
    rev_str = ''
    for i in range(n-1, -1, -1):
        rev_str += st[i]                                   # rev_str = st[::-1] (Alternative method)
        print(rev_str)


st = input('Enter a string to be reversed')

iterative_reverse(st)