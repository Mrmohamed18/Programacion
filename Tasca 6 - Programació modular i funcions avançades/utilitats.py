import os
import csv

def carregar_preguntes_txt(ruta):
    preguntes = []
    if not os.path.exists(ruta):
        pass
    
    try:
        with open(ruta, 'r', encoding='utf-8') as fitxer:
            for linia in fitxer:
                linia = linia.strip()
                if not linia: 
                    continue
                parts = linia.split(',')
                if len(parts) >= 2:
                    preguntes.append((parts[0], parts[1]))
    except:
        print("Error: No s'ha trobat el fitxer " + ruta + ".")
    return preguntes

def carregar_preguntes_csv(ruta):
    preguntes = []
    try:
        with open(ruta, "r", encoding="utf-8") as fitxer:
            lector = csv.reader(fitxer)
            capçalera = True
            for parts in lector:
                if not parts: 
                    continue
                if capçalera:
                    capçalera = False
                    continue
                if len(parts) >= 2:
                    preguntes.append((parts[0], parts[1]))
    except:
        print("Error!! No s'ha trobat el fitxer " + ruta + ".")
    return preguntes

# fa les preguntes i compta les correctes
def fer_preguntes(preguntes):
    punts = 0
    for pregunta, resposta_correcta in preguntes:
        print(pregunta)
        resposta = input("Resposta: ").strip()
        if resposta.lower() == resposta_correcta.lower():
            print("Correcte ")
            punts += 1
        else:
            print("Incorrecte La resposta era : " + resposta_correcta)
    return punts

# afegeix el ranking
def afegir_ranking(ruta, nom, punts):
    fitxer_existeix = os.path.exists(ruta)
    try:
        with open(ruta, "a", encoding="utf-8") as fitxer:
            if not fitxer_existeix:
                fitxer.write("nom, punts\n")
            fitxer.write(nom + "," + str(punts) + "\n")
    except:
        print("Error en desar el ranking.")

# llegeix el ranking
def llegir_ranking(ruta):
    ranking = []
    try:
        with open(ruta, "r", encoding="utf-8") as fitxer:
            capçalera = True
            for linia in fitxer:
                linia = linia.strip()
                if not linia:
                    continue
                if capçalera:
                    capçalera = False
                    continue
                parts = linia.split(",")
                if len(parts) >= 2:
                    nom = parts[0]
                    if parts[1].isdigit():
                        punts = int(parts[1])
                        ranking.append((nom, punts))
    except:
        print("Encara no hi ha cap ranking a " + ruta + ".")
    return ranking

def mostrar_ranking_ordenat(ranking):
    print("- RANKING -")
    if not ranking:
        print("Ranking està buit.")
        return
    
    def obtenir_punts(element):
        return element[1]
    
    ranking_ordenat = sorted(ranking, key=obtenir_punts, reverse=True)

    contador = 1
    for nom, punts in ranking_ordenat:
        print(str(contador) + " . " + nom + " - " + str(punts) + " punts")
        contador += 1
