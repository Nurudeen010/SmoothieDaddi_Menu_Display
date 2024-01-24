import csv
import pathlib

# List to store items from the CSV file
listedItems = []

# Check if the CSV file exists
check = pathlib.Path("SmoothieDadii.csv")
if check.exists() == False:
    raise FileExistsError("Wrong File")
else:
    # Open and read the CSV file
    with open("SmoothieDadii.csv", "r") as f:
        # Create a CSV reader that interprets each row as a dictionary
        openedDoc = csv.DictReader(f)
        
        # Iterate through each row in the CSV file and append it to the list
        for items in openedDoc:
            listedItems.append(items)

# Define a Product class to represent each item
class Product: 
    def __init__(self, name_of_product: str, price: int, description: str, quantity: str):
        self.name = name_of_product
        self.price = price
        self.description = description
        self.quantity = quantity
    
    def displayProducts(self):
        # Return a formatted string with product information
        return f"""
Product Information:
    Name: {self.name}
    Description: {self.description}
    Price: N{self.price:.2f}
    Quantity: {self.quantity} units
--------------------------
"""

# Create Product instances for each row in the CSV file and display product information
for row in listedItems:
    eachProduct = Product(
        name_of_product=row["Name"],
        price=int(row["Price"]),
        description=row["Description"],
        quantity=int(row["Quantity"])
    )

    # Print the formatted product information for each Product instance
    print(eachProduct.displayProducts())