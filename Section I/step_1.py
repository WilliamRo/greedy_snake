"""
If you want to create a game based on whatever programming language, you must
decide where to show your user interface. It can be on terminal (sometimes
people call it 'command line window' or 'command shell') of course, yet a
window on which we can draw whatever shape with whatever color is definitely
more preferable. Here we go with a build-in package named 'tkinter' to create
such a window.
"""
import tkinter as tk


# This line create a tk root which is ready to be showed
root = tk.Tk()
# This line let the root show itself
root.mainloop()

"""
Now that you have created and showed a window using tk, it's time to change its
styles such as its size, start position and background color.
"""