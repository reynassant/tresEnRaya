#!/usr/bin/python3

import os
from re import I

from tablero import Tablero
from jugador import Jugador


class Juego:
    token = ['X', 'O']

    def __init__(self):
        os.system("color")
        self.jugadores = [
            Jugador(self.token[0], -1),
            Jugador(self.token[1], 1)
        ]

    def __del__(self):
        print('\n\n    Gracias por jugar.')

    def reset(self):
        self.turno = 0
        self.tablero = Tablero()

    def continuePlaying(self):
        acceptance = ['y', 's']
        denial = ['n']

        while True:
            qr = input('\n    Quieres volver a jugar?\n    ')
            if qr == '' or not qr[0].lower() in acceptance + denial:
                print('\n    Por favor, contesta [S]i o [N]o (yes/no)!')
            else:
                break

        return True if qr[0].lower() in acceptance else False

    def juega(self):
        playAgain = True
        while playAgain:
            self.reset()
            while self.tablero.quedanCeldasLibres():
                self.tablero.dibuja(self.jugadores)
                jugador = self.jugadores[self.turno % 2] \
                .elige(self.tablero)

                self.turno += 1

                if self.tablero.hayJugadaGanadora():
                    print(f"\n    Felicidades jugador [ {jugador} ]! Has ganado")
                    break

            if not self.tablero.hayJugadaGanadora():
                print("\n    EMPATE: Habéis llegado al final sin que gane nadie.")
            
            if not self.continuePlaying():
                break
            
            print("\n    Gracias por volver a jugar, está claro que te estás divirtiendo")
        