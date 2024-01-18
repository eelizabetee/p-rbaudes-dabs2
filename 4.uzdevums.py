def lasit_failu(pārbaudes_darbs):
    try:
        with open(pārbaudes_darbs, 'r') as faila_objekts:
            saturs = faila_objekts.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")
    except Exception as e:
        print("Kļūda:", e)

if __name__ == "__main__":
    try:
        pārbaudes_darbs = input("Ievadiet faila nosaukumu: ")
        faila_formats = input("Ievadiet faila formātu (paplašinājumu): ")

   
        if '.' not in faila_formats:
            raise ValueError("Nepareizs faila formāts. Ievadiet paplašinājumu, piemēram, 'txt'.")

        
        if '.' not in pārbaudes_darbs:
            raise ValueError("Nepareizs faila nosaukums. Ievadiet faila nosaukumu ar paplašinājumu.")

        _, ievadits_formats = faila_formats.rsplit('.', 1)

        if ievadits_formats != pārbaudes_darbs.split('.')[-1]:
            raise ValueError("Ievadītais formāts nesakrīt ar faila paplašinājumu.")

        lasit_failu(pārbaudes_darbs)
    except ValueError as ve:
        print("Kļūda:", ve)
    except Exception as e:
        print("Nezināma kļūda:", e)
