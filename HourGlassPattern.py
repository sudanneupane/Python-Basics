def star():
    print("*", end="")

def space():
    print(" ", end="")

def pattern(n):
    # n = 6
    i = n
    x = 0
    ranze = ((2*n)-1)
    while (i <= n):        
        if (i == n):
            for j in range(n):
                star()
                space()
        else:
            for k in range(ranze+1):
                if ((x == (n-i) and x==k) or k==(ranze-x-1) or k==x):
                    star()
                else:
                    space()
        print()
        x = x + 1
        if (x<n):
            i = i-1
        else:
            i = i+1        

def main():
    size = int(input("Enter the size of the HourGlass:\t"))
    pattern(size)

if __name__ == "__main__":
    main()
