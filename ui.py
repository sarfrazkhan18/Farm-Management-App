import tkinter as tk
from tkinter import ttk, messagebox
from database import *
from datetime import datetime

class FarmManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Farm Management System")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.create_crops_tab()
        self.create_tasks_tab()
        self.create_cows_tab()
        self.create_milk_production_tab()

    # ... (keep the create_crops_tab method as is) ...

    def create_tasks_tab(self):
        tasks_frame = ttk.Frame(self.notebook)
        self.notebook.add(tasks_frame, text="Tasks")

        ttk.Label(tasks_frame, text="Description:").grid(row=0, column=0, padx=5, pady=5)
        self.task_description = ttk.Entry(tasks_frame, width=40)
        self.task_description.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tasks_frame, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.task_due_date = ttk.Entry(tasks_frame)
        self.task_due_date.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(tasks_frame, text="Add Task", command=self.add_task_ui).grid(row=2, column=0, columnspan=2, pady=10)

        self.tasks_tree = ttk.Treeview(tasks_frame, columns=("ID", "Description", "Due Date"), show="headings")
        self.tasks_tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.tasks_tree.heading("ID", text="ID")
        self.tasks_tree.heading("Description", text="Description")
        self.tasks_tree.heading("Due Date", text="Due Date")

        ttk.Button(tasks_frame, text="Refresh Tasks", command=self.refresh_tasks).grid(row=4, column=0, columnspan=2, pady=10)

    def create_cows_tab(self):
        cows_frame = ttk.Frame(self.notebook)
        self.notebook.add(cows_frame, text="Cows")

        ttk.Label(cows_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.cow_name = ttk.Entry(cows_frame)
        self.cow_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(cows_frame, text="Breed:").grid(row=1, column=0, padx=5, pady=5)
        self.cow_breed = ttk.Entry(cows_frame)
        self.cow_breed.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(cows_frame, text="Birth Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        self.cow_birth_date = ttk.Entry(cows_frame)
        self.cow_birth_date.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(cows_frame, text="Add Cow", command=self.add_cow_ui).grid(row=3, column=0, columnspan=2, pady=10)

        self.cows_tree = ttk.Treeview(cows_frame, columns=("ID", "Name", "Breed", "Birth Date", "Last Milked"), show="headings")
        self.cows_tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.cows_tree.heading("ID", text="ID")
        self.cows_tree.heading("Name", text="Name")
        self.cows_tree.heading("Breed", text="Breed")
        self.cows_tree.heading("Birth Date", text="Birth Date")
        self.cows_tree.heading("Last Milked", text="Last Milked")

        ttk.Button(cows_frame, text="Refresh Cows", command=self.refresh_cows).grid(row=5, column=0, columnspan=2, pady=10)

    def create_milk_production_tab(self):
        milk_frame = ttk.Frame(self.notebook)
        self.notebook.add(milk_frame, text="Milk Production")

        ttk.Label(milk_frame, text="Cow ID:").grid(row=0, column=0, padx=5, pady=5)
        self.milk_cow_id = ttk.Entry(milk_frame)
        self.milk_cow_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(milk_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.milk_date = ttk.Entry(milk_frame)
        self.milk_date.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(milk_frame, text="Quantity (liters):").grid(row=2, column=0, padx=5, pady=5)
        self.milk_quantity = ttk.Entry(milk_frame)
        self.milk_quantity.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(milk_frame, text="Add Milk Production", command=self.add_milk_production_ui).grid(row=3, column=0, columnspan=2, pady=10)

        self.milk_tree = ttk.Treeview(milk_frame, columns=("ID", "Cow ID", "Date", "Quantity"), show="headings")
        self.milk_tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.milk_tree.heading("ID", text="ID")
        self.milk_tree.heading("Cow ID", text="Cow ID")
        self.milk_tree.heading("Date", text="Date")
        self.milk_tree.heading("Quantity", text="Quantity (liters)")

        ttk.Button(milk_frame, text="Refresh Milk Production", command=self.refresh_milk_production).grid(row=5, column=0, columnspan=2, pady=10)

    # ... (keep the add_crop_ui and refresh_crops methods as is) ...

    def add_task_ui(self):
        description = self.task_description.get()
        due_date = self.task_due_date.get()
        if description and due_date:
            add_task(description, due_date)
            messagebox.showinfo("Success", "Task added successfully!")
            self.refresh_tasks()
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def refresh_tasks(self):
        for item in self.tasks_tree.get_children():
            self.tasks_tree.delete(item)
        for task in list_tasks():
            self.tasks_tree.insert("", "end", values=task)

    def add_cow_ui(self):
        name = self.cow_name.get()
        breed = self.cow_breed.get()
        birth_date = self.cow_birth_date.get()
        if name and breed and birth_date:
            add_cow(name, breed, birth_date, datetime.now().strftime("%Y-%m-%d"))
            messagebox.showinfo("Success", "Cow added successfully!")
            self.refresh_cows()
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def refresh_cows(self):
        for item in self.cows_tree.get_children():
            self.cows_tree.delete(item)
        for cow in list_cows():
            self.cows_tree.insert("", "end", values=cow)

    def add_milk_production_ui(self):
        cow_id = self.milk_cow_id.get()
        date = self.milk_date.get()
        quantity = self.milk_quantity.get()
        if cow_id and date and quantity:
            add_milk_production(int(cow_id), date, float(quantity))
            messagebox.showinfo("Success", "Milk production record added successfully!")
            self.refresh_milk_production()
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def refresh_milk_production(self):
        for item in self.milk_tree.get_children():
            self.milk_tree.delete(item)
        for record in list_milk_production():
            self.milk_tree.insert("", "end", values=record)

if __name__ == "__main__":
    init_db()
    app = FarmManagementApp()
    app.mainloop()