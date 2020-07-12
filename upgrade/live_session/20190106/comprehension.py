# Implementing own map, reduce and filter functions, instead of using
# map, reduce and filter built-in functions given by Python.

# Comprehension:
# Is the syntactic sugar to write map, reduce and filter 
# operations on list. 
def myMap(f,l):
 nl = []
 for el in l:
  nl.append(f(el))
 return nl

def myReduce(f,l,acc):
 out=acc
 for i in range(0,len(l)):
  out = f(out,l[i])
 return out

def myFilter(f,l):
 nl = []
 for el in l:
  if f(el):
   nl.append(el)
 return nl

if __name__ == "__main__":
 nums = [1,2,3,4,5,6,7,8,9,10]
 print(myMap(lambda x:2*x, nums))
 print(myReduce(lambda x,y:x+y, nums, 1))
 print(myFilter(lambda x:(x%2)==0, nums))
# Comprehension 
 lst = [x*x for x in nums if x%2==0]
 print(lst)
