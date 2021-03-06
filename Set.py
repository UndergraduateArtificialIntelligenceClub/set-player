# Code Written by Justin Stevens, March 5th, 2021
# Implementation of GUI sourced from https://realpython.com/pysimplegui-python/
# To-do: Real time implementation so it gets the cards from the screen
# To-do: Better GUI visualization of the grid
# To-do: Add a hint button such that it can give one card in the solution
# To-do: Visualize solution instead of showing it as an array 

import tkinter as tk

from math import floor
window = tk.Tk()

grid=[["green", "green", "blue"], ["red", "blue", "green"], ["blue", "green", "red"], ["red", "blue", "blue"]]
shapes=[["d", "d", "o" ], ["s", "s", "o"], ["d", "s", "s"], ["o", "o", "o"]]
numbers=[[3, 1, 2], [3, 1, 3], [1, 1, 2], [1, 3, 1]]
fill=[["e", "f", "s"], ["e", "e", "s"], ["f", "s", "e"], ["s", "f", "e"]]


def check_set():

    answers=[]
    for i in range(12):
        rowi=floor(i/3)
        coli=i%3
        for j in range(i+1, 12):
            rowj=floor(j/3)
            colj=j%3
            for k in range(j+1, 12):
                #print(i,j,k)
                # For all possible permutations
                rowk=floor(k/3)
                colk=k%3
                if((grid[rowi][coli]==grid[rowj][colj]==grid[rowk][colk]) or \
                grid[rowi][coli]!=grid[rowj][colj] and grid[rowi][coli]!=grid[rowk][colk] and grid[rowj][colj]!=grid[rowk][colk]):
                    #print("good")
                    pass
                else:
                    continue
                if((shapes[rowi][coli]==shapes[rowj][colj] and shapes[rowi][coli]==shapes[rowk][colk]) or \
                shapes[rowi][coli]!=shapes[rowj][colj] and shapes[rowi][coli]!=shapes[rowk][colk] and shapes[rowj][colj]!=shapes[rowk][colk]):
                    #print("good")
                    pass
                else:
                    continue

                if((numbers[rowi][coli]==numbers[rowj][colj] and numbers[rowi][coli]==numbers[rowk][colk]) or \
                numbers[rowi][coli]!=numbers[rowj][colj] and numbers[rowi][coli]!=numbers[rowk][colk] and numbers[rowj][colj]!=numbers[rowk][colk]):
                    #print("good")
                    pass
                else:
                    continue

                if((fill[rowi][coli]==fill[rowj][colj] and fill[rowi][coli]==fill[rowk][colk]) or \
                fill[rowi][coli]!=fill[rowj][colj] and fill[rowi][coli]!=fill[rowk][colk] and fill[rowj][colj]!=fill[rowk][colk]):
                    #print("good")
                    pass
                else:
                    continue
                answers.append([i,j,k])
                #print(i,j,k)
    return answers

answers=check_set()
print(answers)

for i in range(4):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=4
        )
        frame.grid(row=i, column=j)
        if(fill[i][j]=="s"):
            shade="sunken"
        elif(fill[i][j]=="f"):
            shade="raised"
        else:
            shade="flat"
        label = tk.Label(master=frame, text=f"Shape {shapes[i][j]}\nNumber {numbers[i][j]}\n Fill {fill[i][j]}", bg=grid[i][j], borderwidth=2, relief=shade)
        label.pack()

window.mainloop()
