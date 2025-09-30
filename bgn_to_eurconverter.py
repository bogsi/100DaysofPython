import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        # create widgets
        self.label = tk.Label(text="BGN to EUR Converter")
        self.label.pack(pady=10)
        
        self.numberEntry = tk.Entry()
        self.numberEntry.pack(pady=5)
        
        self.convertButton = tk.Button(text="Convert", command=self.convert)
        self.convertButton.pack(pady=5)
        
        self.output = tk.Label(text="")
        self.output.pack(pady=10)
    
    def convert(self):
        try:
            bgn_amount = float(self.numberEntry.get())
            eur_amount = bgn_amount / 1.95583  # BGN to EUR exchange rate
            self.output.config(text=f"{bgn_amount:.2f} BGN = {eur_amount:.2f} EUR")
        except ValueError:
            self.output.config(text="Please enter a valid number")
        
# create the application
root = tk.Tk()
root.title("BGN to EUR Converter")
app = Application(master=root)

# start the program
root.mainloop()
