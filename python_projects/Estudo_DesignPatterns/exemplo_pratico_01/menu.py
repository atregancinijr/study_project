import sys
from exemplo_pratico_01.notebook import Notebook, Note
class Menu:
    def __init__(self):
        '''Display a menu and respond to choices when run.'''
        self.notebook = Notebook()
        self.choices = {"1": self.show_notes,
                        "2": self.search_notes,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.quit}

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def display_menu(self):
        print("Notebook Menu:\n 1. Show all Notes\n 2. Search Notes\n 3. Add Note\n 4. Modify Note\n 5. Quit")

    def show_notes(self, notes=None):
        if not notes:
            for i, note in enumerate(self.notebook.notes):
                print(f'iD: {note.id}\n'
                      f'Note: {note.memo}\n'
                      f'Tag: {note.tags}\n'
                      f'\n')
        else:
            print(f'The following notes were found: \n')
            for note in notes:
                print(f'iD: {note.id}\n'
                      f'Note: {note.memo}\n'
                      f'Tag: {note.tags}\n')

    def search_notes(self):
        filter = input("Enter with a filter: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        tag = input("Enter a tag: ")
        self.notebook.new_note(memo, tag)
        print("Your note has been added.")

    def modify_note(self):
        id = int(input("Enter the note ID: "))
        if len(self.notebook.notes) < int(id):
            print(f"The iD '{id}' does not exist.  We just have {len(self.notebook.notes)} added notes")
        else:
            memo = input("Enter the new memo: ")
            tag = input("Enter the new tag: ")
            if memo:
                self.notebook.modify_memo(id, memo)
            if tag:
                self.notebook.modify_tag(id, tag)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)





if __name__ == '__main__':
    Menu().run()