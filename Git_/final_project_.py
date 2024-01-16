
from greek_accentuation.accentuation import*                        #οι δύο βιβλιοθήκες που χρησιμοποιούμε για την υλοποίηση
import spacy
import os

def join_katachrestic_diphthongs(word):
    katachrestic_diphthongs = ['ειά', 'ειέ', 'ειό', 'ειού', 'ειώ', 'ιά', 'ιέ','ιώ', 'ιό', 'ιού', 'ιών', 'οιά', 'οιέ', 'οιό',
                               'οιού', 'υά', 'υό', 'υού', 'υώ',
                               'εια', 'ειε', 'ειο', 'ειου', 'ειω', 'ια', 'ιε','ιω', 'ιο', 'ιου', 'ιων', 'οια', 'οιε', 'οιο',
                               'οιου', 'υα', 'υο', 'υου', 'υω']

    syllables = syllabify(word)
    joined_syllables = []                                                       # Χρησιμοποιούμε την συνάρτηση αυτή για να ενώσουμε σε μία συλλαβή τυχόν καταχρηστικούς δίφθογγους που δεν βρίσκονται στην τελευταία συλλαβή,
                                                                                # καθώς η συνάρτηση syllabify που παίρνουμε από την βιβλιοθήκη greek accentuation χωρίζει όλους τους καταχρηστικούς διφθόγγους σε δύο συλλαβές.
                                                                                # Ωστόσο επιθυμούμε η διάσπαση να συμβαίνει μόνο όταν βρίσκονται στην τελευταία συλλαβή αφού σύμφωνα με την γραμματική του Τριανταφυλλίδη για χάρην τονισμού οι καταχρηστικοί δίφθογγοι στη λήγουσα λογίζονατι σα δύο συλλαβές.
    current_syllable = syllables[0]

    for i in range(1, len(syllables)):
        diphthong = current_syllable[-1] + syllables[i][0]  # Check if diphthong
        if diphthong in katachrestic_diphthongs and i < len(syllables) - 1:
            current_syllable += syllables[i]
        else:
            joined_syllables.append(current_syllable)
            current_syllable = syllables[i]

    joined_syllables.append(current_syllable)
    return joined_syllables

def find_accent_position(syllables):
    counter = 0
    thesi = 0                                                    # Αυτή η συνάρτηση διαβάζει μία μία τις συλλαβές κάθε λέξης και μας επιστρέφει τη θέση του τόνου αν αυτός υπάρχει.
                                                                 # Επίσης μας επιστρέφει μια τυχαία τιμή 5 εφόσον εντοπίσει ότι η λέξη έχει δύο τόνους, κάτι που θα είναι ιδιαίτερα χρήσιμο να γνωρίζουμε για τη συνέχεια.
    for i, syllable in enumerate(syllables):

            if 'ά' in syllable:
                thesi = i
                counter = counter+1
            elif 'ύ' in syllable:
                thesi = i
                counter = counter + 1

            elif 'ή' in syllable:
                thesi = i
                counter = counter + 1

            elif 'ό' in syllable:
                thesi = i
                counter = counter + 1

            elif 'έ' in syllable:
                thesi = i
                counter = counter + 1

            elif 'ί' in syllable:
                thesi = i
                counter = counter + 1

            elif 'ώ' in syllable:
                thesi = i
                counter = counter + 1

            elif 'Ά' in syllable:
                thesi = i
                counter = counter + 1

            elif 'Ύ' in syllable:
                thesi = i
                counter = counter + 1

            elif 'Ή' in syllable:
                thesi = i
                counter = counter + 1

            elif 'Ό' in syllable:
                thesi = i
                counter = counter + 1

            elif 'Έ' in syllable:
                thesi = i
                counter = counter + 1

            elif 'Ί' in syllable:
                thesi = i
                counter = counter + 1

            elif 'Ώ' in syllable:
                thesi = i
                counter = counter + 1

    if counter == 1:
        return thesi
    elif counter == 2:
        return 5

def syllable_type(syllables):                            # Αυτή η συνάρτηση έχει την αρμοδιότητα να χαρακτηρίσει τις συλλαβές κάθε λέξης και να τις χωρίσει σε m = μακρόχρονη και v = βραχύχρονη όπου αυτό είναι δυνατό. Αποτυπώνει το αποτέλεσμά της μέσα στη λίστα types.
    for i, syllable in enumerate(syllables):
        if ('ε' in syllable and 'ει' not in syllable and 'έι' not in syllable and 'εί' not in syllable and 'ευ' not in syllable and 'εύ' not in syllable) or ('έ' in syllable and 'ει' not in syllable and 'έι' not in syllable and 'εί' not in syllable and 'ευ' not in syllable and 'εύ' not in syllable) or ('Ε' in syllable and 'Ει' not in syllable and 'Έι' not in syllable and 'Εί' not in syllable and 'Ευ' not in syllable and 'Εύ' not in syllable) or ('Έ' in syllable and 'Ει' not in syllable and 'Έι' not in syllable and 'Εί' not in syllable and 'Ευ' not in syllable and 'Εύ' not in syllable):
            types.append('v')
        elif ('ο' in syllable and 'οι' not in syllable and 'όι' not in syllable and 'οί' not in syllable and 'ου' not in syllable and 'ού' not in syllable) or ('ό' in syllable and 'οι' not in syllable and 'όι' not in syllable and 'οί' not in syllable and 'ου' not in syllable and 'ού' not in syllable) or ('Ο' in syllable and 'Οι' not in syllable and 'Όι' not in syllable and 'Οί' not in syllable and 'Ου' not in syllable and 'Ού' not in syllable) or ('Ό' in syllable and 'Οι' not in syllable and 'Όι' not in syllable and 'Οί' not in syllable and 'Ου' not in syllable and 'Ού' not in syllable):
            types.append('v')
        elif 'ει' in syllable or 'εί' in syllable or 'έι' in syllable or 'Ει' in syllable or 'Εί' in syllable or 'Έι' in syllable:

            types.append('m')
        elif ('οι' in syllable and syllables[-1][-2] != 'ο' and syllables[-1][-1] != 'ι') or ('οί' in syllable and 'οί' not in syllable[-1]) or ('όι' in syllable and syllables[-1][-2] != 'ό' and syllables[-1][-1] != 'ι') or ('Οι' in syllable) or ('Οί' in syllable) or ('Όι' in syllable):
            types.append('m')
        elif ('οι' in syllable and syllables[-1][-2] == 'ο' and syllables[-1][-1] == 'ι') or ('οί' in syllable and syllables[-1][-2] == 'ο' and syllables[-1][-1] == 'ί') or ('όι' in syllable and syllables[-1][-2] == 'ό' and syllables[-1][-1] == 'ι'):
            types.append('v')

        elif 'η' in syllable or 'ή' in syllable or 'Η' in syllable or 'Ή' in syllable:
            types.append('m')
        elif 'ω' in syllable or 'ώ' in syllable or 'Ω' in syllable or 'Ώ' in syllable:
            types.append('m')
        elif ('αι' in syllable and syllables[-1][-2] != 'α' and syllables[-1][-1] != 'ι') or ('αί' in syllable and syllables[-1][-2] != 'α' and syllables[-1][-1] != 'ί') or ('άι' in syllable and syllables[-1][-2] != 'ά' and syllables[-1][-1] != 'ι') or ('Αι' in syllable) or ('Άι' in syllable) or ('Αί' in syllable):
            types.append('m')
        elif ('αι' in syllable and syllables[-1][-2] == 'α' and syllables[-1][-1] == 'ι') or ('αί' in syllable and syllables[-1][-2] == 'α' and syllables[-1][-1] == 'ί') or ('άι' in syllable and syllables[-1][-2] == 'ά' and syllables[-1][-1] == 'ι'):
            types.append('v')

        elif 'υι' in syllable or 'υί' in syllable or 'ύι' in syllable or 'υϊ' in syllable or 'Υι' in syllable or 'Υί' in syllable or 'Ύι' in syllable:
            types.append('m')
        elif 'ου' in syllable or 'ού' in syllable or 'όυ' in syllable or 'οϋ' in syllable or 'Ου' in syllable or 'Ού' in syllable or 'Όυ' in syllable or 'Οϋ' in syllable:
            types.append('m')
        elif 'αυ' in syllable or 'αύ' in syllable or 'άυ' in syllable or 'Αυ' in syllable or 'Αύ' in syllable or 'Άυ' in syllable:
            types.append('m')
        elif 'ευ' in syllable or 'εύ' in syllable or 'έυ' in syllable or 'Ευ' in syllable or 'Εύ' in syllable or 'Έυ' in syllable:
            types.append('m')
        else:
            types.append('-')


def replace_with_vareia(word):                                  # Όπως υποδηλώνει και το όνομά της η συνάρτηση αυτή καλείται όποτε το πρόγραμμα κρίνει ότι μία οξεία πρέπει να αντικατασταθεί από μία βαρεία.
    if 'ά' in word:
        modified_word = word.replace('ά', '\u1F70')
        return modified_word
    elif 'ή' in word:
        modified_word = word.replace('ή', '\u1F74')
        return modified_word
    elif 'ώ' in word:
        modified_word = word.replace('ώ', '\u1F7C')
        return modified_word
    elif 'ί' in word:
        modified_word = word.replace('ί', '\u1F76')
        return modified_word
    elif 'ΐ' in word:
        modified_word = word.replace('ΐ', '\u1FD2')
        return modified_word
    elif 'ύ' in word:
        modified_word = word.replace('ύ', '\u1F7A')
        return modified_word
    elif 'ΰ' in word:
        modified_word = word.replace('ΰ', '\u1FE2')
        return modified_word
    elif 'έ' in word:
        modified_word = word.replace('έ', '\u1F72')
        return modified_word
    elif 'ό' in word:
        modified_word = word.replace('ό', '\u1F78')
        return modified_word
    elif 'Ά' in word:
        modified_word = word.replace('Ά', '\u1FBA')
        return modified_word
    elif 'Έ' in word:
        modified_word = word.replace('Έ', '\u1FC8')
        return modified_word
    elif 'Ό' in word:
        modified_word = word.replace('Ό', '\u1FF8')
        return modified_word
    elif 'Ή' in word:
        modified_word = word.replace('Ή', '\u1FCA')
        return modified_word
    elif 'Ί' in word:
        modified_word = word.replace('Ί', '\u1FDA')
        return modified_word
    elif 'Ύ' in word:
        modified_word = word.replace('Ύ', '\u1FEA')
        return modified_word
    elif 'Ώ' in word:
        modified_word = word.replace('Ώ', '\u1FFA')
        return modified_word

    else:
        return word


def replace_with_perispomeni(word):                               # Παρομοίως, η συνάρτηση αυτή καλείται όταν απαιτηθεί η αντικατάσταση μιας οξείας από μία περισπωμένη.
    if 'άυ' in word:
        return word
    elif 'έυ' in word:
        return word
    elif 'έι' in word:
        return word
    elif 'άι' in word:
        return word
    elif 'όι' in word:
        return word
    elif 'όυ' in word:
        return word
    elif 'ά' in word:
        modified_word = word.replace('ά', '\u1FB6')
        return modified_word
    elif 'ή' in word:
        modified_word = word.replace('ή', '\u1FC6')
        return modified_word
    elif 'ώ' in word:
        modified_word = word.replace('ώ', '\u1FF6')
        return modified_word
    elif 'ί' in word:
        modified_word = word.replace('ί', '\u1FD6')
        return modified_word
    elif 'ΐ' in word:
        modified_word = word.replace('ΐ', '\u1FD7')
        return modified_word
    elif 'ύ' in word:
        modified_word = word.replace('ύ', '\u1FE6')
        return modified_word
    elif 'ΰ' in word:
        modified_word = word.replace('ΰ', '\u1FE7')
        return modified_word
    else:
        return word

def vale_okseia(word):                                            # Η συνάρτηση αυτή μπαίνει σε λειτουργία για να τονίσει με οξεία μονοσύλλαβες λέξεις της νεοελληνικής οι οποίες στο μονοτονικό σύστημα δεν τονίζονται.
    if 'ου' in word:
        modified_word = word.replace('ου', 'ού')
        return modified_word
    elif 'αι' in word:
        modified_word = word.replace('αι', 'αί')
        return modified_word
    elif 'ο' in word:
        modified_word = word.replace('ο', 'ό')
        return modified_word
    elif 'ε' in word:
        modified_word = word.replace('ε', 'έ')
        return modified_word
    elif 'ω' in word:
        modified_word = word.replace('ω', 'ώ')
        return modified_word
    elif 'α' in word:
        modified_word = word.replace('α', 'ά')
        return modified_word
    elif 'ι' in word:
        modified_word = word.replace('ι', 'ί')
        return modified_word
    elif 'η' in word:
        modified_word = word.replace('η', 'ή')
        return modified_word
    elif 'Α' in word:
        modified_word = word.replace('Α', 'Ά')
        return modified_word
    elif 'Ω' in word:
        modified_word = word.replace('Ω', 'Ώ')
        return modified_word


def vale_okseia_dipth(word):                                      # Αντιστοίχως, η συνάρτηση αυτή τίθεται σε λειτουργία για τον τονισμό με οξεία ορισμένων μονοσύλλαβων λέξεων της νέας ελληνικής που δεν τονίζονατι στο μονοτονικό σύστημα
                                                                  # και που λόγω του καταχρηστικού διφθόγγου στη λήγουσα το πρόγραμμά μας τις λογίζει ως δισύλλαβες.
    if 'ια' in word:
        modified_word = word.replace('ια', 'ιά')
        return modified_word
    elif 'ιε' in word:
        modified_word = word.replace('ιε', 'ιέ')
        return modified_word
    elif 'ιο' in word and 'ιοι' not in word:
        modified_word = word.replace('ιο', 'ιό')
        return modified_word
    elif 'ιοι' in word:
        modified_word = word.replace('ιοι', 'ιοί')
        return modified_word
    elif 'ιου' in word:
        modified_word = word.replace('ιου', 'ιού')
        return modified_word
    elif 'υο' in word:
        modified_word = word.replace('υο', 'υό')
        return modified_word
    elif 'εια' in word:
        modified_word = word.replace('εια', 'ειά')
        return modified_word


def vale_perispomeni(word):                                          # Ακολουθώντας την ίδια λογική, η συνάρτηση αυτή τοποθετεί περισπωμένη σε μονοσύλλαβες της νέας ελληνικής οι οποίες στο μονοτονικό δεν τονίζονται.
    if 'αι' in word:
        modified_word = word.replace('αι', 'α\u1FD6')
        return modified_word
    if 'α' in word:
        modified_word = word.replace('α', '\u1FB6')
        return modified_word
    elif 'ει' in word:
        modified_word = word.replace('ει', 'ε\u1FD6')
        return modified_word

    elif 'ου' in word:
        modified_word = word.replace('ου', 'ο\u1FE6')
        return modified_word
    elif 'η' in word:
        modified_word = word.replace('η', '\u1FC6')
        return modified_word
    elif 'ω' in word:
        modified_word = word.replace('ω', '\u1FF6')
        return modified_word
    elif 'υ' in word:
        modified_word = word.replace('υ', '\u1FE6')
        return modified_word

def vale_daseia(word):                                               # Η συνάρτηση εδώ τοποθετεί δασεία στο αρχικό φωνήεν με το οποίο αρχίζει η εκάστοτε λέξη όποτε αυτό απαιτείται.
    if word[0] == 'ο':
        modified_word = '\u1F41' + word[1:]
        return modified_word
    elif word[0] == 'η':
        modified_word = '\u1F21' + word[1:]
        return modified_word
    elif word[0] == 'α':
        modified_word = '\u1F01' + word[1:]
        return modified_word
    elif word[0] == 'ε':
        modified_word = '\u1F11' + word[1:]
        return modified_word
    elif word[0] == 'ι':
        modified_word = '\u1F31' + word[1:]
        return modified_word
    elif word[0] == 'υ':
        modified_word = '\u1F51' + word[1:]
        return modified_word
    elif word[0] == 'ω':
        modified_word = '\u1F61' + word[1:]
        return modified_word
    elif word[0] == 'ό':
        modified_word ='\u1F45' + word[1:]
        return modified_word
    elif word[0] == 'ή':
        modified_word ='\u1F25' + word[1:]
        return modified_word
    elif word[0] == '\u1FC6':
        modified_word ='\u1F27' + word[1:]
        return modified_word
    elif word[0] == 'ά':
        modified_word ='\u1F05' + word[1:]
        return modified_word
    elif word[0] == 'έ':
        modified_word ='\u1F15' + word[1:]
        return modified_word
    elif word[0] == 'ί':
        modified_word = '\u1F35' + word[1:]
        return modified_word
    elif word[0] == 'ύ':
        modified_word ='\u1F55' + word[1:]
        return modified_word
    elif word[0] == 'ώ':
        modified_word ='\u1F65' + word[1:]
        return modified_word
    elif word[0] == 'Ο':
        modified_word = '\u1F49' + word[1:]
        return modified_word
    elif word[0] == 'Η':
        modified_word = '\u1F29' + word[1:]
        return modified_word
    elif word[0] == 'Α':
        modified_word = '\u1F09' + word[1:]
        return modified_word
    elif word[0] == 'Ε':
        modified_word = '\u1F19' + word[1:]
        return modified_word
    elif word[0] == 'Ι':
        modified_word = '\u1F39' + word[1:]
        return modified_word
    elif word[0] == 'Υ':
        modified_word = '\u1F59' + word[1:]
        return modified_word
    elif word[0] == 'Ω':
        modified_word = '\u1F69' + word[1:]
        return modified_word
    elif word[0] == 'Ό':
        modified_word ='\u1F4D' + word[1:]
        return modified_word
    elif word[0] == 'Ή':
        modified_word ='\u1F2D' + word[1:]
        return modified_word
    elif word[0] == 'Ά':
        modified_word ='\u1F0D' + word[1:]
        return modified_word
    elif word[0] == 'Έ':
        modified_word ='\u1F1D' + word[1:]
        return modified_word
    elif word[0] == 'Ί':
        modified_word = '\u1F3D' + word[1:]
        return modified_word
    elif word[0] == 'Ύ':
        modified_word ='\u1F5D' + word[1:]
        return modified_word
    elif word[0] == 'Ώ':
        modified_word ='\u1F6D' + word[1:]
        return modified_word


def vale_daseia_dipth(word):                                             # Τοποθετεί δασεία σε λέξεις που ξεκινούν με δίψηφο φωνήεν. Δεν λαμβάνονται υπόψιν όλοι οι συνδυασμοί καθώς οι λέξεις που παίρνουν δασεία αφορούν περιορισμένες περιπτώσεις οι οποίες είναι γνωστές.
    if word[1] == 'ι':
        modified_word = word[0] + '\u1F31' + word[2:]
        return modified_word
    elif word[1] == 'ί':
        modified_word = word[0] + '\u1F35' + word[2:]
        return modified_word
    elif word[1] == '\u1FD6':
        modified_word = word[0] + '\u1F37' + word[2:]
        return modified_word
    elif word[1] == 'υ':
        modified_word = word[0] + '\u1F51' + word[2:]
        return modified_word
    elif word[1] == 'ύ':
        modified_word = word[0] + '\u1F55' + word[2:]
        return modified_word

def vale_psili_dipth(word):                                               # Χρησιμοποιείται για να τοποθετήσει την ψιλή σε λέξεις που αρχίζουν με δίψηφο φωνήεν.
    if word[1] == 'ι':
        modified_word = word[0] + '\u1F30' + word[2:]
        return modified_word
    elif word[1] == 'ί':
        modified_word = word[0] + '\u1F34' + word[2:]
        return modified_word
    elif word[1] == '\u1FD6':
        modified_word = word[0] + '\u1F36' + word[2:]
        return modified_word
    elif word[1] == 'υ':
        modified_word = word[0] + '\u1F50' + word[2:]
        return modified_word
    elif word[1] == 'ύ':
        modified_word = word[0] + '\u1F54' + word[2:]
        return modified_word
    elif word[1] == '\u1FE6':
        modified_word = word[0] + '\u1F56' + word[2:]
        return modified_word
    elif word[1] == '\u1F76':
        modified_word = word[0] + '\u1F32' + word[2:]
        return modified_word
    elif word[1] == '\u1F7A':
        modified_word = word[0] + '\u1F52' + word[2:]
        return modified_word

def vale_psili(word):                                                     # Καλείται για να βάλει ψιλή σε λέξεις που ξεκινούν με φωνήεν.
    if word[0] == 'ο':
        modified_word = '\u1F40' + word[1:]
        return modified_word
    elif word[0] == 'η':
        modified_word = '\u1F20' + word[1:]
        return modified_word
    elif word[0] == 'α':
        modified_word = '\u1F00' + word[1:]
        return modified_word
    elif word[0] == 'ε':
        modified_word = '\u1F10' + word[1:]
        return modified_word
    elif word[0] == 'ι':
        modified_word = '\u1F30' + word[1:]
        return modified_word

    elif word[0] == 'ω':
        modified_word = '\u1F60' + word[1:]
        return modified_word
    elif word[0] == 'ό':
        modified_word ='\u1F44' + word[1:]
        return modified_word
    elif word[0] == 'ή':
        modified_word ='\u1F24' + word[1:]
        return modified_word
    elif word[0] == '\u1FC6':
        modified_word ='\u1F26' + word[1:]
        return modified_word
    elif word[0] == 'ά':
        modified_word ='\u1F04' + word[1:]
        return modified_word
    elif word[0] == 'έ':
        modified_word ='\u1F14' + word[1:]
        return modified_word
    elif word[0] == 'ί':
        modified_word = '\u1F34' + word[1:]
        return modified_word
    elif word[0] == '\u1FD6':
        modified_word = '\u1F36' + word[1:]
        return modified_word
    elif word[0] == '\u1FB6':
        modified_word = '\u1F06' + word[1:]
        return modified_word
    elif word[0] == '\u1FF6':
        modified_word = '\u1F66' + word[1:]
        return modified_word
    elif word[0] == 'ώ':
        modified_word ='\u1F64' + word[1:]
        return modified_word

    elif word[0] == '\u1F70':
        modified_word ='\u1F02' + word[1:]
        return modified_word
    elif word[0] == '\u1F72':
        modified_word ='\u1F12' + word[1:]
        return modified_word
    elif word[0] == '\u1F74':
        modified_word = '\u1F22' + word[1:]
        return modified_word
    elif word[0] == '\u1F76':
        modified_word = '\u1F32' + word[1:]
        return modified_word
    elif word[0] == '\u1F78':
        modified_word = '\u1F42' + word[1:]
        return modified_word
    elif word[0] == '\u1F7C':
        modified_word = '\u1F62' + word[1:]
        return modified_word


    elif word[0] == 'Ο':
        modified_word = '\u1F48' + word[1:]
        return modified_word
    elif word[0] == 'Η':
        modified_word = '\u1F28' + word[1:]
        return modified_word
    elif word[0] == 'Α':
        modified_word = '\u1F08' + word[1:]
        return modified_word
    elif word[0] == 'Ε':
        modified_word = '\u1F18' + word[1:]
        return modified_word
    elif word[0] == 'Ι':
        modified_word = '\u1F38' + word[1:]
        return modified_word
    elif word[0] == 'Ω':
        modified_word = '\u1F68' + word[1:]
        return modified_word
    elif word[0] == 'Ό':
        modified_word ='\u1F4C' + word[1:]
        return modified_word
    elif word[0] == 'Ή':
        modified_word ='\u1F2C' + word[1:]
        return modified_word
    elif word[0] == 'Ά':
        modified_word ='\u1F0C' + word[1:]
        return modified_word
    elif word[0] == 'Έ':
        modified_word ='\u1F1C' + word[1:]
        return modified_word
    elif word[0] == 'Ί':
        modified_word = '\u1F3C' + word[1:]
        return modified_word
    elif word[0] == 'Ώ':
        modified_word ='\u1F6C' + word[1:]
        return modified_word

    elif word[0] == '\u1FBA':
        modified_word ='\u1F0A' + word[1:]
        return modified_word
    elif word[0] == '\u1FCA':
        modified_word ='\u1F2A' + word[1:]
        return modified_word
    elif word[0] == '\u1FDA':
        modified_word ='\u1F3A' + word[1:]
        return modified_word
    elif word[0] == '\u1FFA':
        modified_word ='\u1F6A' + word[1:]
        return modified_word
    elif word[0] == '\u1FC8':
        modified_word = '\u1F1A' + word[1:]
        return modified_word
    elif word[0] == '\u1FF8':
        modified_word ='\u1F4A' + word[1:]
        return modified_word


def check_for_patterns(input_list, patterns):                              # Αυτή η συνάρτηση χρησιμοποιείται για να ελέγξει τη λίστα output στην περίπτωση που περιέχει τις λέξεις 'ό,τι'/'Ό,τι'.                 
    found_patterns = []

    for i in range(len(input_list) - len(patterns) + 1):
        if input_list[i:i + len(patterns)] == patterns:
            found_patterns.append(''.join(patterns))

    return found_patterns




accent = []                             # Λίστα στην οποία η συνάρτηση find_accent_position αποθηκεύει τον αριθμό των τόνων που ανιχνεύει στην εκάστοτε λέξη.
types = []                              # Λίστα στην οποία αποθηκεύονται τα αποτελέσματα που προκύπτουν από τη συνάρτηση syllable_types.
lemma = []                              # Λίστα στην οποία αποθηκεύεται το λήμμα κάθε λέξης όπως προκύπτει από την spacy
cases = []                              # Λίστα στην οποία καταχωρείται ένας χαρακτηριστικός αριθμός για κάθε λέξη με βάση τον οποίο γίνεται ο διαχωρισμός των λέξεων όσον αφορά τη συλλαβή που τονίζονται.
output = []                             # Εδώ αποθηκεύονται οι λέξεις που προκύπτουν μετά τους ελέγχους και την τοποθέτηση του κατάλληλου τόνου αλλά πριν την τοποθέτηση πνεύματος.
values=[]                               # Σε συτή τη λίστα αποθηκεύονται οι ετικέτες που χαρακτηρίζουν τι μέρος του λόγου είναι η κάθε λέξη με βάση την ανάλυση της spacy.
eksaireseis_perispomenis = ['μήτε', 'είτε', 'ώστε', 'ούτε', 'είθε','Μήτε', 'Είτε', 'Ώστε', 'Ούτε', 'Είθε']
ktitikes_antonumies = ['μου','σου','του','της','μας','σας','τους']
monosyllabes_gia_perispomeni = ['μου','σου','του','της','μας','σας','των','τω','βγω','βγεις','βγει','βγουν','γη','γης','δρω','δρας','δρα','δρουν','δρυς','δρυ','δω','δεις','δει','δουν','ζω','ζεις','ζει','ζουν','μπω','μπεις','μπει','μπουν','μυς','μυ','νους','νου','παν','πλους','πλου','πυρ','ρους','ρου','συν','τρεις','φως','φταις','κλαις','πω','πεις','πει','πουν','πιω','πιεις','πιει','πιουν','σκας','φας','τρως','πας','βρω','βρεις','βρει','βρουν','καις',
                                'Μου','Σου','Του','Της','Μας','Σας','Των','Τω','Βγω','Βγεις','Βγει','Βγουν','Γη','Γης','Δρω','Δρας','Δρα','Δρουν','Δω','Δεις','Δει','Δουν','Ζω','Ζεις','Ζει','Ζουν','Μπω','Μπεις','Μπει','Μπουν','Μυς','Μυ','Νους','Νου','Παν','Πλους','Πλου','Πυρ','Ρους','Ρου','Συν','Τρεις','Φως','Φταις','Κλαις','Πω','Πεις','Πει','Πουν','Πιω','Πιεις','Πιει','Πιουν','Σκας','Φας','Τρως','Πας','Βρω','Βρεις','Βρει','Βρουν','Καις']
monosyllabes_gia_okseia = ['την','τη','στη','το','τον','τους','τις','τα','που','πως','στο','στα','στους','στον','στην','στις','αν','ας','γκρι','δα','δε','δεν','δη','δις','θα','και','καν','μα','με','μεν','μες','μη','μην','μπας','μπα','μπεζ','μπλε','μπρος','μωβ','να','ναι','ντε','ον','πα','πλην','πριν','προ','προς','ροζ','σα','σαν','σε','συ','τι','τρις','χθες','χτες','ψες','αχ','βρε','κιχ','μπαμ','ουστ','ουφ','ρε','σουτ','φτου','χα','ωχ','βγες','πες','δες','μπες','λες','θες','βρες',
                           'Την','Τη','Στη','Το','Τον','Τους','Τις','Τα','Που','Πως','Στο','Στα','Στους','Στον','Στην','Στις','Αν','Ας','Γκρι','Δα','Δε','Δεν','Δη','Δις','Θα','Και','Καν','Μα','Με','Μεν','Μες','Μη','Μην','Μπας','Μπα','Μπεζ','Μπλε','Μπρος','Μωβ','Να','Ναι','Πλην','Πριν','Προ','Προς','Ροζ','Σα','Σαν','Σε','Συ','Τι','Τρις','Χθες','Χτες','Ψες','Αχ','Βρε','Κιχ','Μπαμ','Ουστ','Ουφ','Ρε','Σουτ','Φτου','Χα','Ωχ','Βγες','Πες','Δες','Μπες','Λες','Θες','Βρες']
disyllabes_gia_okseia = ['βια','βιος','βιους','βιοι','γεια','για','γιος','γιο','γιε','γιοι','γιους','δυο','μια','μιας','πια','πιο','ποιος','ποια','ποιο','ποιον','ποιες','ποιοι','ποιους','ποιες','πιες',
                         'Βια','Βιος','Γεια','Για','Γιος','Γιο','Γιε','Γιοι','Γιους','Δυο','Μια','Μιας','Πια','Πιο','Ποιος','Ποια','Ποιο','Ποιον','Ποιες','Ποιοι','Ποιους','Ποιες','Πιες']
nlp = spacy.load("el_core_news_lg")                                   # Φορτώνουμε το επιθυμητό μοντέλο της spacy με βάση το οποίο θα γίνει η ανάλυση.
text = input("Παρακαλώ εισάγετε το κείμενό σας: ")
doc = nlp(text)                                                       # Δίνουμε στην spacy το κείμενό μας.
sentences = list(doc.sents)                                           # Χωρίζουμε το κείμενο σε προτάσεις για να διευκολύνουμε την ανάλυση.
for sentence in sentences:
    doc1 = nlp(sentence.text)                                         # Ανάλυση ανά πρόταση
    for i, first_token in enumerate(doc1):
        final_form = first_token.text                                 # Η μεταβλητή .text είναι το string δηλαδή η εκάστοτε λέξη.
        case= 0
        values.append(first_token.pos_)                               # Η μεταβλητή .pos είναι η ετικέτα με το μέρος του λόγου
        lemma.append(first_token.lemma_)                              # Η μεταβλητή .lemma είναι το λήμμα κάθε λέξης
        joined_syllables = join_katachrestic_diphthongs(first_token.text)

        #print(first_token.text, first_token.pos_, first_token.morph, first_token.lemma_, first_token.ent_type_)         # Εκτυπώνουμε την πλήρη ανάλυση που μας προσφέρει η spacy ώστε να έχουμε καλύτερη εικόνα σε περίπτωση που κάνει λάθος.
                                                                                                                        # Η .morph μας παρέχει πληροφορία σχετικά με την κλίση, το γένος, τον αριθμό της λέξης ενώ η .ent_type_ δίνει ετικέτα σε πρόσωπα και τοποθεσίες.
        accent_position = find_accent_position(joined_syllables)
        accent.append(accent_position)
        #print(accent)
        if accent_position == len(joined_syllables) - 1:
            #print("Η λέξη τονίζεται στη λήγουσα.")
            case = 1
            cases.append('1')
        elif accent_position == len(joined_syllables) - 2:
            #print("Η λέξη τονίζεται στην παραλήγουσα.")
            case = 2
            cases.append('-')

        elif first_token.pos_ != 'PUNCT' and len(joined_syllables) <= 2:
            #print('Κανένας τόνος και δεν είναι σημείο στίξης.')
            case = 4
            cases.append('4')
        else:
            cases.append('-')



        if len(joined_syllables) > 0 and len(joined_syllables[-1]) == 1:
            # Προσθήκη δύο κενών στο τελευταίο string για την αποφυγή error στις συνθήκες που παίρνουμε παρακάτω, δεν επηρεάζει σε κάποιο βαθμό την ανάλυση.
            joined_syllables[-1] += "  "


        k= syllable_type(joined_syllables)
        #print(joined_syllables)
        #print(types)

        if case == 1:                                                                   # Λαμβάνουμε τις περιπτώσεις για λέξεις που τονίζονται στη λήγουσα και πρέπει να αντικατασταθεί ο τόνος τους με περισπωμένη.
            if final_form in ['πού','πώς','Πού','Πώς','εμάς','εσάς','Εμάς','Εσάς']:
                final_form = replace_with_perispomeni(final_form)
            if ('είς' in joined_syllables[-1]) and (first_token.pos_ == 'NOUN' or first_token.pos_ == 'ADJ' or first_token.pos_ == 'PRON'):
                final_form = replace_with_perispomeni(first_token.text)
            if (first_token.ent_type_ == 'PERSON' and 'ά' in joined_syllables[-1]) or (first_token.text in ['Ιησούς','Ιησού','Αθηνά','Αθηνάς','Ναυσικάς','Ναυσικά','Απελλή','Απελλής','Ερμή','Ερμής','Ηρακλή','Ηρακλής','Θαλή','Θαλής','Θεμιστοκλή','Θεμιστοκλής','Μωυσή','Μωυσής','Περικλή','Περικλής']):
                final_form = replace_with_perispomeni(final_form)
            if (first_token.pos_ == 'NOUN' or first_token.pos_ == 'ADJ') and ('Case=Gen' in first_token.morph):
                final_form = replace_with_perispomeni(final_form)
            if (types[-1] == 'm') and (first_token.pos_ == 'ADV') and (first_token.text not in ['πού','πώς','ειδεμή','παμψηφεί','καθώς','Πού','Πώς','Ειδεμή','Παμψηφεί','Καθώς']):
                final_form = replace_with_perispomeni(final_form)
            if (first_token.pos_ == 'VERB' and types[-1] == 'm') or (first_token.pos_ == 'VERB' and 'ά' in joined_syllables[-1]):
                final_form = replace_with_perispomeni(final_form)



        elif case == 2:                                                 # Εξετάζονται όλες οι περιπτώσεις για λέξεις που τονίζονται στη παραλήγουσα και πρέπει να τονιστούν με περισπωμένη.
            if types[-2] == 'm' and types[-1] == 'v' and final_form not in eksaireseis_perispomenis:
                final_form = replace_with_perispomeni(first_token.text)
            if final_form == 'τοίχοι' or final_form == 'οίκοι' or final_form == 'κοίλοι' or final_form == 'οίκτοι' or final_form == 'Τοίχοι' or final_form == 'Οίκοι' or final_form == 'Κοίλοι' or final_form == 'Οίκτοι' or final_form in ['Κωνσταντίνος','Κωνσταντίνο']:
                final_form = replace_with_perispomeni(first_token.text)
            if (types[-2] == 'm') and (first_token.pos_ == 'NOUN' or first_token.pos_ == 'ADJ' or first_token.pos_ == 'PRON') and ('Gender=Neut' in first_token.morph) and ('α' in joined_syllables[-1]) and ('αυ' not in joined_syllables[-1]) and ('αι' not in joined_syllables[-1]):
                final_form = replace_with_perispomeni(first_token.text)
            if ('α' in joined_syllables[-1] and 'αι' not in joined_syllables[-1] and 'αυ' not in joined_syllables[-1]) and (first_token.pos_ == 'VERB') and ('Mood=Imp' not in first_token.morph) and (types[-2] == 'm'):
                final_form = replace_with_perispomeni(first_token.text)
            if (first_token.pos_ == 'VERB') and (first_token.text[-1] == 'ε' and first_token.text[-2] in ['ν','μ','τ'] and first_token.text[-3] == 'ά'):
                final_form = replace_with_perispomeni(first_token.text)
            if (first_token.text[-1] == 'ι' and first_token.text[-2] == 'α' and first_token.text[-3] in ['μ','σ','τ'] and first_token.text[-4] == 'ά'):
                final_form = replace_with_perispomeni(first_token.text)


        elif case==4:                                         # Εδώ λαμβάνονται υπόψιν όλες οι περιπτώσεις μονοσύλλαβων που δεν τονίζονται στο μονοτονικό και κρίνεται το αν θα πρέπει να τονιστούν καθώς και τι είδος τόνου θα πάρουν.
            if (values[i-1] == 'NOUN' or values[i-1] == 'PROPN') and (first_token.text in ktitikes_antonumies):
                final_form = first_token.text
            elif (accent[i-1] == 5) and (first_token.text in ktitikes_antonumies):
                final_form = first_token.text
            elif first_token.text in monosyllabes_gia_okseia:
                final_form = vale_okseia(first_token.text)
            elif first_token.text in disyllabes_gia_okseia:
                final_form = vale_okseia_dipth(first_token.text)
            elif first_token.text in monosyllabes_gia_perispomeni:
                final_form = vale_perispomeni(first_token.text)


        types = []
        output.append(final_form)

pattern1_to_find =['ό', ',', 'τί']                                 # Ειδική συνθήκη για τη λέξη 'ό,τι' καθώς εμπεριέχει κόμμα και το πρόγραμμά μας το διαβάζει σαν τρεις λέξεις.
pattern2_to_find =['Ό', ',', 'τί']
found_pattern1 = check_for_patterns(output, pattern1_to_find)
found_pattern2 = check_for_patterns(output, pattern2_to_find)


final_output = []                              # Σε αυτή τη λίστα θα αποθηκεύσουμε την τελική μορφή που θα πάρει η λέξη μετά την επεξεργασία από το πρόγραμμά μας.
for i in range(1,len(output)):         # Αφού έχουμε διακρίνει τις λέξεις που τονίζονται με οξεία στη λήγουσα, εδώ κάνουμε τον έλεγχο για το αν θα πρέπει να αντικατασταθεί η οξεία από την βαρεία.
    if (cases[i-1] == '1' or cases[i-1] == '4') and (values[i] != 'PUNCT' and output[i] not in ['μου','σου','του','μας','σας','τον','την','το','τη','των','τους','τις','τες','τα']) and ('ώ' in output[i-1] or 'έ' in output[i-1] or 'ά' in output[i-1] or 'ή' in output[i-1] or 'ύ' in output[i-1] or 'ί' in output[i-1] or 'ό' in output[i-1] or 'Ά' in output[i-1] or 'Ώ' in output[i-1] or 'Έ' in output[i-1] or 'Ύ' in output[i-1] or 'Ό' in output[i-1] or 'Ή' in output[i-1] or 'Ί' in output[i-1]):
        #print('Η λέξη παίρνει βαρεία')
        output[i-1]= replace_with_vareia(output[i-1])

                           # Η παρακάτω λίστα περιέχει όλες τις γνωστές λέξεις που παίρνουν δασεία με βάση τη γραμματική του Μ. Τριανταφυλλίδη καθώς και κάποιες από τις πιο συνήθεις παράγωγές τους. Σε περιπτώσεις που έχουν συμπεριληφθεί όλα π.χ. τα γένη μιας λέξης είναι επειδή ο lemmatizer της spacy δεν είναι ιδιαίτερα αξιόπιστος, με αποτέλεσμα σε πολλές περιπτώσεις να μην αναγνωρίζει λέξεις από την ίδια οικογένεια λέξεων.
list_for_daseia=['αβρός','αβρή','αβρό','αβροί','αβρά','άγιος','άγια','άγιο','αγνός','αγνή','αγνό','Άδης','Άδη','αδρός','αδρά','αδρή','αδρό','αδροί','αίμα','Α'+'\u1FD6'+'μος','Α'+'\u1FD6'+'μο','αίρεση','αιρετός','αλάτι','Αλιάκμονας','Αλιάκμονα','αλιεία','Αλικαρνασσός','Αλικαρνασσό','Αλικαρνασσ'+'\u1F78'+'ς','Αλικαρνασσ'+'\u1F78','αλίπαστο','αλίπεδο','άλμα','Αλόννησος','Αλόννησο','αλτήρες','αλτήρας','αλυκή','αλυσίδα','αλώνι','άλωση','άμα','Αμαδρυάδες','αμάξι','άμαξα','αμαξάκι','αμαξωτός','αμαξιάτικα','αμαξοστάσιο','αμαξοστοιχία','αμαρτάνω','άμιλλα','απαλός','απαλά','απλός','απλά','άρμα','άρμη','αρμόζω','αρμός','αρπάζω','αφή','αψίδα','αψίθυμος','αψίκορος','εαυτός',
                 'έβδομος','Εβρα'+'\u1FD6'+'ος','Εβρα'+'\u1FD6'+'οι','Εβρα'+'\u1FD6'+'ο','Έβρος','Έβρο','έδρα','είλωτας','είλωτες','ειμαρμένη','ειρκτή','ειρμός','Εκάβη','Εκάβης','Εκάτη','Εκάτης','εκατό','Έκτορας','Έκτορα','Ελένη','Ελένης','έλικας','Ελικώνας','Ελικώνα','έλκος','ελκύω','Έλλη','Έλλης','Έλληνας','Έλληνα','έλος','ένας','έντεκα','ενώνω','έξι','έρμαιο','έρμαια','έρμαιος','ερμαφρόδιτος','ερμαφρόδιτη','εκατομμύριο','Εκατομμύριο','ενικός','Ενικός','εβδομάδα','Εβδομάδα','Εξήντα','εξήντα','εξακόσια','Εξακόσια',
                  'ερμαφρόδιτα','ερμηνεύω','Ερμ'+'\u1FC6'+'ς','Ερμιόνη','Ερμιόνης','έρπω','εσμός','εσπερινός','εστία','εστιατόριο','ετα'+'\u1FD6'+'ρος','εταίρα','έτοιμος','έτοιμα','έτοιμοι','ευρετήριο','εφτά','ήβη','ηγεμόνας','ηγεμονία','ηγούμενος','ηδονή','ηλικία','ήλιος','ημέρα','ήμερος','ήμερα','ήμερη','ήμερο','ηνίοχος','ήπατα','Ήρα','Ήρας','Ηρακλ'+'\u1FC6'+'ς','Ηρακλ'+'\u1FC6','Ηρόδοτος','Ηρόδοτο','ήρωας','ηρωίδα','Ησίοδος','Ησίοδο','ήσυχος','ήσυχοι','Ήφαιστος','Ήφαιστο','ιδρύω','ιδρώτας','ιερός','ιερή','Ιερουσαλήμ','Ιερουσαλ'+'\u1F74'+'μ','ικανός','ικετεύω','ιλαρός','ίλεος','ίλερη','ιμάτιο','ιππικό','ιστορία','ιστός','ιστοί','οδηγός','οδός','όλμος','ολόκληρος','όλος','ομάδα','ομαλός','όμηρος','Όμηρος','Όμηρο','ομιλία','όμιλος','ομίχλη','όμοιος','όμως','οι','οπλή','όπλο','όποιος','οποίος','όποτε','όπου','όπως','όραση','ορίζω','όριο','όρκος','όρμος','όρος','όρη','όσιος','οσία','όσιο','όσια','όσος','όση','όσο','όσοι','όταν','ότι','ώρα','ωραίος','ώριμος','ως',
                  'εξ'+'\u1FC6'+'ς','Εξ'+'\u1FC6'+'ς','αμαρτία','Αμαρτία','ήττα','ημεδαπός','Ήττα','Ημεδαπός','Ιποκράτης','Ιποκράτη','Ολλανδία','Ολλανδίας','αρπαγή','Αρπαγή','ένωση','Ένωση','ερπετό','Ερπετό','ηδονίζομαι','Ηδονίζομαι','ησυχάζω','Ησυχάζω','ίδρυση','Ίδρυση','ιδρώνω','Ιδρώνω','ικεσία','Ικεσία','ιππότης','Ιππότης','Οδεύω','οδεύω','οπότε','Οπότε','ωρολόγιο','Ωρολόγιο','ωροδείκτης','Ωροδείκτης','ωρολόγιο','Ωρολόγιο','ώστε','Ώστε','ομηρία','Ομηρία','ωριμάζω','Ωριμάζω','ερμηνεία','Ερμηνεία','εύρεση','Εύρεση','ικανότητα','Ικανότητα','ίππος','Ίππος','ιστορικός','Ιστορικός','ηρωικός','Ηρωικός','ομιλητικός','Ομιλητικός','ομαλότητα','Ομαλότητα','ομιχλώδης','Ομιχλώδης','ηττημένος','Ηττημένος','Ωριμότητα','ωριμότητα','ετοιμότητα','Ετοιμότητα','οδηγία','Οδηγία','ημερήσιος','Ημερήσιος','οδηγώ','Οδηγώ','εδρεύω','Εδρεύω','έρπειν','Έρπειν','ετοιμάζω','Ετοιμάζω','ετοιμασία','Ετοιμασία','αφήνω','Αφήνω','εστίαση','Εστίαση','εστιάζω','Εστιάζω','ερμηνεία','Ερμηνεία','Ερμηνευτής','ερμηνευτής','έλξη','Έλξη','ηλικιωμένος','Ηλικιωμένος','ηλιοφάνεια','Ηλιοφάνεια','ηλιαχτίδα','Ηλιαχτίδα','ήπατος','Ήπατος','ηνία','Ηνία','ημερήσιος','Ημερήσιος','Ημερίδα','ημερίδα','ολομέλεια','Ολομέλεια','οπλίζω','Οπλίζω','ορμητικό','Ορμητικό','απλουστεύω','Απλουστεύω','απλότητα','Απλότητα','αλωνίζω','Αλωνίζω',
                 'Αβρός','Αβρή','Αβρό','Αβροί','Αβρά','Άγιος','Άγια','Άγιο','Αγνός','Αγνή','Αγνό','Αδρός','Αδρά','Αδρή','Αδρό','Αδροί','Αίμα','Α'+'\u1FD6'+'μα','Αίρεση','Αιρετός','Αλάτι','Αλιεία','Αλίπαστο','Αλίπεδο','Άλμα','Αλτήρες','Αλτήρας','Αλυκή','Αλυσίδα','Αλώνι','Άλωση','Άμα','Αμάξι','Άμαξα','Αμαξάκι','Αμαξωτός','Αμαξιάτικα','Αμαξοστάσιο','Αμαξοστοιχία','Αμαρτάνω','Άμιλλα','Απαλός','Απαλά','Απλός','Απλά','Άρμα','Άρμη','Αρμόζω','Αρμός','Αρπάζω','Αφή','Αψίδα','Αψίθυμος','Αψίκορος','Εαυτός','ωρών','Ωρών','ησύχως','Ησύχως',
                 'Έβδομος','Έδρα','Είλωτας','Είλωτες','Ειμαρμένη','Ειρκτή','Ειρμός','Εκατό','Έλικας','Έλκος','Ελκύω','Έλος','Ένας','Έντεκα','Ενώνω','Έξι','Έρμαιο','Έρμαια','Έρμαιος','Ερμαφρόδιτος','Ερμαφρόδιτη',
                 'Ερμαφρόδιτα','Ερμηνεύω','Έρπω','Εσμός','Εσπερινός','Εστία','Εστιατόριο','Ετα'+'\u1FD6'+'ρος','Εταίρα','Έτοιμος','Έτοιμα','Έτοιμοι','Ευρετήριο','Εφτά','Ήβη','Ηγεμόνας','Ηγεμονία','Ηγούμενος','Ηδονή','Ηλικία','Ήλιος','Ημέρα','Ήμερος','Ήμερα','Ήμερη','Ήμερο','Ηνίοχος','Ήπατα','Ήρωας','Ηρωίδα','Ήσυχος','Ήσυχοι','Ιδρύω','Ιδρώτας','Ιερός','Ιερή','Ικανός','Ικετεύω','Ιλαρός','Ίλεος','Ίλερη','Ιμάτιο','Ιππικό','Ιστορία','Ιστός','ιστοί','Οδηγός','Οδός','Όλμος','Ολόκληρος','Όλος','Ομάδα','Ομαλός','Ομιλία','Όμιλος','Ομίχλη','Όμοιος','Όμως','Οι','Οπλή','Όπλο','Όποιος','Οποίος','Όποτε','Όπου','Όπως','Όραση','Ορίζω','Όριο','Όρκος','Όρμος','Όρος','Όρη','Όσιος','Οσία','Όσιο','Όσια','Όσος','Όση','Όσο','Όσοι','Όταν','Ότι','Ό,τι','Ώρα','Ωραίος','Ώριμος','Ως']

dipsifa=['ι','υ','ί','ύ','\u1FD6','\u1FE6','ϋ','ϊ','\u1FD3','\u1FE3','\u1F76','\u1F7A','\u1FD7','\u1FE7','\u1FD3','\u1FE3']                      # Περιέχει όλα τα πιθανά δεύτερα συνθετικά ενός δίψηφου φωνήεντος.
vowels = ['α', 'ε', 'η', 'ι', 'ο', 'υ', 'ω','ά','έ','ή','ί','ό','ύ','ώ','\u1FB6','\u1FC6','\u1FD6','\u1FE6','\u1FF6','\u1F70','\u1F72','\u1F74','\u1F76','\u1F78','\u1F7A','\u1F7C','Α', 'Ε', 'Η', 'Ι', 'Ο', 'Υ', 'Ω','Ά','Έ','Ή','Ί','Ό','Ύ','Ώ','\u1FBA','\u1FCA','\u1FDA','\u1FEA','\u1FFA','\u1FC8','\u1FF8']       # Περιέχει όλα τα πιθανά φωνήεντα με τα οποία μπορεί να ξεκινάει μία λέξη.
for i,word in enumerate(output):
    if word in ['ο','Ο','η','Η']:                       # Μονοψήφια για δασεία λαμβάνονται ξεχωριστά.
        telos = vale_daseia(word)
        final_output.append(telos)
    elif found_pattern1 and word == '\u1F78':           # Ειδική συνθήκη για χειρισμό της λέξης 'ό,τι' αν υπάρχει.
        final_output.append('\u1F45,τι')
        output[i:i+3] = [''.join(output[i:i+3])]
    elif found_pattern2 and word == '\u1FF8':           # Ειδικές συνθήκες για χειρισμό των λέξεων 'ό,τι'/'Ό,τι' αν υπάρχουν.
        final_output.append('\u1F4D,τι')
        output[i:i+3] = [''.join(output[i:i+3])]

    elif word in ['ή','Ή','\u1F74','\u1FCA']:           # Μονοψήφια για ψιλή λαμβάνονται ξεχωριστά.
        telos = vale_psili(word)
        final_output.append(telos)

    elif word == 'Ήττες':
        telos = '\u1F2F' + word[1:]
        final_output.append(telos)               # Τρεις ιδιάζουσες περιπτώσεις λέξεων με βάση τη δομή του προγράμματός μας που πρώτα τοποθετεί τόνο και μετά εξετάζει την λέξη για πνεύμα.

    elif word == 'Ώρες':
        telos = '\u1F6F' + word[1:]
        final_output.append(telos)

    elif word in ['Ώμος','Ώμοι']:
        telos = '\u1F6E' + word[1:]
        final_output.append(telos)


    elif (word[0] in ['η','Η','ή','Ή'] and word[1] == 'μ' and word[2] in ['ι','ί']) or (word[0] in ['ο','Ο','ό','Ό'] and word[1] == 'μ' and word[2] in ['ο','ό']) or (word[0] in ['ο','Ο','ό','Ό'] and word[1] == 'π' and word[2] == 'λ'):                  # Ελέγχει για δασεία όλες τις λέξεις που ξεκινούν από ομο- , ημι- , οπλ-
        telos = vale_daseia(word)
        final_output.append(telos)



    elif word[0] in vowels and word[1] in dipsifa:
        if (word in list_for_daseia) or (lemma[i] in list_for_daseia) or (word[0] in ['Υ','υ','Ύ','ύ'] and word[1] in ['ι','ί']):                     # Έλεγχος για τοποθέτηση δασείας ή ψιλής σε λέξεις που ξεκινούν από δίψηφο φωνήεν.
            telos = vale_daseia_dipth(word)
            final_output.append(telos)

        else:
            telos = vale_psili_dipth(word)
            final_output.append(telos)


    elif (word[0] in vowels) and word not in ['οπότε','Οπότε']:                                                                                        # Έλεγχος για τοποθέτηση δασείας ή ψιλής σε λέξεις που αρχίζουν από φωνήεν.(ιδιάζουσα περίπτωση το 'οπότε' που παρόλο που δεν υπάρχει στη λίστα για δασεία το πρόγραμμα το εμφάνιζε με δασεία)
            if (word in list_for_daseia) or (lemma[i] in list_for_daseia) or (word[0] in ['Υ', 'υ', 'Ύ', 'ύ']):
                telos = vale_daseia(word)
                final_output.append(telos)
            else:
                telos = vale_psili(word)
                final_output.append(telos)
    elif word in ['οπότε','Οπότε']:
        telos = vale_psili(word)
        final_output.append(telos)
    else:
        final_output.append(word)


result = " ".join(final_output)# Τυπώνουμε το τελικό αποτέλεσμα!!
print('\n\n')
print(result)
os.system('pause')

