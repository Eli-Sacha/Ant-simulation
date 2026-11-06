import tkinter as tk
import time
from random import randrange

screen = tk.Tk()
screen.title("Simulation")
WIDTH = 900
screen.geometry(f"{WIDTH+150}x{WIDTH+20}")

screen.grid_rowconfigure(0, weight=1)
screen.grid_columnconfigure(0, weight=1)

canvas = tk.Canvas(screen, background="white", width=WIDTH, height=WIDTH)
canvas.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

step_size: int = 3
p = False

def get_color_at(x, y):
	# Trouve les identifiants des objets qui recouvrent le point (x, y)
	ids = canvas.find_overlapping(x, y, x+step_size, y+step_size)
	if ids:
		# On prend le dernier élément (le plus au premier plan)
		color = canvas.itemcget(ids[-1], "fill")
		return color
	else:
		# S'il n'y a rien, on retourne la couleur de fond du canvas
		return canvas.cget("bg")

def flip_to_white(x, y):
	ids = canvas.find_overlapping(x, y, x+step_size, y+step_size)
	for id in ids:
		canvas.delete(id)

def flip_to_black(x, y):
	canvas.create_rectangle(x, y, x+step_size, y+step_size, fill="black", outline="")

def flip(x, y):
	color = get_color_at(x, y)
	if color == "white":
		flip_to_black(x, y)
		return -1
	flip_to_white(x, y)
	return 1

running: bool = False

def simulate():
	global running
	update_step_size()
	print("Starting simulation")
	d = float(delai.get())
	s = int(steps.get())

	i = 0

	x, y = canvas.winfo_width()//2, canvas.winfo_height()//2
	direction = 0

	running = True
	while i<s and running:
		direction += flip(x, y)

		match direction%4:
			case 0:
				x+=step_size
			case 1:
				y+=step_size
			case 2:
				x-=step_size
			case 3:
				y-=step_size

		if x<0 or y<0 or x>WIDTH or y>WIDTH:
			x, y = canvas.winfo_width()//2, canvas.winfo_height()//2
			direction=0

		i+=1

		if i%1000==0:
			d=float(delai.get())
			s=int(steps.get())

		if p:
			if i<50000 or (i<100000 and i%1000==0) or (i<300000 and i%10000==0):
				screen.update()
		else:
			screen.update()
		time.sleep(d)
	print("Simulation ended! reached step:", i, "out of", s)
	running = False

def stop_simulation():
	global running
	print("Stopping simulation!")
	running = False

def reset():
	stop_simulation()
	canvas.delete('all')
	print("Canvas reseted!")

def update_step_size():
	global step_size
	if not running:
		step_size = int(stepSizeSpinBox.get())

def on_canvas_click(event):
	if running:
		return
	x, y = event.x, event.y
	
	x, y = (x//step_size)*step_size, (y//step_size)*step_size

	flip(x, y)


def noise():
	reset()
	for i in range(100//step_size-2):
		x, y = randrange(0, WIDTH), randrange(0, WIDTH)
		x, y = (x//step_size)*step_size, (y//step_size)*step_size
		flip_to_black(x, y)

def update_performance():
	global p
	p = bool(performance.get())

controls = tk.Frame(screen, padx=10, pady=10)
controls.grid(row=0, column=1, sticky="ns")

tk.Button(controls, text="Start simulation", command=simulate).pack(fill="x", pady=(0, 8))
tk.Button(controls, text="Stop simulation", command=stop_simulation).pack(fill="x", pady=(0, 8))
tk.Button(controls, text="Reset simulation", command=reset).pack(fill="x", pady=(0, 8))
tk.Button(controls, text="Generate random", command=noise).pack(fill="x", pady=(0, 8))

tk.Label(controls, text="Amount of steps").pack(anchor="w")
steps = tk.Spinbox(controls, from_=10, to=10_000_000)
steps.pack(fill="x", pady=(0, 12))

tk.Label(controls, text="Delay").pack(anchor="w")
delai = tk.Spinbox(controls, from_=0, to=1, increment=0.001, format="%.3f")
delai.pack(fill="x", pady=(0, 12))

tk.Label(controls, text="Tile size").pack(anchor="w")
stepSizeSpinBox = tk.Spinbox(controls, from_=3, to=20, increment=1, command=update_step_size)
stepSizeSpinBox.pack(fill="x", pady=(0, 12))

performance = tk.IntVar()
tk.Checkbutton(controls, text="Performance mode", variable=performance, command=update_performance).pack(fill="x", pady=(0, 12))

canvas.bind("<Button-1>", on_canvas_click)

screen.mainloop()
