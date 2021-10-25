"""
Name: Kaki Newsome
lab8.py
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')

    counter = 0
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            sent = str(i) + ' ' + word + '\n'
            outfile.write(sent)
            counter = counter + i
            i += 1

    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')

    for line in infile:
        wage_list = line.split()
        first_name = wage_list[0]
        last_name = wage_list[1]
        hourly_wage = wage_list[2]
        hours_worked = wage_list[3]

        new_pay = (float(hourly_wage) + 1.65) * int(hours_worked)
        out_line = first_name + ' ' + last_name + ' $' + str(new_pay) + '\n'

        outfile.write(out_line)


def isbn(isbn_str):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += int(isbn_str[i]) * pos
    return acc


def send_message(file, friend):
    infile = open(file, 'r')
    outfile = open(friend + '.txt', 'w+')

    for line in infile:
        outfile.write(line)


def send_safe_message(file, friend, key):
    infile = open(file, 'r')
    outfile = open(friend + '.txt', 'w+')

    for line in infile:
        enc_line = encode(line, key) + '\n'
        outfile.write(enc_line)


def send_uncrackable_message(file, friend, pad):
    padfile = open(pad, 'r')
    infile = open(file, 'r')
    outfile = open(friend + '.txt', 'w+')

    padline = padfile.readline()

    for line in infile:
        enc_line = encode_better(line, padline) + '\n'
        outfile.write(enc_line)

    infile.close()
    outfile.close()


def main():
    # number_words('Walrus.txt', 'WalrusOutput.txt')
    # hourly_wages('hourly_wages.txt', 'hourly_wagesOutput.txt')
    # isbn('0072946520')
    # send_message('message.txt', 'Dylan')
    # send_safe_message('secret_message.txt', 'DylanSecret', 5)
    # send_uncrackable_message('safest_message.txt', 'DylanSafest', 'pad.txt')


main()
