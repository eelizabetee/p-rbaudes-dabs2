def lasit_failu(pārbaudes_darbs):
    try:
        with open(pārbaudes_darbs,"r" ) as faila_objekts:
            saturs = faila_objekts.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print("Norādītais fails nav atrasts. ")
    except Exception as e:
        print("Kļūda",e)

    if __name__ == "__main__":
      pārbaudes_darbs = "piemers.txt"
    lasit_failu(pārbaudes_darbs)          