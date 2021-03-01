
# Aba Translate
# Aba is a German children’s game where secret messages are exchanged. In Aba, after every vowel we add “b” and add that same vowel.

# Write a method `aba_translate` that takes in a sentence string and returns a new sentence representing its Aba translation. Capitalized words of the original sentence should be properly capitalized in the new sentence.

# aba_translate(“Cats and dogs”) #=> “Cabats aband dobogs”

# aba_translate(“Everyone can code”) #=> “Ebeveberyobonebe caban cobodebe”

# aba_translate(“Africa is Africa in German”) #=> “Abafribicaba ibis Abafribicaba ibin Gebermaban”


def aba_translate(string):
    vowels_min = ['a', 'e', 'i', 'o', 'u']
    vowels_max = ['A', 'E', 'I', 'O', 'U']
    new_string = ""
    
    for letter in string:
        new_string += letter
        if letter in vowels_min or letter in vowels_max:
            new_string += 'b'
            new_string += letter.lower()
    return new_string

string1 = "Cats and dogs"
string2 = "Everyone can code"
string3 = "Africa is Africa in German"

print(aba_translate(string1))
print(aba_translate(string2))
print(aba_translate(string3))


#Time solving: 11 minutes
# What I learned:
    # String concatenation
    # Handle upper case and lower case