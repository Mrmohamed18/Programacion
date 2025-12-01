# Autor: Mohamed El Moussaoui
# Fecha: 1/12/2025
# Descripció:una funció que et classifiqui una variable numèrica en funció de l’escala Suspès/Aprovat/Notable/Exceŀlent.
def main():
    def clasificador(nota):
        if nota >= 5:
            print('Aprovat')
            return nota
        elif nota >= 7:
            print('Notable')
            return nota
        if nota >= 9:
            print('Exceŀlent')
            return nota
        else:
            print('Suspes')

    numero = float(input('Escribe la nota: '))
    print('Clasificacio: ')
    clasificador(numero)
if __name__ == "__main__":
    main()