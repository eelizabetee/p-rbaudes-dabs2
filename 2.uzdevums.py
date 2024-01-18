import csv

def lasit_csv_otra_kolonna(pārbaudes_darbs):
    try:
        with open(pārbaudes_darbs, 'r') as csv_fails:
            csvlasitajs = csv.reader(csv_fails)
            for rinda in csvlasitajs:
                if len(rinda) > 1:  
                    print("Otrās kolonnas dati:", rinda[1])
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")
    except Exception as e:
        print("Kļūda:", e)

if __name__ == "__main__":
    
    pārbaudes_darb = "piemers.csv"

    lasit_csv_otra_kolonna(pārbaudes_darb)
