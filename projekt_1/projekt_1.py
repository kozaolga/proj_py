'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Olga Krajickova
email: kozaolga@centrum.cz

pozn.
Dobry den, jsem si vedoma rozdilnych vysledku ve statistickych vypoctech, oproti zadani projektu. 
Tyto nepresnosti vznikly pravdepodobne nejasnou definici, toho co je 'slovo' zda a kdy pocitame
cisla jako slovo ci ne. 
Pokud budu pocitat titlecase/lowercase ze vsech slov, tj, vsetne cisel vyjdou spravne, 
ale spatne bude uppercase, protoze zahrnuje i 30N. Samozrejme na zadost upravim. 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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

text_1 = TEXTS[0]
text_2 = TEXTS[1]
text_3 = TEXTS[2]
# hyphen border line counter
hyphen = len('Enter a number btw. 1 and 3 to select: ') +1
# registered users
login = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

# login
user = input('login:')
password = input('password:')
# hyphen border line
print('-' * hyphen)
# login check
if login.get(user) != password:
    print('unregistered user, terminating the program..')
    exit()
else:
    print(
        'Welcome to the app,', user,
        '\nWe have 3 texts to be analyzed.'
         )

# hyphen border line
print('-' * hyphen)

# available texts
text_s = {'1': text_1, '2': text_2, '3': text_3}
# text selection
text_n = input ('Enter a number btw. 1 and 3 to select: ')
# hyphen border line
print('-' * hyphen)
# text control
if text_n not in text_s:
    print('invalid input, terminating program...')    
    exit()

# statistics for the given words
words = text_s[text_n].split()
counter_w = len(words)
listofnum = []

result = {'words_count': counter_w, 'titlecase': 0, 'uppercase': 0, 'lowercase': 0,'numeric_string': 0,'sum': 0 }

for word in words:
    if word.isalpha():
        if word.istitle():
            result['titlecase'] += 1
        if word.isupper():
            result['uppercase'] += 1
        if word.islower():
            result['lowercase'] += 1
    if word.isnumeric():
        result['numeric_string'] += 1
        listofnum.append(word)


result['sum'] = sum(int(num_str) for num_str in listofnum)

    
print ('There are', result['words_count'], 'words in the selected text.')
print ('There are', result['titlecase'], 'titlecase words.')
print ('There are', result['uppercase'], 'uppercase words.')
print ('There are', result['lowercase'], 'lowercase words.')
print ('There are', result['numeric_string'], 'numeric strings.')
print ('The sum of all the numbers', result['sum'])

# bar graph for word lengths
# word lenghts calculation
word_len = {}

for logos in words:
    if len(logos) not in word_len:
        word_len.update({len(logos):0})
    if len(logos) in word_len:
        word_len[len(logos)] += 1

# graph alignment
print('-' * hyphen)
head_len = 3  
head_occ = 20 
head_nr = 5  
head_occ_center = 'OCCURRENCES'.center(head_occ)

print(f"{'LEN':>{head_len}}| {head_occ_center} |{'NR.':^{head_nr}}")

print('-' * hyphen)
for length, occurrences in sorted(word_len.items()):
    print(f"{length:>3}| {'*' * occurrences:<20} |{occurrences}")