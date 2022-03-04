# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Brandon Lorge, 3.2.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
rowDic = {} # A row of data separated into elements of a dictionary {Product, Price}
table_lst = [] # A list that acts as a table of rows

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

# Creating the Constructor
    def __init__(self, __Product_Name, __Product_Price):
    # Attributes
        self.ProductName = __Product_Price
        self.ProductPrice = __Product_Price

    # Properties
    # Product Name Getter
    @property
    def Product_Name(self):
        return str(self.__Product_Name).title()
    # Product Name Setter
    @Product_Name.setter
    def Product_Name(self, value):
        if str(value).isnumeric() == True:
            self.__Product_Name = value
        else:
            raise Exception("Names cannot be numbers")


    # Product Price Getter
    @property
    def Product_Price(self):
        return str(self.__Product_Price).title()


    # Product Price Setter
    @Product_Price.setter
    def Product_Price(self, value):
        if str(value).isnumeric() == False:
            self.__Product_Price = value
        else:
            raise Exception("Product Price Must Be Numbers")
    # Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Brandon Lorge, 3.3.2022,Modified code to complete assignment 8
    """
    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        file = open(file_name, "w")
        for row in list_of_rows:
            file.write((row["Product"] + ", " + row["Price"]) + '\n')
        print("Data was saved to file ")
        file.close()
        return list_of_rows

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Product": task.strip(), "Price": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(Product, Price, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Product": str(Product).strip(), "Price": str(Price).strip()}
        list_of_rows.append(row)
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():   # Code to Show Menu to User
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Add a New Product
            2) View Current Data
            3) Save Data and Exit Program
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():  # Get Users Choice
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_products_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("************** Current List: *****************")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product_and_price():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        Product = (input("Enter a Product: ")).strip()
        Price = (input("Enter a Price: ")).strip()
        return (Product, Price)
        pass


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from products.txt.
FileProcessor.read_data_from_file(file_name=strFileName, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Product
        Product, Price = IO.input_new_product_and_price()
        table_lst = FileProcessor.add_data_to_list(Product=ProductName, Price=ProductPrice, list_of_rows=table_lst)
        print(IO.output_current_products_in_list(list_of_rows=table_lst))
        continue  # to show the menu

    elif choice_str == '2':  # View List
        # task = IO.output_current_products_in_list(list_of_rows)
        # table_lst = list_of_rows
        IO.output_current_products_in_list(list_of_rows=table_lst)  # Show current data in the list/table
        continue  # to show the menu

    elif choice_str == '3':  # Exit Program
        FileProcessor.write_data_to_file(file_name=strFileName, list_of_rows=table_lst)
        print("Goodbye!")
        break  # by exiting loop

# Main Body of Script  ---------------------------------------------------- #

