from Note import Note

class TextNote(Note):
    def __init__(self, id, url,text):
        super().__init__(id, url)
        self.text = text
        
    def describe(self):
        print(f"id is {self.id}, url is {self.url}, text is {self.text}")
        
        
note_1 = TextNote("functional programming > oop","url-2","lorem text stuff")
note_1.describe()


