TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

uzivatele = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"

}
oddelovac = "-" * 40

username = input("username:")
password = input("password:")

print(oddelovac)

if username not in uzivatele or uzivatele[username] != password:
    print(f"We are sorry {username} is not registered")
    exit()
else:
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(oddelovac)

user_num_choice = input(f"Enter a number btw. {1} and {len(TEXTS)} to select:")
if user_num_choice.isdigit():
    user_num_choice = int(user_num_choice)
    print(oddelovac)
else:
    print(f"{user_num_choice} není číslo")
    exit()

if not 1 <= user_num_choice <= 3:
    print(f"{user_num_choice} is not number btw. {1} and {len(TEXTS)}")
    exit()
else:
    selected_text = TEXTS[user_num_choice - 1]

words_text = selected_text.split()  
print(f"There are {len(words_text)} words in the selected text")
digits_text = 0
digits_total = 0
text_titlecase = 0
text_uppercase = 0
text_lowercase = 0

for wordst in words_text:
    if wordst.istitle():
        text_titlecase += 1
print(f"There are {text_titlecase} titlecase words.")

for wordst in words_text:
    if wordst.isupper():
        text_uppercase += 1
print(f"There are {text_uppercase} uppercase words.")

for wordst in words_text:
    if wordst.islower():
        text_lowercase += 1
print(f"There are {text_lowercase} lowercase words.")

for wordsn in words_text:
    if wordsn.isdigit():
        digits_total += int(wordsn)
        digits_text += 1
print(f"There are {digits_text} numeric strings.")
print(f"The sum of all the numbers {digits_total}")
print(oddelovac)
print("LEN|  OCCURENCES  |NR.")
print(oddelovac)

cleaned_words = []
for words in words_text:
    words = words.strip(",.?!")
    cleaned_words.append(words)
words_text = cleaned_words

character_number = {} 
for word in words_text:
    word_length = len(word)
    if word_length not in character_number:
        character_number[word_length] = []

    character_number[word_length].append(word)

for length in sorted(character_number.keys()):
    words = character_number[length]
    stars = '*' * len(words) 
    print(f"{length:<2}|{stars:<20}|{len(words)}")


