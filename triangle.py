def triangle(a,b,c):
    val = False
    if a+b>=c:
        if a+c>=b:
            if c+b>=a:
                val =True
    return val
