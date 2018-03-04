#####################################################################################

# Theory of Computation Assignment 1 Section 1

# NAME: Jamie Sweeney

# STUDENT NUMBER: 2137284s

#####################################################################################

# Background definitions

# Fixed point operator

fix = lambda f:  (lambda y: f(lambda z: y(y)(z)))(lambda y: f(lambda z: y(y)(z)))

#####################################################################################

# Booleans

T = lambda x: lambda y: x

F = lambda x: lambda y: y

cond = lambda b: lambda t: lambda e: b(t)(e)

def decodeBool(b):
    return b(True)(False)

#####################################################################################

# Natural numbers

pair = lambda x: lambda y: lambda z: z(x)(y)

fst = lambda p: p(T)

snd = lambda p: p(F)

Z = lambda x: x

S = lambda x: pair(F)(x)

iszero = lambda x: x(T)

P = lambda x: x(F)

Add = lambda f: lambda x: cond(iszero(x))(lambda y:y)(lambda y:S(f(P(x))(y)))

add = fix(Add)

def decodeNat(n):
    if decodeBool(iszero(n)):
        return 0
    else:
        return 1+decodeNat(P(n))

#####################################################################################

# Binary trees

# We have node as a recursive pair containing {is_leaf,{value,{left,right}}}
Node = lambda v: lambda l: lambda r: pair(F)(pair(v)(pair(l)(r)))

# Take first from second pair
val = lambda n: (n(F))(T)

# Take first from third pair
left = lambda n: (n(F))(F)(T)

# Take second from third pair
right = lambda n: (n(F))(F)(F)

Leaf = lambda x: x

isleaf = lambda x: x(T)

#Takes tree and initial value n
#If tree is leaf return n
#Else return the size (left)(size(right)(n+1))
size = lambda t: cond(isleaf(t))(lambda n: n)(lambda n: size(left(t))(size(right(t))(add(S(Z))(n))))

#Takes tree and initial value n
#If tree is leaf return n
#Else return the sum (left)(sum(right)(n+val))
sum_of = lambda t: cond(isleaf(t))(lambda n: n)(lambda n: sum_of(left(t))(sum_of(right(t))(add(val(t))(n))))

def decodeTree(x,decodeVal):
    if decodeBool(isleaf(x)):
        return []
    else:
        return [decodeVal(val(x)), decodeTree(left(x),decodeVal),
                                    decodeTree(right(x),decodeVal)]

t = Node(S(Z))(Node(S(Z))(Leaf)(Leaf))(Node(S(S(Z)))(Leaf)(Leaf))

print (decodeTree(t,decodeNat))
print (decodeNat(size(t)(Z)))
print (decodeNat(sum_of(t)(Z)))
