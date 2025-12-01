# Autor: Mohamed El Moussaoui
# Fecha: 1/12/2025
# Descripció:una funció que et pregunti dos números. T’ha de mostrar un missatge dient si el primer és més gran, el segon és més gran o són iguals.
def main():
    def clasificado_numeros(numero1, numero2):
        if numero1 > numero2:
            print('Numero 1 es mayor')
        elif numero2 > numero1:
            print('Numero 2 es mayor')
        else:
            print('iguales')
    try:
        numero1 = int(input('Escribe el primer numero: '))
        numero2 = int(input('Escribe el segundo numero: '))
        print('Clasificacio: ')
        clasificado_numeros(numero1, numero2)
    except ValueError:
        print('Error!!!! Has escrito letras o caracteres. ')
if __name__ == "__main__":
    main()