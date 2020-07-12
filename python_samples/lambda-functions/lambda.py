def caller(callback,x):
    return callback(x)

def myCallBack(x):
    return x*x*x

print(caller(lambda x:x, 2))
print(caller(lambda x:x*x, 2))
print(caller(myCallBack, 2))

