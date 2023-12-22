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

def cazzo_draw(length:int):
    print(cazzo_base,end="")
    for _ in range(length):
        print(cazzo_extender)
    print(cazzo_top)


def cazzo_loop(min_len:int, max_len:int, millis:int):
    while True:
        for i in range(min_len, max_len):
            cazzo_draw(i)
            sleep(millis/1000)
            os.system('clear')

        for i in range(max_len -1 , min_len + 1, -1):
            cazzo_draw(i)
            sleep(millis/1000)
            os.system('clear')

if __name__=="__main__":
    if len(argv) < 2:
        print("vaffanculo")
        exit(1)
    if len(argv) == 2:
        cazzo_draw(int(argv[1]))
        exit(0)
    if len(argv) == 3:
        cazzo_loop(int(argv[1]), int(argv[2]), 50)
    if len(argv) == 4:
        cazzo_loop(int(argv[1]), int(argv[2]), int(argv[3]))

