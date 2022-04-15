def getVal(d, searchkey):
    pattern=searchkey.split('/')
    res=[]
    temp=[[]]
    for i in range(len(pattern)):
        for key i d.keys():
            if key==pattern[i]:
                temp[0]=d[key]
                res=d[key]
                break

        d=temp[0]
    return res

a="x/y/z"
print(getVal({"a":{"b"{"c":"d"}}},"a/b/c"))
print(getVal({"x":{"y"{"z":"a"}}},a))

