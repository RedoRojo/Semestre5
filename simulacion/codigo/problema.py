pequenio = int(input())
grande = int(input())

numero = int(input())

peces = []

for i in range(numero): 
    pez = int(input())
    peces.append(pez)
cont = 0

for i in range(pequenio, grande+1):
    for j in peces: 
        if((j*2<=i<=j*10) or (i*2<=j<=i*10)): break
        if(j==peces[-1]): cont+=1
        
print(cont)