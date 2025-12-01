# Autor: Mohamed El Moussaoui
# Fecha: 1/12/2025
# Descripció:una funció que donada una llista, et digui quants números coincideixen amb la seva posició
def main():
    def comprabador(x):
        posicions = []
        for i, valor in enumerate(x):
            if i == valor:
                posicions.append(i)
        return posicions
    llista = [1, 8, 2, 5, 4, 3, 8]
    posicio = comprabador(llista)
    print('Coinciden: ', len(posicio))
    print('Pocisiones que coinciden: ', posicio)  
if __name__ == "__main__":
    main()