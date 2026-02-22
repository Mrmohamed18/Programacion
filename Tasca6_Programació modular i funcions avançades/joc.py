import utilitats
import estadistiques
import os

def actualitzar_estadistiques_partida(nom, punts, total_preguntes): 
    ruta_jugadors = "data/jugadors.csv"
    jugadors = []
    jugador_trobat = False


    if os.path.exists(ruta_jugadors):
        try:
            with open(ruta_jugadors, "r", encoding="utf-8") as f:
                for linia in f:
                    linia = linia.strip()
                    if not linia: 
                        continue

                    parts = linia.split(',')
                    if len(parts) >= 4:
                        nom_j = parts[0]
                        if parts[1] == "partides":
                            jugadors.append(linia)
                            continue
                        
                        # comprovem si son digits amb isdigit
                        if parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
                            partides = int(parts[1])
                            victories = int(parts[2])
                            derrotes = int(parts[3])

                            if nom_j == nom:
                                jugador_trobat = True
                                partides += 1
                                victories += punts
                                derrotes += (total_preguntes - punts)
                            jugadors.append(nom_j + "," + str(partides) + "," + str(victories) + "," + str(derrotes))
        except:
            print("Error llegint " + ruta_jugadors)

    if not jugador_trobat:
        derrotes = total_preguntes - punts
        jugadors.append(nom + ",1," + str(punts) + "," + str(derrotes))

    try:
        with open(ruta_jugadors, 'w', encoding='utf-8') as f:
            for j in jugadors:
                f.write(j + '\n')
    except:
        print("Error escrivint a " + ruta_jugadors)


def main():
    print("Benvingut al Joc de Preguntes i Puntuacions")
    nom = input("Introdueix el teu nom : ").strip()
    
    # comprovem si el nom esta buit
    if not nom:
        nom = "buit"

    print("Selecciona el nivel de la dificultat:")
    print("1. facil")
    print("2. mitjana")
    print("3. dificil")
    
    dificultat = input("Opcio (1/2/3): ").strip()

    ruta = ""
    es_csv = False

    if dificultat == "1" or dificultat.lower() == "facil":
        ruta = "data/preguntes_facil.txt"

    elif dificultat == "2" or dificultat.lower() == "mitjana":
        ruta = "data/preguntes_mitja.txt"

    elif dificultat == "3" or dificultat.lower() == "dificil":
        ruta = "data/preguntes_dificil.csv"
        es_csv = True
    else:
        print("Opcio no valida si va poner la dificultat facil per defecte.")
        ruta = "data/preguntes_facil.txt"

    print("\nCarregant preguntes...")
    if es_csv:
        preguntes = utilitats.carregar_preguntes_csv(ruta)
    else:
        preguntes = utilitats.carregar_preguntes_txt(ruta)

    if not preguntes:
        print("No s'han pogut carregar les preguntes.")
        return

    # guarda els punts i el total de preguntes
    punts = utilitats.fer_preguntes(preguntes)
    total_preguntes = len(preguntes)

    print("Partida acabada Has aconseguit " + str(punts) + " punt(s) de " + str(total_preguntes) + " possibles.")

    # desa el resultat al ranking
    ranking_path = "data/ranking.csv"
    utilitats.afegir_ranking(ranking_path, nom, punts)

    # mostra el ranking ordenat
    ranking = utilitats.llegir_ranking(ranking_path)
    utilitats.mostrar_ranking_ordenat(ranking)

    # actualitza estadistiques del jugador a CSV
    actualitzar_estadistiques_partida(nom, punts, total_preguntes)

    estadistiques.generar_estadisticas_txt()

if __name__ == "__main__":
    main()
