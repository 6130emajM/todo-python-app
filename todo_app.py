"""
To-Do List Application
A simple command-line interface application for managing tasks.
Author: SE Foundations Student
Date: December 2025
"""

# Global list to store tasks
tasks = []


def display_welcome():
    """Display welcome message and application title."""
    print("\n" + "="*50)
    print("    WELCOME TO YOUR TO-DO LIST APPLICATION")
    print("="*50 + "\n")


def display_menu():
    """Display the main menu options."""
    print("\n--- MAIN MENU ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Quit")
    print("-" * 17)


def add_task():
    """
    Add a new task to the to-do list.
    Prompts user for task description and adds it to the tasks list.
    """
    try:
        task = input("\nEnter the task description: ").strip()
        
        if not task:
            print("❌ Error: Task description cannot be empty!")
            return
        
        tasks.append(task)
        print(f"✓ Task added successfully: '{task}'")
        
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    finally:
        print()  # Add spacing for readability


def view_tasks():
    """
    Display all tasks in the to-do list.
    Shows numbered list of tasks or message if list is empty.
    """
    try:
        if not tasks:
            print("\n📭 No tasks to display. Your to-do list is empty!")
            return
        
        print("\n--- YOUR TO-DO LIST ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print(f"\nTotal tasks: {len(tasks)}")
        
    except Exception as e:
        print(f"❌ An error occurred while viewing tasks: {e}")
    finally:
        print()  # Add spacing for readability


def delete_task():
    """
    Delete a task from the to-do list.
    Prompts user for task number and removes it if valid.
    """
    try:
        if not tasks:
            print("\n📭 No tasks to delete. Your to-do list is empty!")
            return
        
        # Display current tasks first
        view_tasks()
        
        # Get user input for task number
        task_num = input("Enter the task number to delete: ").strip()
        
        # Validate input is a number
        if not task_num.isdigit():
            print("❌ Error: Please enter a valid number!")
            return
        
        task_index = int(task_num) - 1
        
        # Check if task number is in valid range
        if task_index < 0 or task_index >= len(tasks):
            print(f"❌ Error: Task number {task_num} doesn't exist!")
            print(f"   Please enter a number between 1 and {len(tasks)}.")
            return
        
        # Delete the task
        deleted_task = tasks.pop(task_index)
        print(f"✓ Task deleted successfully: '{deleted_task}'")
        
    except ValueError:
        print("❌ Error: Invalid input. Please enter a valid number!")
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    finally:
        print()  # Add spacing for readability


def get_user_choice():
    """
    Get and validate user's menu choice.
    Returns the user's choice as a string.
    """
    try:
        choice = input("Enter your choice (1-4): ").strip()
        return choice
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
        return "4"  # Exit if user interrupts
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None


def main():
    """
    Main function to run the To-Do List application.
    Manages the application flow and user interaction loop.
    """
    display_welcome()
    
    while True:
        try:
            display_menu()
            choice = get_user_choice()
            
            if choice == "1":
                add_task()
                
            elif choice == "2":
                view_tasks()
                
            elif choice == "3":
                delete_task()
                
            elif choice == "4":
                print("\n👋 Thank you for using the To-Do List Application!")
                print("   Have a productive day!\n")
                break
                
            else:
                print(f"\n❌ Error: '{choice}' is not a valid option!")
                print("   Please select a number between 1 and 4.\n")
                
        except KeyboardInterrupt:
            print("\n\n👋 Application interrupted. Goodbye!\n")
            break
            
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            print("   Please try again.\n")
            
        finally:
            pass  # Ensures cleanup even if errors occur


# Entry point of the application
if __name__ == "__main__":
    main()
