from datetime import date

last_id = 0


class Note:
    def __init__(self, memo, tags):
        global last_id
        self.memo = memo
        self.tags = tags
        self.creation_date = date.today()
        last_id += 1
        self.id = last_id

    def match(self, filters):
        return filters in self.memo or filters in self.tags

    def __repr__(self):
        return f'{self.id}'

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        self.__find_note(note_id).memo = memo

    def modify_tag(self, note_id, tag):
        self.__find_note(note_id).tags = tag

    def search(self, filter):
        return [note for note in self.notes if
                note.match(filter)]

    def __find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note

if __name__ == '__main__':
    n1 = Note('This is my first note', 'Note 1')
    n2 = Note('This is my second note', 'Note 2')

    print(n1.memo, n1.tags)
    print(n2)
    print(n1.match('Note 1'))

    notebook1 = Notebook()
    notebook1.new_note(n1.memo, n1.tags)
    notebook1.new_note(n2.memo, n2.tags)
    notebook1.new_note('My second first note', 'Note 1')
    notebook1.new_note('My_third note', 'Note 3')
    search_res = notebook1.search('Note 1')

    notebook1.modify_tag(3, 'Note A')

