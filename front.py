import tkinter as tk
from tkinter import Listbox

class Front:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Front")
        self.list = Listbox(self.root)
        self.item = ['item1', 'item2', 'item3']
        self.list.pack()
        self.update_btn = tk.Button(self.root, text="Update", command=self.update, justify="right")
        self.update_btn.pack()
        self.delete_btn = tk.Button(self.root, text="Delete", command=self.delete, justify="left")
        self.delete_btn.pack()

    def update(self):
        self.list.delete(0, tk.END)
        for item in self.item:
            self.list.insert(tk.END, item)
    def delete(self):
        self.list.delete(0, tk.END)


main = Front()
if __name__ == "__main__":
    main.root.mainloop()