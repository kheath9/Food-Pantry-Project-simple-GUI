import tkinter as tk


root = tk.Tk()
root.title("Food Pantry App")
root.geometry("250x600")


# FOOD DONATION LABELS, ENTRY BOXES, AND BUTTONS

# Food donation labels
tk.Label(root, text="Food Donation", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2,
                                                                      padx=10, pady=5)
tk.Label(root, text="Donor Name:").grid(row=1, column=0, sticky="e")

# Food donation entry box
food_donor_entry = tk.Entry(root)
food_donor_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Food item label
tk.Label(root, text="Item:").grid(row=2, column=0, sticky="e")

# Food item entry box
food_entry = tk.Entry(root)
food_entry.grid(row=2, column=1, padx=10, pady=10)

# Food amount label
tk.Label(root, text="Amount:").grid(row=3, column=0, sticky="e")

# Food amount entry box
food_quantity_entry = tk.Entry(root)
food_quantity_entry.grid(row=3, column=1, padx=10, pady=10)

# Food donation add button, command = 'None' for now
tk.Button(root, text="Add Food Donation", command=None).grid(row=4, column=0,
                                                             columnspan=2, pady=5)

# MONEY DONATION LABELS, ENTRY BOXES, AND BUTTONS

# Money donation labels
tk.Label(root, text="Money Donation", font=("Arial", 10, "bold")).grid(row=5, column=0,
                                                                       columnspan=2, padx=10, pady=5)
tk.Label(root, text="Donor Name:").grid(row=6, column=0, sticky="e")

# Money donation entry box
money_donor_entry = tk.Entry(root)
money_donor_entry.grid(row=6, column=1, pady=10)

# Money donation amount labels
tk.Label(root, text="Amount ($):").grid(row=7, column=0, sticky="e")

# Money donation entry box
money_entry = tk.Entry(root)
money_entry.grid(row=7, column=1, pady=10)

# Money donation button, command = 'None' for now
tk.Button(root, text="Add Money Donation", command=None).grid(row=8, column=0,
                                                              columnspan=2, pady=5)

# FOOD DISTRIBUTION LABELS, ENTRY, AND BUTTONS

# Distribution labels
tk.Label(root, text="Food Distribution", font=("Arial", 10, "bold")).grid(row=9, column=0,
                                                                          columnspan=2, padx=10, pady=5)
tk.Label(root, text="Household:").grid(row=10, column=0, sticky="e")

# Distribution entry box
household_entry = tk.Entry(root)
household_entry.grid(row=10, column=1, pady=10)

# Item label and entry box
tk.Label(root, text="Item:").grid(row=11, column=0, sticky="e")
distribute_item_entry = tk.Entry(root)
distribute_item_entry.grid(row=11, column=1, pady=10)

# Amount label and entry box
tk.Label(root, text="Quantity:").grid(row=12, column=0, sticky="e")
distribute_quantity_entry = tk.Entry(root)
distribute_quantity_entry.grid(row=12, column=1, pady=10)

# Button to record distributions, command = 'None' for now
tk.Button(root, text="Record Distribution", command=None).grid(row=13, column=0,
                                                               columnspan=2, pady=5)

# Button to view distributions, command = 'None' for now
tk.Button(root, text="View Distributions", command=None).grid(row=14, column=0,
                                                              columnspan=2, pady=10)

# Button to view inventory, command = 'None' for now
tk.Button(root, text="View Inventory", command=None).grid(row=15, column=0,
                                                           columnspan=2, pady=5)

root.mainloop()



