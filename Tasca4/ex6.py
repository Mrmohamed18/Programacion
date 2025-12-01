# Autor: Mohamed El Moussaoui
# Fecha: 1/12/2025
# Descripció: una funció que demani una llista de números a l’usuari (separats per comes)

def main():
    def mitjana(llista_numeros):
        suma = 0
        for i in llista_numeros:
            suma += int(i)
        media = suma / len(llista_numeros)
        print(round(media, 2))
    def parell_imparells(llista_numeros):
        imparells = []
        parells = []
        for i in llista_numeros:
            numero = int(i)
            if numero % 2 == 0:
                parells.append(numero)
            else:
                imparells.append(numero)
        print("Numeros impares:", len(imparells))
        print("Numeros pares:", len(parells))
        
    entrada = input("Escribe una llista de numeros separats per comas: ")
    coma = entrada.split(",")

    print('Numero de elementos: ', len(coma))
    mitjana(coma)
    parell_imparells(coma)
if __name__ == "__main__":
    main()