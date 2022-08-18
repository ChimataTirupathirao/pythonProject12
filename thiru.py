def primenum01():
    n=int(input("enter any number"))
    d=2
    c=0
    if n<=0:
       return "pls enter positive number"
    elif n==1:
       return "nethier prime or composite number"
    else:
       if d<n:
         if n%(d)==0:
            c+=1
         else:
            c=+0
         d+=1
       if c==0:
         return " not a prime number"
       else:
         return " prime number"

n=primenum01()
print(n)
