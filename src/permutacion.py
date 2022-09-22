import math

def compara(base,m):
  for n in range(m):
    if (base**n) < math.factorial(n):
      return n
  return -1
#print(compara(2,100))

def inserta(x,lst,i):
  # Devuelve una lista resultado de insertar x en la posiciòn i
  return lst[:i]+[x]+lst[i:]

lista = [1,3,5,4,2]
lista_impar = [1,7,4,10,2,9,11,5,6,3,8]
lista_impar_2 = [3,2,1]
#print(inserta('y', lista, 4))

def inserta_multiple(x,lst):
  # Devuelve una lista con el resultado de insertar x en todas las posiciones de lst
  return [inserta(x,lst,i) for i in range(len(lst)+1)]

#print(inserta_multiple('x', lista))

def permuta(c):
  # Calcula y devuelve una lista de todas las permutaciones posibles que se pueden hacer con los 
  # elemntos   contenidos en c
  if len(c)==0:
    return [[]]
  return sum([inserta_multiple(c[0],i) for i in permuta(c[1:])],[])

#print(permuta(lista))
#print(len(permuta(lista)))

def sgn(p):
  # Cuenta el nùmero de inversiones en una permutaciòn a y calcula su  signo
  count=0;i=-1;a=[]
  for k in range(len(p)):
    a=a+[p[k]]
  while i<len(a)-2:
    i=i+1
    if a[i]>a[i+1]:
      aux=a[i];a[i]=a[i+1];a[i+1]=aux
      count=count+1
      i=-1
      continue
  if count%2==0:
    return "par"
  return "impar"

print(sgn(lista))
print(sgn(lista_impar_2))

def det(a):
  # Calcula el determinante de la matris a 
  n=len(a)
  s=range(n)
  t=permuta1(s)
  d=0
  for u in t:
    r=sgn(u)
    for i in range(n):
      r=r*a[i,u[i]]
    d=d+r
  return d

def permuta1(c):
  # Calcula y devuelve una lista de todas las permutaciones posibles que se pueden hacer con los 
  # elemntos   contenidos en c
  if len(c)==0:
    return [[]]
  lst=[]
  for i in permuta1(c[1:]):
    lst=lst+inserta_multiple(c[0],i)
  return lst

