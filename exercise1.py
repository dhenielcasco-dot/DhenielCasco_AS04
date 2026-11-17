def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of {amount:.2f} is due: {due_date}")

display_invoice("John Doe", 150.75, "2024-07-15")