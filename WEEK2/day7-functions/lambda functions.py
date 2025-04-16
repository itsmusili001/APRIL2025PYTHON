#lambda argument:expression

def trippler(n):
    return n*3
print(trippler(20))


trippler2=lambda x: x*3
print(trippler2(20))

print((lambda x:x*3)(25))

print((lambda x:x+5)(25))

print((lambda x:x*x)(30))
