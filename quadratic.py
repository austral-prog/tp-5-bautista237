def roots(a, b, c):
    r1 = ((-b+((b2)-4ac)0.5)/2a)
    r2 = ((-b-((b**2)-4ac)**0.5)/2a)

    if  (b*2)-4ac<0:
        return "( )"
    elif r1!=r2:
        return f"({r1}, {r2})"
    elif r1==r2:
        return f"({r1})"


def value_y(a, b, c, x):
    t1 = axx+bx+c
    return t1


def to_string(a, b, c):
    A=a 
    B=b
    C=c
    if a!=0:
        if b==0:
            return f"f(x) = {A} * X^2 + {C}"
        else:
            return f"f(x) = {A} * X^2 + {B} * X + {C}"
    elif a==0 and b!=0:
        return f"f(x) = {B} * X + {C}"
    else:
        return f"f(x) = {C}"

def derivation(a, b,c):
    if a!=0 and b!=0:
        return f"f'(x) = {2a} X + {b}"
    elif a==0 and b!=0:
        return f"f'(x) = {b}"
    elif a==0 and b==0:
        return f"f'(x) = 0"
    elif a!=0 and b==0:
        return f"f'(x) = {2a} X"
