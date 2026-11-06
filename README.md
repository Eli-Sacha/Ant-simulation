# Ant-simulation
The ant simulation, in python (using tkinter) with option for random start pattern, clearing the canvas, changing the amount of steps and the speed.

# Installation:

```bash
git clone https://github.com/Eli-Sacha/Ant-simulation.git
```

Just make sure you have python installed (they should already be installed along with python), with the following libraries:
  - tkinter
  - time
  - random

# How to use it:

```bash
python main.py #or whatever name you gave to your python executable / binary
```

The interface is divided into two parts: on the left is a canvas where the simulation takes place, and on the right are the controls and settings.

Controls (buttons):
  - Start simulation: Starts the simulation (the ant starts on the middle of the canva, looking right)
  - Stop simulation: Stops the simulation but doesn't clear
  - Reset simulation: Stops the simulation and clears the canvas
  - Generate random: Generates 100 random black tiles

Settings:
  - Amount of steps (range using buttons: 10 -> 10 000 000): Change the amount of steps 
  - Delay (range using buttons: 0 -> 1): Changes the delay between each step (default is 0: no delay)
  - Tile size (from 3 to 20): changes the size of the tile.
  - Performance mode: Toggles on/off the performance mode

When the ant reaches the border of the canva, it will teleport to the spawn (useful when the ant creates a highway). You can disable that feature by commenting lines 76, 77 and 78.

When you change the tile size, it reset the simulation (you can disable that feature by commenting line 110)
The same behaviour exists for random generation, you can disable it by commenting line 124.

If you ant a specific starting pattern, you can click on the canvas and it will flip the closest tile.

# What is the performance mode ?

Due to tkinter limitations (each black tile is stored in a list), the steps you do, the more the simulations slows down because there is too many black tiles. So each screen update takes more and more time to render. What performance mode does is that on passing a certain amount of steps, it will no longer update the screen on every steps and will only update every 1 000 then 10 000 steps. The simulation is a little bit faster but you don't see it live anymore.

I also advise you to increase the size of the tiles -> bigger tiles = less tiles on the screen = less lag = more performance.
