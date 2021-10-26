"""
Name: Kaki Newsome
File: weighted_average.py

This program finds the weighted average for a student from a text file.

Certification of Authenticity:
I certify this assignment is entirely my own.
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    for line in in_file:
        half_line = line.split(':')
        sec_half = half_line[1]

        sec_half = sec_half.split()

        weight_acc = 0
        wgacc = 0

        for i in range(0, len(sec_half) - 1, 2):
            wgmult = int(sec_half[i]) * int(sec_half[i + 1])
            wgacc = wgmult + wgacc
            weight_acc = weight_acc + int(sec_half[i])

        if weight_acc > 100:
            line = half_line[0] + "'s" + " average: " + "Error: The weights are more than 100.\n"
        elif weight_acc < 100:
            line = half_line[0] + "'s" + " average: " + "Error: The weights are less than 100.\n"
        else:
            stud_avg = wgacc / 100
            line = half_line[0] + "'s" + " average: " + str(round(stud_avg, 1)) + '\n'

        out_file.writelines(line)

    in_file.close()
    out_file.close()


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    main()
