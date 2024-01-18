def lasit_treso_rindu(pārbaudes_darbs):
    try:
        with open(pārbaudes_darbs, 'r') as faila_objekts:
            rindas = faila_objekts.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2]
                print("Trešās rindas saturs:", tresa_rinda)
            else:
                print("Fails ir pārāk īss, lai būtu trešā rinda.")
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")
    except Exception as e:
        print("Kļūda:", e)

if __name__ == "__main__":
    
   pārbaudes_darbs = "piemers.txt"

   
   lasit_treso_rindu(pārbaudes_darbs)
