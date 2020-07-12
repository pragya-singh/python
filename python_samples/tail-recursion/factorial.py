def fact_helper(acc,n):
    if(n==0):
        return acc
    else:
        return fact_helper(acc*n,n-1)

def fact(n):
    return fact_helper(1,n)

def permutation(n,r):
    return fact(n)/fact(n-r)

def combintation(n,r):
    return fact(n)/(fact(r)*fact(n-r))

print("Factorial of 0="+str(fact(0)))
print("Factorial of 1="+str(fact(1)))
print("Factorial of 2="+str(fact(2)))
print("Factorial of 3="+str(fact(3)))
print("Factorial of 4="+str(fact(4)))

print("P(4,0)="+str(permutation(4,0)))
print("P(4,1)="+str(permutation(4,1)))
print("P(4,2)="+str(permutation(4,2)))
print("P(4,3)="+str(permutation(4,3)))
print("P(4,4)="+str(permutation(4,4)))

print("C(4,0)="+str(combintation(4,0)))
print("C(4,1)="+str(combintation(4,1)))
print("C(4,2)="+str(combintation(4,2)))
print("C(4,3)="+str(combintation(4,3)))
print("C(4,4)="+str(combintation(4,4)))

