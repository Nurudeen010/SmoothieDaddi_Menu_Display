# SmoothieDadii Product Information Display

This Python program reads product information from a CSV file named "SmoothieDadii.csv" and displays the details in a formatted manner. Each product is represented as an instance of the `Product` class, and its information is printed to the console.

## Prerequisites

- Python 3.x
- CSV file named "SmoothieDadii.csv" with the following columns: "Name", "Price", "Description", "Quantity"

## Usage

1. Ensure you have Python installed on your system.

2. Check if the CSV file "SmoothieDadii.csv" exists. If not, raise a `FileExistsError` indicating a wrong file.

3. Open and read the CSV file, creating a list of product information dictionaries.

4. Define a `Product` class to represent each product with attributes: name, price, description, and quantity.

5. For each row in the CSV file, create a `Product` instance, and print the formatted product information using the `displayProducts` method.

6. Run the program using the command:
   ```bash
   python your_program_filename.py
