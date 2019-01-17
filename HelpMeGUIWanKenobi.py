import tkinter as tk

# I'm not terrible at GUIs, but I'd like to be better

# I definitely AM terrible at decorators and I'd like to not be

# @grid() is finally working!
def grid(num_rows, num_columns, row_min=5, col_min=5):
    def real_decorator(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            for rows in range(num_rows):
                self.grid_rowconfigure(rows,minsize=row_min,weight=1)
                print("row "+str(rows)+" configured")
            for cols in range(num_columns):
                self.grid_columnconfigure(cols,minsize=col_min,weight=1)
                print("column "+str(cols)+" configured")
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
        
class MainWindow(tk.Frame):
    @grid(10, 10, row_min=15, col_min=3)
    def __init__(self, parent):
        tk.Frame.__init__(self, parent=None)
        self.parent = parent
        parent.title("First")
        self.make_widgets()
    
    def make_widgets(self):
        for n in range(10):
            lbl = tk.Label(self, text="wat")
            lbl.grid(row=(2*n), column=n, sticky='')

class SecondWindow(tk.Toplevel):
    @grid(100, 10, row_min=2, col_min=12)
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent=None)
        self.parent = parent
        self.title("Second")
        self.make_widgets()
    
    def make_widgets(self):
        for n in range(10):
            lbl = tk.Label(self, text="wat")
            lbl.grid(row=(2*n), column=n, sticky='') 

class ThirdWindow(tk.Toplevel):
    @grid(2, 2, row_min=2, col_min=120)
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent=None)
        self.parent = parent
        self.title("Third")
        self.make_widgets()
    
    def make_widgets(self):
        for n in range(10):
            lbl = tk.Label(self, text="wat")
            lbl.grid(row=(2*n), column=n, sticky='') 


if __name__ == '__main__':
    app = TkRoot()
    app.minsize(50, 50)
    app.mainloop()
