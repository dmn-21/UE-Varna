import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from data import DataManager
from utils import calculate_total_value, generate_category_summary


class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("900x700")
        self.root.configure(bg="#e0f7fa")

        self.data_manager = DataManager()

        self.setup_ui()

        self.data_manager.load_data()
        self.refresh_tree()

    def setup_ui(self):
        title_label = tk.Label(
            self.root,
            text="Inventory Management System",
            font=("Arial", 24, "bold"),
            bg="#e0f7fa",
            fg="#00796b",
        )
        title_label.pack(pady=10)

        self.frame_buttons = tk.Frame(self.root, bg="#e0f7fa")
        self.frame_buttons.pack(pady=10)

        ttk.Button(self.frame_buttons, text="Add Item", command=self.add_item).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(self.frame_buttons, text="Edit Item", command=self.edit_item).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.frame_buttons, text="Delete Item", command=self.delete_item).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(self.frame_buttons, text="Export Report", command=self.export_report).grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(
            self.frame_buttons, text="Category Summary", command=self.show_category_summary
        ).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(
            self.frame_buttons, text="Total Value Summary", command=self.show_total_value_summary
        ).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(
            self.frame_buttons, text="Export Category Summary", command=self.export_category_summary
        ).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(
            self.frame_buttons, text="Export Total Value", command=self.export_total_value_summary
        ).grid(row=1, column=3, padx=5, pady=5)

        tree_frame = tk.Frame(self.root, bg="#e0f7fa")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(tree_frame, columns=("Name", "Quantity", "Price", "Category"), show="headings")
        self.tree.pack(fill="both", expand=True)

        for col in ["Name", "Quantity", "Price", "Category"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        tree_scroll_x = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree.xview)
        tree_scroll_y = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(xscrollcommand=tree_scroll_x.set, yscrollcommand=tree_scroll_y.set)

        tree_scroll_x.pack(side="bottom", fill="x")
        tree_scroll_y.pack(side="right", fill="y")

    def refresh_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in self.data_manager.inventory:
            self.tree.insert("", "end", values=(item["Name"], item["Quantity"], item["Price"], item["Category"]))

    def add_item(self):
        def save_new_item():
            name = entry_name.get().strip()
            quantity = entry_quantity.get().strip()
            price = entry_price.get().strip()
            category = entry_category.get().strip()

            if not (name and quantity.isdigit() and price.replace('.', '', 1).isdigit() and category):
                messagebox.showerror("Error", "Invalid input. Please fill all fields correctly.")
                return

            self.data_manager.inventory.append({
                "Name": name,
                "Quantity": quantity,
                "Price": price,
                "Category": category
            })
            self.refresh_tree()
            self.data_manager.save_data()
            add_window.destroy()

        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Item")
        add_window.geometry("400x300")
        add_window.configure(bg="#e0f7fa")

        tk.Label(add_window, text="Name", bg="#e0f7fa", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Quantity", bg="#e0f7fa", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
        entry_quantity = tk.Entry(add_window)
        entry_quantity.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Price", bg="#e0f7fa", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
        entry_price = tk.Entry(add_window)
        entry_price.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Category", bg="#e0f7fa", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
        entry_category = tk.Entry(add_window)
        entry_category.grid(row=3, column=1, padx=10, pady=10)

        btn_save = ttk.Button(add_window, text="Save", command=save_new_item)
        btn_save.grid(row=4, columnspan=2, pady=20)

    def edit_item(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No item selected.")
            return

        item_values = self.tree.item(selected_item[0], "values")

        def save_edited_item():
            name = entry_name.get().strip()
            quantity = entry_quantity.get().strip()
            price = entry_price.get().strip()
            category = entry_category.get().strip()

            if not (name and quantity.isdigit() and price.replace('.', '', 1).isdigit() and category):
                messagebox.showerror("Error", "Invalid input. Please fill all fields correctly.")
                return

            for item in self.data_manager.inventory:
                if item["Name"] == item_values[0] and item["Quantity"] == item_values[1]:
                    item["Name"] = name
                    item["Quantity"] = quantity
                    item["Price"] = price
                    item["Category"] = category
                    break

            self.refresh_tree()
            self.data_manager.save_data()
            edit_window.destroy()

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Item")

        tk.Label(edit_window, text="Name").grid(row=0, column=0, padx=10, pady=5)
        entry_name = tk.Entry(edit_window)
        entry_name.insert(0, item_values[0])
        entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(edit_window, text="Quantity").grid(row=1, column=0, padx=10, pady=5)
        entry_quantity = tk.Entry(edit_window)
        entry_quantity.insert(0, item_values[1])
        entry_quantity.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(edit_window, text="Price").grid(row=2, column=0, padx=10, pady=5)
        entry_price = tk.Entry(edit_window)
        entry_price.insert(0, item_values[2])
        entry_price.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(edit_window, text="Category").grid(row=3, column=0, padx=10, pady=5)
        entry_category = tk.Entry(edit_window)
        entry_category.insert(0, item_values[3])
        entry_category.grid(row=3, column=1, padx=10, pady=5)

        btn_save = ttk.Button(edit_window, text="Save", command=save_edited_item)
        btn_save.grid(row=4, columnspan=2, pady=10)

    def delete_item(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No item selected.")
            return

        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete the selected item(s)?")
        if not confirm:
            return

        for item in selected_item:
            item_values = self.tree.item(item, "values")
            self.data_manager.inventory = [
                inv
                for inv in self.data_manager.inventory
                if not (inv["Name"] == item_values[0] and inv["Quantity"] == item_values[1])
            ]

        self.refresh_tree()
        self.data_manager.save_data()

    def export_report(self):
        export_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not export_path:
            return

        try:
            with open(export_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Quantity", "Price", "Category"])
                writer.writeheader()
                writer.writerows(self.data_manager.inventory)
            messagebox.showinfo("Success", "Report exported successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export report: {e}")

    def show_category_summary(self):
        category_summary = generate_category_summary(self.data_manager.inventory)

        summary_window = tk.Toplevel(self.root)
        summary_window.title("Category Summary")

        tk.Label(summary_window, text="Category", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(summary_window, text="Total Quantity", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)

        for i, (category, total_quantity) in enumerate(category_summary.items(), start=1):
            tk.Label(summary_window, text=category).grid(row=i, column=0, padx=10, pady=5)
            tk.Label(summary_window, text=total_quantity).grid(row=i, column=1, padx=10, pady=5)

    def show_total_value_summary(self):
        total_value = calculate_total_value(self.data_manager.inventory)

        summary_window = tk.Toplevel(self.root)
        summary_window.title("Total Value Summary")

        tk.Label(summary_window, text="Total Inventory Value", font=("Arial", 12, "bold")).pack(padx=10, pady=10)
        tk.Label(summary_window, text=f"${total_value:.2f}", font=("Arial", 12)).pack(padx=10, pady=10)

    def export_category_summary(self):
        category_summary = generate_category_summary(self.data_manager.inventory)

        export_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not export_path:
            return

        try:
            with open(export_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Category", "Total Quantity"])
                for category, total_quantity in category_summary.items():
                    writer.writerow([category, total_quantity])
            messagebox.showinfo("Success", "Category summary exported successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export category summary: {e}")

    def export_total_value_summary(self):
        total_value = calculate_total_value(self.data_manager.inventory)

        export_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not export_path:
            return

        try:
            with open(export_path, mode="w", encoding="utf-8") as file:
                file.write(f"Total Inventory Value: ${total_value:.2f}\n")
            messagebox.showinfo("Success", "Total value summary exported successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export total value summary: {e}")
