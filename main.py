def main():
    import sympy

    plist = []
    ##################################################
    # Comlete your code here
    ##################################################
    while True:
        x = int(input("First integer value greater than 1: "))
        if x > 1:
            break

    while True:    
        y = int(input("Second integer value greater than 1: "))
        if y > x:
            break

    while x < y:
        if sympy.isprime(x):
            plist.append(x)
        x += 1

    print(plist)
    return plist


if __name__ == '__main__':
    main()
