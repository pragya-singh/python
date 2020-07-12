# Functions are first class objects in Python.
# - Can be passed as parameter of a function
# - Can be returned as output of a function
# - Can stored in a data structure 

def myMax(x,y):
 if x>y:
  return x
 else:
  return y

def newMax(f, x, y):
 if(f(x,y)):
  return x
 else:
  return y

def gt(x,y):
 return x > y

def gt_text(x,y):
 return len(x) > len(y)

def gt_date(dt1,dt2):
 d1,m1,y1 = dt1
 d2,m2,y2 = dt2
 if y1 > y2:
  return True
 elif y2 > y1:
  return False
 else:
  if m1 > m2:
   return True
  elif m2 > m1:
   return False
  else:
   if d1 > d2:
    return True
   else:
    return False

if __name__ == "__main__":
 d1 = (9, 3, 2018)
 d2 = (6, 1, 2019)
 
# Using myMax without Higher Order Function
# The logic for different data types, may change. Hence
# we need different versions of myMax version. Which is 
# cumbersome.
 print("max(1,2)=",myMax(1,2))
 print("max(3,1)=",myMax(3,1))
 print("max(IIITB,Bangalore)",myMax("IIITB","Bangalore"))
 print("max({},{})".format(d1,d2),myMax(d1,d2))
 print("=============================")
# Using myMax with Higher Order Function.
# See how the HOF has made the code more flexible and easier.
# Now any new data type which needs to be compared, we need to define a new function
# for that date type and just it has to be plugged for that data type.
 print("max(1,2)=",newMax(gt,1,2))
 print("max(3,1)=",newMax(gt,3,1))
 print("max(IIITB,Bangalore)",newMax(gt_text, "IIITB","Bangalore"))
 print("max({},{})".format(d1,d2),newMax(gt_date, d1,d2)) 
