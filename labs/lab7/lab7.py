"""
Name: Kaki Newsome
lab7.py
"""

def cash_conversion():
    num = eval(input("Enter a number: "))
    print("${:.2f}".format(num))  # :x.y x is in front of dec, y is after

def encode():
    sent = input("Enter a sentence to be encoded: ")
    key_val = eval(input("Enter the integer key value: "))
    acc = ''

    for ch in sent:
        enc_ch = ord(ch) + key_val
        uncoded_ch = chr(enc_ch)
        acc = acc + uncoded_ch
    print(acc)

def sphere_area(radius):
    area = 4 * 3.14 * radius ** 2
    return area

def sphere_volume(radius):
    volume = (4 / 3) * 3.14 * radius ** 3
    return volume

def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i
    return total

def sum_n_cubes(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i ** 3
    return total

def encode_better():
    sent = input("Enter a sentence to be encoded: ")
    key = input("Enter a another sentence equal or longer than the encoded sentence: ")
    acc = ''

    for i in range(len(sent)):
        encod_ch = ord(sent[i])
        encod_key = ord(key[i])
        x = encod_ch + encod_key - 97
        acc = acc + chr(x)
    print(acc)


def main():
    # cash_conversion()
    # encode()
    # print(sphere_area(5))
    # print(sphere_volume(5))
    # print(sum_n(5))
    # print(sum_n_cubes(5))
    # encode_better()



main()
