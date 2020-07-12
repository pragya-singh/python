
def addPolynomial(pol1,pol2):
 keys1 = set(list(pol1.keys()))
 keys2 = set(list(pol2.keys()))
 merged_keys = keys1 | keys2
 keys = sorted(list(merged_keys))
 l = len(keys)
 out = {}
 for i in range(1,l+1):
  k = keys[0-i]
  v = pol1.get(k,0)+pol2.get(k,0)
  out[k] = v
 return out 

def printPolynomial(pol):
 out = ""
 end = "+"
 length=len(pol.keys())
 count=0
 for key in pol:
  if count == length-1:
   end = ""
  if key == 0:
   out+=str(pol[key])+end   
  else:
   out+=(str(pol[key])+"X^"+str(key)+end)
  count+=1
 return out 

if __name__ == "__main__":
 pol1 = {5:3,2:1,0:2}
 pol2 = {5:2,4:2,2:2,1:3}
 print("f1(x)={}, f2(x)={}, f(x)=f1(x)+f2(x) => f(x)={}".format(printPolynomial(pol1),printPolynomial(pol2),printPolynomial(addPolynomial(pol1,pol2)))) 
