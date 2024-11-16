
class RansomNote:
    """
    Ransom Note Class.
    """

    def can_construct(self, ransom_note, magazine):
        """
        Returns true if the ransome_note can be constructed
        from magazine.
        """
        obj={
            
        }
        for letter in ransom_note:
            if letter in obj:
                obj[letter] +=1
            else:
                obj[letter]=1
        
        can_construct = True
        for letter in obj:
            letter_count = obj[letter]
            if (ransom_note.count(letter) != letter_count ):
                can_construct = False
                break
        return can_construct
                
    
note = RansomNote()
print(note.can_construct("a", "b"))  # false
print(note.can_construct("aa", "bb"))  # false
print(note.can_construct("aba", "aab"))  # true

