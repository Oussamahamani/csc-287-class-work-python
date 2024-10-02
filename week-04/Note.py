class Note:
    def __init__(self,id,url):
        self.id = id
        self.url = url
        
    def describe(self):
        print(f"id is {self.id}, url is {self.url}")
        

note_1 = Note("types safety is not necessary and neither testing","url-1")
note_2 = Note("functional programming > oop","url-2")
note_3 = Note("javascript is the best programming language, javascript > typescript","url-3")
note_4 = Note("You don't need comments and documentation","url-4")
 