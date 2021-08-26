from database import add_entry, create_table, get_entries


menu = """\nPlease select one of the following options:\n
1) Add new entry for today
2) View entries
3) Exit

Your selection: """


def prompt_new_entry():
    entry_content = input("Enter new entry: ")
    entry_date = input("Enter date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


welcome = "\n### Welcome to your personal journal\n"
print(welcome)
create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("\nInvalid option, please try again\n")
