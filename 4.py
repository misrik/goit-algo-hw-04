print("Available commands:")
print("  - hello: Greet the assistant")
print("  - add <name> <phone>: Add a new contact")
print("  - change <name> <new_phone>: Update an existing contact")
print("  - show <name>: Show details of a contact")
print("  - all: Show all contacts")
print("  - close/exit: Exit the assistant")

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        raise ValueError("Contact")
    contacts[name] = phone
    return "Contact updated successfully"

def show_contact(args, contacts):
    name, *_ = args
    return contacts[name]

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_contact(args, contacts))
            
        elif command == "all":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")


        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
