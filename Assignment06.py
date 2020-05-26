# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoFile.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# Kate Golenkova,05/22/2020, Modified code to complete assignment 6
# Kate Golenkova,05/23/2020, Modified code to complete assignment 6
# Kate Golenkova, 05/24/2020, Modified code to complete assignment 6
#
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open("C:\_PythonClass\Assignment06\ToDoFile.txt", "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        # TODO: Add Code Here!
        # add new row of task and priority to list_of_rows
        row = {"Task": task, "Priority": priority}
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        # TODO: Add Code Here!
        # remove row for exact task if this task is in list_of_rows
        found = False
        for row in list_of_rows:
            if row["Task"].lower() == strTask.lower():
                list_of_rows.remove(row)
                IO.print_row_removed()
                found = True
                break
        # if task not found, return to Menu
        if not found:
             IO.print_task_not_found()
        return list_of_rows, 'Success'

    # @statismethod
    # def check_for_duplicates(list_of_rows):
    #     tasks = set()
    #     for row in list_of_rows:
    #         if i in tasks:
    #             return True
    #         else:
    #             tasks.add(i)
    #     return False


    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Add Code Here!
        # open file, save data to it and close the file
        file = open("C:\_PythonClass\Assignment06\ToDoFile.txt", "w")
        for row in list_of_rows:
            file.write("{0},{1}\n".format(row["Task"], row["Priority"]))
        file.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + str(row["Priority"]) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        # pass  # TODO: Add Code Here!
        # user input for task and priority
        task = input("Please enter a Task you want to add: ")
        task = task.capitalize()
        # while loop to check if priority is number. If user put not number, loop will start again
        while True:
            priority = input("Please enter number to set Priority for this task: ")
            if priority.isdigit() == True:
                for row in dicRow:
                    print(row["Task"] + " (" + row["Priority"] + ")")
            else:
                continue
            return task, priority

    @staticmethod
    def input_task_to_remove():
        #pass  # TODO: Add Code Here!
        # user input for task he wants to delete
        task = input("Please type the Task you want to delete: \n")
        return task

    @staticmethod
    def print_row_removed(): # function to confirm the row has been deleted
        print("The row has been deleted.")

    @staticmethod
    def print_task_not_found(): # function to inform user task not found in list
        print("This Task not found.")

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        (strTask, strPriority) = IO.input_new_task_and_priority() # Get user input new data
        Processor.add_data_to_list(strTask, strPriority, lstTable) # Put new data to list
        IO.input_press_to_continue(strStatus) # Get user back to Menu
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here
        strTask = IO.input_task_to_remove() # Get user input task
        Processor.remove_data_from_list(strTask, lstTable) # Remove row with exact task
        IO.input_press_to_continue(strStatus) # Get user back to Menu
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
            Processor.write_data_to_file(strFileName, lstTable) # Write data to file
            print("Your data has been saved!\n")
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Add Code Here!
            Processor.read_data_from_file(strFileName, lstTable) # Read data from file
            print("Data has been reloaded from file.")
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
