class Tablero:

    def __init__(self):

        self.celdas = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]

    def dibuja(self, jugadores):

        def sustituye(celdas, jugadores):
            casillas = []
            casillaActual = 1
            for celda in self.celdas:
                if celda == -1:
                    casillas.append(jugadores[0].token)
                elif celda == 1:
                    casillas.append(jugadores[1].token)
                else:
                    casillas.append(str(casillaActual))
                casillaActual += 1

            return casillas

        c = sustituye(self.celdas, jugadores)
        print(f"""
        _______________________
        |       |       |       |
        |   {c[6]}   |   {c[7]}   |   {c[8]}   |
        |_______|_______|_______|
        |       |       |       |
        |   {c[3]}   |   {c[4]}   |   {c[5]}   |
        |_______|_______|_______|
        |       |       |       |
        |   {c[0]}   |   {c[1]}   |   {c[2]}   |
        |_______|_______|_______|""")

    def quedanCeldasLibres(self):
        return 0 in self.celdas

    def estaDisponibleLaCelda(self, celda):
        return self.celdas[celda] == 0

    def introduce(self, jugador, casillaElegida):
        self.celdas[casillaElegida] = jugador.valor

    def hayJugadaGanadora(self):
        lineas = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for pos in lineas:
            c = self.celdas
            suma = c[pos[0]] + c[pos[1]] + c[pos[2]]
            if suma == 3 or suma == -3:
                return True

        return False