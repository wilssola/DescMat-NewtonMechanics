# newton_menu.py

import os

def menu_newton():
    while True:
        print("Selecione uma simulação de mecânica Newtoniana:")
        print("1. Sistema de Buraco Negro")
        print("2. Sistema Binário")
        print("3. Sistema Solar")
        print("4. Sistema Trinário")

        escolha = input("Digite o número da simulação desejada: ")

        if escolha == "1":
            os.system("python newton_black_hole_system.py")
        elif escolha == "2":
            os.system("python newton_binary_system.py")
        elif escolha == "3":
            os.system("python newton_solar_system.py")
        elif escolha == "4":
            os.system("python newton_trinary_system.py")
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    menu_newton()