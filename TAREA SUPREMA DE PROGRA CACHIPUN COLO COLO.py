import random
a = 0
e = 0


def JUEGARDO():
    print("introduzca su nombre:")
    player_juan = str(input())
    print('Quieres darle un nombre al Enemigo?')
    print('"si" o "no"')
    querionoqueri = input()
    if querionoqueri == 'si':
        print('Que nombre quieres otorgarle a tu rival?')
        pprr = 0
        while pprr == 0:
            player_IA = str(input())
            if player_IA == 'Mija':
                print('imposible, Mija no es un Enemigo, PORFAVOR PUEDES PONERNOS EL 7?????')
            elif player_IA != 'Mija':
                pprr = 1

    elif querionoqueri == 'no':
        player_IA = "Universidad de Chile"

    else:
        print('LLANOMA TU ENEMIGO VA A SER EL RENEPUENTE')
        player_IA = 'Rene Puente El FIXA FUMADOR DE CRIPY ABITUAL LLANOMA'


    print("bienvenido a Cachipun COLO-COLO")
    print('EL DUELO DE HOY SERA')
    print('')
    print(player_IA,'VS',player_juan)
    q = 0
    Piedra = 1
    Papel = 2
    Tijera = 3
    contador_jugador = 0
    contador_bot = 0

    while (contador_jugador < 3) and (contador_bot < 3):
        print('Que jugaras?,"Piedra","Papel" o "Tijera"?')
        def Piedra(x):
            print(str(x), '''
            ##    _______
            ##---'   ____)
            ##      (_____)
            ##      (_____)
            ##      (____)
            ##---.__(___)
            ##''')

        def Papel(x):
            print(str(x), '''
            ##    _______
            ##---'   ____)____
            ##          ______)
            ##          _______)
            ##         _______)
            ##---.__________)
            ##''')

        def Tijera(x):
            print(str(x), '''
            ##    _______
            ##---'   ____)____
            ##          ______)
            ##       __________)
            ##      (____)
            ##---.__(___)
            ##''')

        while q == 0:
            nro_playerjuan = str(input()).lower()
            if nro_playerjuan == 'piedra':
                nro_playerjuan = 1
                q = 1
            elif nro_playerjuan == 'papel':
                nro_playerjuan = 2
                q = 1
            elif nro_playerjuan == 'tijera':
                nro_playerjuan = 3
                q = 1
            else:
                print('Debe ingresar una de las siguientes opciones: "Piedra","Papel" o "Tijera"')

        nro_playeria = random.randint(1, 3)

        # Jugadas del Jugador
        if nro_playerjuan == 1:
            Piedra(player_juan)
        elif nro_playerjuan == 2:
            Papel(player_juan)
        elif nro_playerjuan == 3:
            Tijera(player_juan)

        # Jugadas del Bot

        if nro_playeria == 1:
            Piedra(player_IA)
        elif nro_playeria == 2:
            Papel(player_IA)
        elif nro_playeria == 3:
            Tijera(player_IA)

        if (nro_playerjuan == 1) and (nro_playeria == 1):
            print('Empate,ambos Jugadores eligieron Piedra')
            q = 0
        elif (nro_playerjuan == 1) and (nro_playeria == 2):
            print('El ganador es', player_IA)
            contador_bot += 1
            q = 0
        elif (nro_playerjuan == 1) and (nro_playeria == 3):
            print('El ganador es', player_juan)
            contador_jugador += 1
            q = 0
        elif (nro_playerjuan == 2) and (nro_playeria == 1):
            print('El ganador es', player_juan)
            contador_jugador += 1
            q = 0
        elif (nro_playerjuan == 2) and (nro_playeria == 2):
            print('Empate,ambos Jugadores eligieron Papel')
            q = 0
        elif (nro_playerjuan == 2) and (nro_playeria == 3):
            print('El ganador es', player_IA)
            contador_bot += 1
            q = 0
        elif (nro_playerjuan == 3) and (nro_playeria == 1):
            print('El ganador es', player_IA)
            contador_bot += 1
            q = 0
        elif (nro_playerjuan == 3) and (nro_playeria == 2):
            print('El ganador es', player_juan)
            contador_jugador += 1
            q = 0
        elif (nro_playerjuan == 3) and (nro_playeria == 3):
            print('Empate,ambos jugadores eligieron Tijera')
            q = 0
        print(player_juan + ':', str(contador_jugador), player_IA + ':', str(contador_bot))
    if contador_jugador == 3:
        print('')
        print('VICTORY ROYALE')
        print('')
        print('El ganador de la Copa COLO-COLO es', player_juan)
        print('')
        print('*Suena de fondo https://youtu.be/Sm0TeXjvNJg?t=25')
    elif contador_bot == 3:
        print('')
        print("CHILE CAMPEON'T")
        print('')
        print('El ganador de la Copa COLO-COLO es', player_IA)
        print('')
        print('*Suena de fondo https://www.youtube.com/watch?v=wdGbR5pOeW8')
    return 1

print('Bienvenido a Cachipun COLO-COLO')
while a == 0:

    print('')
    if e == 0:
        print('Quieres jugar?')
    print('Escribe "si" para continuar')
    print('')
    print('Escribe "no" para salir')
    decision = input()

    if decision == 'si':
        e = JUEGARDO()
        if e == 1:
            print('Quieres volver a jugar?')

    elif decision == 'no':
        print('Colo-Colo lo mas grande, my final message. GOODBYE.')
        a = 1
    elif decision == (('colocolo')):
        print('Sabemos que Colo-Colo es lo mas grande, sin embargo, no nos sirve para continuar el programa.')
    elif decision == 'U':
        print('Chuncho weco')
    elif decision == 'Mija':
        print('Ponme el 7, We love Mija, We believe in that Religion')
    else:
        print('Esta opcion no es valida')

#Escribe "colocolo" en el primer input, Mija we love u
#Tambien puedes probrar con escribir "Mija"
#Python no nos dejo poner como opciones nuestras queriadas y variadas maneras de escribir colo colo, por ejemplo: (('colo colo') or ('Colo Colo') or ('colocolo') or ('ColoColo') or ('Colo-Colo') or ('COLO-COLO') or ('COLOCOLO') or ('Colocolo') or ('coloColo') or ('ColoCOLO') or ('COLOcolo'))