def display_invoice(username, amount, due_date):
    print(f"Hello {username},")
    print(f"Your bill of £{amount:.2f} is due on: {due_date}.")

display_invoice("John Doe", 150.75, "18/05/2023")  # calling the function