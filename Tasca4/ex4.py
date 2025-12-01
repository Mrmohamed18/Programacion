# Autor: Mohamed El Moussaoui
# Fecha: 1/12/2025
# Descripció:una funció que donada una llista qualsevol, et digui si és simètrica o no. Si ho és, que et digui quants elements té.
def main():
    def es_simetrica(lista):
        return lista == lista[::-1]
    def lista_invertida(lista):
        return lista[::-1]
    lista_simetrica = [4, 5, 6, 5, 4]
    llista = es_simetrica(lista_simetrica)
    n = lista_invertida(lista_simetrica)
    if llista == True:
        print('La llista es simetrica.')
        print('La llista tiene', len(lista_simetrica), 'elementos.')
    else:
        print('La llista no es simetrica.')
    print('Llista invertida:', n)
if __name__ == "__main__":
    main()