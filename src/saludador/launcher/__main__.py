import sys
import saludador.modules.examples.saludador as saludador
import saludador.launcher.__version__ as __version__

from termcolor import colored

def main():
    print("[", colored(f"Iniciando app de pruebas, ver:({__version__})", "green"), "]") 
    saludador.saluda_a("jaime") 

if __name__ == "__main__":
    sys.exit(main())
