completed_items = []
uncompleted_items = []

while True:
    def add_item(new_item):
        uncompleted_items.append(new_item)

    def complete_item(new_item):
        input(f"Which of these {uncompleted_items} would you like to mark as complete? ")
        completed_items.append()
    def delete_item(new_item):
        print("Hello")
    def edit_item(new_item):
        print("Hello")   

    print("Press 1 for new item")
    print("Press 2 to complete item")
    print("Press 3 to delete otem")
    print("Press 4 to edit item")

    choice = int(input("Enter a Number 1 - 5: "))

    if  choice == 1:
        new_item = input("What should it be called? ")
        add_item(new_item)
        print("Current uncompleted items: ", uncompleted_items)

    if choice == 2:
        completed_item = input(f"Which of these {uncompleted_items} would you like to mark as complete? ")
        completed_items.append(completed_item)
        uncompleted_items.remove(completed_item)
        print("Current completed items: ", completed_items)
        
    if choice == 3:
        delete = input(f"Which of these {uncompleted_items} would you like to delete? ")
        uncompleted_items.remove(delete)
        print("Current uncompleted items: ", uncompleted_items)

    if choice == 4:
        delete_edit = input(f"Which of these {uncompleted_items} would you like to edit? ")
        edit = input("What would you like to replace it with? ")
        uncompleted_items.remove(delete_edit)
        uncompleted_items.append(edit)
        print("Current uncompleted items: ", uncompleted_items)
