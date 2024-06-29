def main():
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
        if x % 2 == 0:
            plist.append(x)
        x += 1


    return plist


if __name__ == '__main__':
    main()
