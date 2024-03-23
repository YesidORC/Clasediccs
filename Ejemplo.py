# import json

# h = []

# class Perro():
#     def __init__(self):
#         self.raza = ""
#         self.edad = 0
#         self.nombre = ""
        
#     def ladrar(self,t):
#         print(f"{self.nombre} ladra {t} veces")
        
# def main():           
#     while True:
#         m = input("")
#         if m == "1":
#             x= input("ingrese cedula: ")
#             p = Perro()
#             p.nombre = input("Ingrese nombre del perro")
#             p.raza = input("Ingrese raza: ")
#             p.edad = int(input("Ingrese edad: "))
#             h.append(p)
        
#         elif m == "2":
#             print(h[0]==h[1])
#         else:
#             break
        
    
# if __name__ == '__main__':
#     main()

print("Modulo Ejemplo __name__ is set to: {}" .format(__name__))

def function_three():
       print("Function three is executed")
       
def function_four():
       print("Function four is executed")

if __name__ == "__main__":
    print("\nModuloa Ejemplo ejecutado cuando corre directametne\n")
else:
    print("\nModulo Ejemplo ejecutado cuando es importado\n")