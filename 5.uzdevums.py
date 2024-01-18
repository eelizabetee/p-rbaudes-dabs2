def ierakstit_faila(lietotaja_vards):
    try:
       
        with open("lietotajs.txt", 'w') as faila_objekts:
            faila_objekts.write(lietotaja_vards)
        print("Vārds veiksmīgi ierakstīts failā lietotajs.txt.")
    except IOError:
        print("Kļūda: Nevarēja atvērt vai izveidot failu.")
    except Exception as e:
        print("Kļūda:", e)

if __name__ == "__main__":
    try:
   
        lietotaja_vards = input("Ievadiet savu vārdu: ")

        ierakstit_faila(lietotaja_vards)
    except Exception as e:
        print("Nezināma kļūda:", e)
