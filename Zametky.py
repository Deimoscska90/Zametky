import json

def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    return {"title": title, "content": content}

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def list_notes(notes):
    if len(notes) == 0:
        print("No notes found.")
    else:
        for note in notes:
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            print()

def edit_note(notes):
    if len(notes) == 0:
        print("No notes found.")
        return
    title = input("Enter the title of the note to edit: ")
    for note in notes:
        if note['title'] == title:
            new_title = input("Enter the new title: ")
            new_content = input("Enter the new content: ")
            note['title'] = new_title
            note['content'] = new_content
            print("Note edited successfully.")
            return
    print("Note not found.")

def delete_note(notes):
    if len(notes) == 0:
        print("No notes found.")
        return
    title = input("Enter the title of the note to delete: ")
    for note in notes:
        if note['title'] == title:
            notes.remove(note)
            print("Note deleted successfully.")
            return
    print("Note not found.")

def main():
    notes = load_notes()
    while True:
        print("1. Create note")
        print("2. View notes")
        print("3. Edit note")
        print("4. Delete note")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            note = create_note()
            notes.append(note)
            save_notes(notes)
            print("Note created successfully.")
        elif choice == '2':
            list_notes(notes)
        elif choice == '3':
            edit_note(notes)
            save_notes(notes)
        elif choice == '4':
            delete_note(notes)
            save_notes(notes)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()