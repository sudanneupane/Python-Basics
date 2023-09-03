'''
                ## 29th April
# Regular expression:
            these are using to maake searching easier by writting pattern 

#pattern are written using some standard symbols


(), searches if the search key is present in this group
., matches any letters
|, searches for either of the pattern written having symbol | in between
{2}, searches whether the input has exactaly the specified number of occurance
?, zero or one occurance
+, one or more occurance 
*, zero or more occurance
$, checks whether the input ends with the letter or word specified prefixded with the symbol $
^ or \A, checks whether the input starts with the letter or word suffixed with the symbol ^
[a-z], checks whether the onput has anything in the given range 
\, it is used to remove the builtin meanings
\b checks whether the input starts or ends  with the letter or word specified suffixed = starts or prefixed = ends 
\B matches anywhere but not in the begining and ending
\d matches any of digits 
\D matches anything but not digits
\s matches for any types of spaces
\S matches anything but not the spaces
\w matches a-z, 0-9 (word)
\W matches anything but not the words


'''

# Program to check if the string staris with "This" and ends with " sity" 

import re   # regular expression are supported in th emodune name "re" in python

string1 = "This year khelo india is at our jain university"
#res = re.search("^This.*sity\\b", string1)    #search function returns match object upon sucess or else NONE upon condition faliure
#res = re.search("\\AThis.*sity$", string1)
#print(res)  

res = re.search("\s",string1)
print(res.start())              # start() function is used to dislay the first match position of the given pattern 

res = re.findall("i" ,string1)  # findall() function is used to  display all the matches of the pattern 
print(res)

res = re.split("\s",string1)   # split() function is used to display the input  string as a list [], {}, ().
print(res)

res = re.sub("i", "1", string1) # sub() function replaces the search pattern with a new string or a letter in the given input string
print(res)


