
def GenerateEvenDifferencecSquares():
    for i in range(1, 100):
        for k in range(1, 100):
            a = 2*i*k
            b = i*k**2-i
            c = i*k**2+i
            print(i, k, "  ", a,b,c)

def GenerateOddDifferencecSquares():
    for i in range(0, 100):
        for k in range(0, 100):
            a = (4*i+2)*k-(2*i+1)
            b = (4*i+2)*k**2-(4*i+2)*k
            c = (4*i+2)*k**2-(4*i+2)*k+(2*i+1)
            print(i, k, "  ", a,b,c)

print("Even Difference Squares")
GenerateEvenDifferencecSquares()
print("Odd Difference Squares")
GenerateOddDifferencecSquares()
