from colorhelper import rojo, azul


class Jugador:
    def __init__(self, token, valor):
        self._token = token
        self.valor = valor
        self.color = rojo if self.valor == 1 else azul

    def get_token(self):
        return self.color(self._token)

    def set_token(self, token):
        self._token = token

    def del_token(self):
        del self._token

    token = property(get_token, set_token, del_token)

    def elige(self, tablero):

        def humanToMachine(casillaElegida):
            return int(casillaElegida) - 1

        def validarEntrada(tablero, casillaElegida):
            if not casillaElegida.isdigit():
                print("    Eso no parece una jugada válida")
                return False

            celdaElegida = humanToMachine(casillaElegida)
            if celdaElegida not in range(0, 9):
                print("    Eso parece estar fuera del tablero")
                return False

            if not tablero.estaDisponibleLaCelda(celdaElegida):
                print("    Esa casilla ya está ocupada")
                return False

            return True

        def solicitaJugada():

            return input(f"\n    jugador [ {self.token} ] elige pos: ")

        casillaElegida = solicitaJugada()
        while not validarEntrada(tablero, casillaElegida):
            casillaElegida = solicitaJugada()

        celdaElegida = humanToMachine(casillaElegida)

        tablero.introduce(self, celdaElegida)
