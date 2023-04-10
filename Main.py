from ui import UI
from Resource_Manager import ResourceManager
from Data_Persistence import DataPersistence

def main():
    data_persistence = DataPersistence()  # initialize data persistence manager
    resource_manager = ResourceManager(data_persistence.load_data())  # initialize resource manager with data from file
    ui = UI(resource_manager)  # initialize UI with resource manager

    while True:
        ui.display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            ui.create_resource()
        elif choice == "2":
            ui.search_resource()
        elif choice == "3":
            ui.edit_resource()
        elif choice == "4":
            ui.delete_resource()
        elif choice == "5":
            data_persistence.save_data(resource_manager.get_all_resources())  # save data to file
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
