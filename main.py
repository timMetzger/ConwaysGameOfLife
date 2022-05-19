#By: Timothy Metzger

import p5
from Box import Box

HEIGHT = 1000
WIDTH = 1000

boxs = []
SIZE = 50


def setup():
    p5.size(WIDTH,HEIGHT)
    p5.title("Conway's Game of Life")

    for x in range(0,1000,SIZE):
        row = []
        for y in range(0,1000,SIZE):
            row.append(Box(x,y,SIZE))

        boxs.append(row)



def draw():

    p5.background(0)

    alive = []
    dead = []
    for i in range(len(boxs)):
        for j in range(len(boxs[0])):
            alive_count = get_alive_count(i,j)
            if boxs[i][j].isalive():
                if alive_count > 3 or alive_count < 2:
                    dead.append((i,j))
            else:
                if alive_count == 3:
                    alive.append((i,j))

    for i,j in alive:
        boxs[i][j].invigorate()
    for i,j in dead:
        boxs[i][j].kill()

    for i in range(len(boxs)):
        for j in range(len(boxs[0])):
            boxs[i][j].display()




def get_alive_count(x,y):
    count = 0
    combos = [(x+1,y),(x-1,y),(x,y-1),(x,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]
    for combo in combos:
        i,j = combo
        if(0 <= i < len(boxs) and 0 <= j < len(boxs[0])):
            if boxs[i][j].isalive():
                count += 1


    return count

if __name__ == "__main__":
    p5.run()