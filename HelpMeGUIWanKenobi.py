import tkinter as tk

# I'm not terrible at GUIs, but I'd like to be better

# I definitely AM terrible at decorators and I'd like to not be

# @grid() is almost working, but not quite
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
        SecondWindow(parent=self)
        ThirdWindow(parent=self)
        

# this test case makes it seem like @grid(10,10) works, but it really doesn't

class MainWindow(tk.Frame):
    @grid(10, 10)
    def __init__(self, parent):
        tk.Frame.__init__(self, parent=None)
        self.parent = parent
        parent.title("First")
        self.make_widgets()
    
    def make_widgets(self):
        for n in range(10):
            lbl = tk.Label(self, text="wat")
            lbl.grid(row=n, column=n, sticky='')

# this version will give the exact same result as the above
class SecondWindow(tk.Toplevel):
    @grid(2000, 10)
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent=None)
        self.parent = parent
        self.title("Second")
        self.make_widgets()
    
    def make_widgets(self):
        for n in range(10):
            lbl = tk.Label(self, text="wat")
            lbl.grid(row=n, column=n, sticky='') 

# this version will ALSO give the same result
class ThirdWindow(tk.Toplevel):
    @grid(2, 2)
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent=None)
        self.parent = parent
        self.title("Third")
        self.make_widgets()
    
    def make_widgets(self):
        for n in range(10):
            lbl = tk.Label(self, text="wat")
            lbl.grid(row=n, column=n, sticky='') 


if __name__ == '__main__':
    app = TkRoot()
    app.minsize(50, 50)
    app.mainloop()
