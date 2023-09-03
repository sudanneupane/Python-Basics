import sys

def checkBraces(str):
    res = False
    try:
        for i in range(0,len(str),2):
            if(str[i]=='(' and str[i+1]==')'):
                res = True
            elif(str[i]=='{' and str[i+1]=='}'):
                res = True
            elif(str[i]=='[' and str[i+1]==']'):
                res = True
            else:
                res = False
    except IndexError:
        sys.exit('False')
    return res

def main():
    string =  input("Enter the condition:\t")
    print(checkBraces(string))
    
if __name__ == "__main__":
    main()