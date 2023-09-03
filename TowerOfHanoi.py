######################      12th May 2022   ######################

# Implement the solution for the tower of Hanoi problem.

def toh(n, s, d, i):
    if n == 1:
        print(f"move disc {n} form source {s} to destination {d}. ")
        return 
    toh(n-1, s, i, d)
    print(f"move disc {n} from source {s} to destination {d} ")
    toh(n-1, i, d, s)

n = int(input("How many discs you have?  "))

toh(n, 'p1', 'p2', 'p3')

# on top of A we have B, on top of B we have C. here in this code, disc1 is C, disc2, is B, disc3 is A