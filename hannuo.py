def moveplate(n, placeA, placeB):
    print("把第",n,"层从",placeA,"移动到",placeB)
    
def Hannuo(cengshu, a, b, c):
    if cengshu == 1:
        moveplate(cengshu, a, c)
    else:
        Hannuo(cengshu-1, a, c, b)
        moveplate(cengshu, a, c)
        Hannuo(cengshu-1, b, a, c)
 

layers = 3
a="a"
b="b"
c="c"
Hannuo(layers, a, b, c)