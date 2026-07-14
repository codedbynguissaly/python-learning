nom = input("Quel est ton nom ?")
note = int(input("Quelle est ta note ?"))
if note >= 10:
    print("Félicitation" , nom , "!")
    print("Tu as obtenu", str(note) + "/20")
    print("Tu es admis !")
else:
    print("Courage" , nom , "!")
    print("Tu n'es pas admis cette fois-ci .")