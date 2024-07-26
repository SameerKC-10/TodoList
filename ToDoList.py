from tabulate import tabulate
import colorama
from colorama import Fore,Style
import pyfiglet
import csv
import time


colorama.init(autoreset = True)


def menu():
    table = [["1",Fore.YELLOW + "View Tasks" + Style.RESET_ALL] ,["2",Fore.GREEN + Style.BRIGHT +"Add Tasks" + Style.RESET_ALL],["3",Fore.RED + Style.BRIGHT + "Delete Tasks" + Style.RESET_ALL],["4",Fore.MAGENTA + Style.DIM + "Exit" + Style.RESET_ALL]]
    print(tabulate(table, tablefmt="double_outline"))
    while True:
        try:
            choice = input("Enter:")
            if choice in ["1", "2", "3", "4"]:
                return choice
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Please Enter Option 1(View Tasks), 2(Add Tasks), 3(Delete Tasks) or 4(Exit)\n")
            continue
        else:
            print(Fore.RED + Style.BRIGHT + "Please Enter Option 1(View Tasks), 2(Add Tasks), 3(Delete Tasks) or 4(Exit)\n")


def welcome():
    border =("--------------------------------------------")
    welcome = pyfiglet.figlet_format("TO DO List")
    print(Fore.YELLOW + border)
    print("")
    print(Fore.YELLOW + welcome)
    print(Fore.YELLOW + border)


def main():
    welcome()
    choice = menu()
    if choice == "1":
        Menu.View()
    if choice == "2":
        Menu.Add()
    if choice == "3":
        Menu.Delete()
    if choice == "4":
        Menu.Exit()

def running():
    choice = menu()
    if choice == "1":
        Menu.View()
    if choice == "2":
        Menu.Add()
    if choice == "3":
        Menu.Delete()
    if choice == "4":
        Menu.Exit()


class Menu:

    with open("List.csv", "r") as file:
        reader = csv.DictReader(file)
        tasks_list = []
        for line in reader:
            task = line["task"]
            tasks_list.append(task)

    def View():
        tab = [["Number", "Task"]]
        for i in Menu.tasks_list:
            tab.append([Menu.tasks_list.index(i)+1, i])
        print(Fore.YELLOW + tabulate(tab, headers="firstrow", tablefmt="rounded_outline"))
        time.sleep(2)
        running()



    def Add():
        user_input = input(Fore.GREEN + Style.BRIGHT + "Add a Task: " + Style.RESET_ALL)
        Menu.tasks_list.append(user_input)
        task_dict = {"number": Menu.tasks_list.index(user_input)+ 1, "task": user_input}
        with open("List.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["number", "task"])
            writer.writerow(task_dict)
        print("Grabbing List...")
        time.sleep(1)
        print("Appending Data...")
        time.sleep(1)
        print(Fore.GREEN + Style.BRIGHT + "Task has been added to To Do List")
        time.sleep(2)
        running()
        
        


    def Delete():
        while True:
            try:
                delete = int(input(Fore.RED + Style.BRIGHT + "Task Number: " + Style.RESET_ALL)) - 1
                num = len(Menu.tasks_list) - 1
                if (delete > num) or (delete < 0):
                    print(Fore.RED + Style.BRIGHT + "Please enter a Task number")
                    continue
                else:
                    break
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Please enter a Task number")
                continue
        deleted_task = Menu.tasks_list[delete]
        Menu.tasks_list.remove(deleted_task)
        with open("List.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["number", "task"])
            writer.writeheader()
            for i in Menu.tasks_list:
                writer.writerow({"number":Menu.tasks_list.index(i) + 1, "task": i})
            print("Gathering Data...")
            time.sleep(1)
            print("Removing Task from List...")
            time.sleep(1)
            print(Fore.RED + Style.BRIGHT + "Task has been Removed Succesfully" + Style.RESET_ALL)
            time.sleep(2)
            running()


    def Exit():
        goodbye = pyfiglet.figlet_format("Thank You For Using ToDoList!")
        print(Fore.YELLOW + Style.BRIGHT + goodbye + Style.RESET_ALL)


if __name__ == "__main__":
    main()