#!/usr/bin/python3

import sys
import os

from juego import Juego

if __name__ == "__main__":

    juego = Juego()
    try:
        juego.juega()
    except KeyboardInterrupt:
        
        print("\n    (proceso interrumpido por el usuario)")

        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
