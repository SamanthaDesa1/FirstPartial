def suma(a,b):
  x = a + b
  return x

def resta(a,b):
  x = a - b
  return x

print("Tell me a number...")
a = int(input())
print("Now tell me another number...")
b = int(input())
print("the addition of those two numbers is", suma(a,b))
print("and the substraction is",resta(a,b))
def conversion(k):
 x = k*1000
 return x

print("How many kilometers have you passed?")
k = int(input())
print("You have passed",conversion(k),"meters.")


def triangle_area(b,h):
  x = b*h/2
  return x

print("WHat is the base of the traingle?")
b = int(input())
print("How tall is the triangle?")
h = int(input())
print("The area of the traingle is",triangle_area(b,h))
