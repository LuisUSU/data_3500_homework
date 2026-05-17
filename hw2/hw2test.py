number = [0,1,2,3,4,5]
square = []
cube = []

headers = ["Number","Squares","Cube"]


for sq in number:
   square.append(sq ** 2)

for cu in number:
   cube.append(cu ** 3)

print("Number\tSquare\tCube")

for n,s,c in zip(number,square,cube):
    print(n,s,c,sep="\t",end="\n")