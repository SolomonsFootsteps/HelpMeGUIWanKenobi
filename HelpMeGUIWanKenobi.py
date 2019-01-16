import tkinter as tk

# I'm not terrible at GUIs, but I'd like to be better

# I definitely AM terrible at decorators and I'd like to not be

def grid(num_rows, num_columns):
    def real_decorator(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            for rows in range(num_rows):
                return self.grid_rowconfigure(rows, weight=1)
            for cols in range(num_columns):
                return self.grid_columnconfigure(cols, weight=1)
            return result
        return wrapper
    return real_decorator

class TkRoot(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        main_window = MainWindow(parent=self)
        main_window.grid()

class MainWindow(tk.Frame):
    @grid(10, 10)
    def __init__(self, parent):
        tk.Frame.__init__(self, parent=None)
        self.parent = parent
        self.make_widgets()
    
    def make_widgets(self):
        for n in range(10):
            lbl = tk.Label(parent=self, text="wat")
            lbl.grid(row=lambda r=n: r, column=lambda c=n:c, sticky='')

if __name__ == '__main__':
    app = TkRoot()
    app.minsize(50, 50)
    app.mainloop()
