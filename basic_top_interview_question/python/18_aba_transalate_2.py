
# Aba Translate
# Aba is a German children’s game where secret messages are exchanged. In Aba, after every vowel we add “b” and add that same vowel.

# Write a method `aba_translate` that takes in a sentence string and returns a new sentence representing its Aba translation. Capitalized words of the original sentence should be properly capitalized in the new sentence.

# aba_translate(“Cats and dogs”) #=> “Cabats aband dobogs”

# aba_translate(“Everyone can code”) #=> “Ebeveberyobonebe caban cobodebe”

# aba_translate(“Africa is Africa in German”) #=> “Abafribicaba ibis Abafribicaba ibin Gebermaban”


def aba_translate(string):
    vowels, t_string = "aeiou", ""
    
    for letter in string:
        t_string += letter
        if letter.lower() in vowels:
            t_string += 'b' +  letter.lower()
    return t_string

string1 = "Cats and dogs"
string2 = "Everyone can code"
string3 = "Africa is Africa in German"

print(aba_translate(string1))
print(aba_translate(string2))
print(aba_translate(string3))