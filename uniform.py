def check_uniform(n):
    n = str(n)
    for i in n:
        if i != n[0]:
            return False
    return True

def are_equal(a):
    return a

def arent_equal(a,b):
    count = 0
    for i in range(a,b+1):
        if check_uniform(i):
            count += 1
    print(count)

while True:
    a = int(input("Enter a number(A): "))
    b = int(input("Enter a number(B): "))
    if 0 < a <= b <= 10**12:
        if a == b:
            are_equal(a)
        else:
            arent_equal(a,b)