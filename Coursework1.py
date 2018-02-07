#####################################################################################

# Theory of Computation Assignment 1 Section 1

# NAME:

# STUDENT NUMBER:

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

# THE SOLUTION TO SECTION 1 GOES HERE

# Binary trees

def decodeTree(x,decodeVal):
    if decodeBool(isleaf(x)):
        return []
    else:
        return [decodeVal(val(x)), decodeTree(left(x),decodeVal),
                                    decodeTree(right(x),decodeVal)]
    

                      



