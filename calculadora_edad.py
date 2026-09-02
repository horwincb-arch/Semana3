from colorama import Fore, Style
while True:
    try:
        edad = int(input("Edad: "))
        print("Edad registrada: ", edad)
        break
    except ValueError:
        print(Fore.RED + "Ingrese un valor númerico: ")
        print(Style.RESET_ALL)
print(Fore.GREEN + "Edad registrda: ", edad)