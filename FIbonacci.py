'''
#
# int n, a=0, b=1, temp=0, i=0;
# printf("\nEnter the number of terms : ");
# scanf("%d", &n);
# printf("The fibonacci series is : \n");
# for(i=0; i<n; i++)
# {
#     printf("%d \t", a);
#     temp = a + b;
#     a = b;
#     b = temp;
# }
# 
'''

def fibo(x):
    a= 0
    b= 1
    temp= 0
    n=x
    for x in range(n):
        print(f"{a} is {x} item ")
        temp = a+b
        a=b
        b=temp



x= int(input("Enter the no of item: "))
fibo(x)


