import tkinter as tk


# Create the window
root = tk.Tk()
# Change the name displayed on the top bar of the window
root.title('Greedy Snake')
# Decide the size and start position of the window
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
start_position_x = 200
start_position_y = 300
root.geometry('{}x{}+{}+{}'.format(
  width, height, start_position_x, start_position_y))
# Show this window
root.mainloop()
