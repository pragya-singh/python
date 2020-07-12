# Decorator function is a wrapper function.

# A simple decorator is as follows. raw() is a function which does a task. But we want to do some other task before 
# performing raw. Which can be acheived by 'raw=decorator(raw), but Pyhton has given Syntatic Sugar to do this. Which
# is done by giving @decorator before defining raw. 
# Same has been done on divide function. safeguard is decorator for divide.

def decorator(f):
 def g():
  print("Getting decorated")
  f()
 return g 

@decorator
def raw():
 print('needs decoration')

#raw = decorator(raw)

def safeguard(f):
 def g(x,y):
  if(y == 0):
   print("Divide by zero is not possible")
  else:
   return f(x,y)

 return g

@safeguard
def divide(x,y):
 return x/y

#divide = safeguard(divide)

if __name__ == "__main__":
 print(divide(2,0))
 print(divide(2,1))
 raw()


