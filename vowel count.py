st=input("Enter the string")
v=0
for ch in st:
        c=ch.lower()
        if(c=='a'or c=='e'or c=='i'or c=='o'or c=='u'):
                v=v+1
print("The no.of vowels is:- ",v)        
