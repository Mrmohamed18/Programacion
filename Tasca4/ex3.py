# Autor: Mohamed El Moussaoui
# Fecha: 1/12/2025
# Descripció:una funció que et pregunti el teu nom, i et demani un número. Si el número és 0, hauria de mostrar un missatge d’error. 
# En cas contrari, hauria de mostrar el nom repetit tants cops com indiqui el número.
def main():
    def mostrar_nombre(nombre, numero):
        if numero == 0:
            print("Error!!! El numero no puede ser 0.")
        else:
            if numero < 0:
                numero = abs(numero)
            for i in range(numero):
                if i == numero - 1:
                    print(nombre, end="")  
                else:
                    print(nombre, end=", ")
            print()
    nombre = input("Escribe nombre: ")
    numero = int(input("Escribe un numero: "))
    mostrar_nombre(nombre, numero)
if __name__ == "__main__":
    main()