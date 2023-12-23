from sys import argv, exit
from time import sleep
import os

"""
disegna un cazzo sul terminale
"""

cazzo_base:str= """  +------+   +------+
 /         V         \\
|          |          |       
|          |          |       
|          |          |       
 \\                   /
  +--      +      --+
"""
cazzo_extender:str="   |               |"

cazzo_top:str = """   +--           --+
  /                 \\
  |                 |
  \\                 /
   \\       |       /
    +------|------+
"""

def sleep_millis(millis:int):
    """
    sleep for time specified in milliseconds

    @param millis the milliseconds to sleep for
    """

    sleep(millis/1000)

def clear_terminal():
    """
    clears terminal
    """

    os.system('cls' if os.name == 'nt' else 'clear')

def cazzo_draw(length:int):
    """
    disenga un cazzo lungo `length` sul terminale

    @param length la lunghezza del cazzo
    """

    print(cazzo_base,end="")
    for _ in range(length):
        print(cazzo_extender)
    print(cazzo_top)


def cazzo_loop(min_len:int, max_len:int, millis:int):
    """
    disenga un cazzo di lunghezza tempo-variabile tra `min_len` e `max_len`
    sul terminale

    @param min_len la lunghezza del cazzo
    @param max_len la lunghezza del cazzo
    @param millis periodio di transizione tra lunghezze, in millisecondi

    @see cazzo_draw
    """
    while True:
        def cazzo_loop_iteration(l:int):
            cazzo_draw(l)
            sleep_millis(millis)
            clear_terminal()
            
        for i in range(min_len, max_len):
            cazzo_loop_iteration(i)

        for i in range(max_len -1 , min_len + 1, -1):
            cazzo_loop_iteration(i)

if __name__=="__main__":
    if len(argv) < 2:
        print("cazzo.py richiede almeno un parametro(intero) da command line")
        exit(1)
    if len(argv) == 2:
        cazzo_draw(int(argv[1]))
        exit(0)
    if len(argv) == 3:
        cazzo_loop(int(argv[1]), int(argv[2]), 50)
    if len(argv) == 4:
        cazzo_loop(int(argv[1]), int(argv[2]), int(argv[3]))
    if len(argv) > 4:
        print("cazzo.py richiede meno di 4 parametri(interi), 4 o più non vale")
        exit(1)

