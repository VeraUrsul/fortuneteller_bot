name = 'Максим'
VALUE_OF_LETTER = dict(
    а=1, б=2, в=3, г=4, д=5, е=6, ё=7, ж=8, з=9, и=1, й=2, к=3, л=4, м=5,
    н=6, о=7, п=8, р=9, с=1, т=2, у=3, ф=4, х=5, ц=6, ч=7, ш=8, щ=9, ъ=1,
    ы=2, ь=3, э=4, ю=5, я=6
    )
     
    
    
     
     
    
    
    


value_of_name = sum([VALUE_OF_LETTER[letter] for letter in name.lower()])
while value_of_name > 9:
    value_of_name = value_of_name // 10 + value_of_name % 10

   

print(value_of_name)