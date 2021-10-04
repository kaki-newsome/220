"""
Name: Kaki Newsome
lab6.py
"""


def name_reverse():
    first_last = input("Enter your first and last name: ")
    split_first_last = first_last.split()

    print(split_first_last[-1] + ",", split_first_last[0])

def company_name():
    website = input("Enter website: ")
    split_web = website.split('.')

    print(split_web[1])

def initials():
    num_students = eval(input("Enter number of students: "))

    for i in range(1,num_students + 1):
        first_name = input("Enter first name of student " + str(i) + ": ")
        last_name = input("Enter " + first_name + "'s last name: ")
        print(first_name + "'s initials are", first_name[0] + last_name[0])

def names():
    names_string = input("Enter a list of names separated by a comma: ")
    names_list = names_string.split(',')
    acc = ''

    for name in names_list:
        split_name = name.split()
        first_name = split_name[0]
        last_name = split_name[1]
        acc = acc + first_name[0] + last_name[0] + ' '
    print("the initials are", acc)

def thirds():
    num_sent = eval(input("Enter number of sentences: "))
    for i in range(1, num_sent + 1):
        sent = input("Enter sentence " + str(i) + ": ")
        print(sent[::3])

def word_average():
    sentence = input("Enter a sentence: ")
    sentence = sentence.split()
    acc = 0

    for word in sentence:
        acc += len(word)

    avg = acc / len(sentence)
    print(avg)

def pig_latin():
    sentence = input("Enter a sentence: ")
    sentence = sentence.lower()
    sentence = sentence.split()
    acc = ''

    for word in sentence:
        x = word[1:]
        x = x + word[0] + 'ay'
        acc = acc + x + ' '
    print(acc)

def main():
    # name_reverse()
    # add other function calls here
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()


main()