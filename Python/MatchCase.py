pet = input("Voce tem um pet?")
pet = pet.lower()

match(pet):
    case "cachorro":
        print("Voce tem um cachorro")
    case "gato":
        print("Voce tem um gato")
    case "passaro":
        print("Voce tem um passaro")
    
    #anycase para outros casos
    case _:
        print("Voce nao tem um pet")