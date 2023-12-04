import os

def word_to_num(parola):
    numeri_parole = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for chiave, valore in numeri_parole.items():
        if chiave in parola:
            return valore
    return parola


def read_caldoc(file_path):
    with open(file_path, 'r') as file:
        total = 0
        for row in file:
            num1 = ""
            num2 = ""

            # Scorrimento da sinistra verso destra
            for char in row:
                if char.isdigit():
                    num1 = char
                    break
                else:
                    num1 += char
                    num1 = word_to_num(num1)
                    if num1.isdigit():
                        break

            # Scorrimento da destra verso sinistra
            for char in reversed(row):
                if char.isdigit():
                    num2 = char
                    break
                else:
                    num2 = char + num2
                    num2 = word_to_num(num2)
                    if num2.isdigit():
                        break

            num_full = num1 + num2
            # print(numero_completo)
            total += int(num_full)
        
        print("The sum of all of the calibration values is: " + str(total))


if __name__ == "__main__":
    read_caldoc(os.path.join(os.path.dirname(os.path.abspath(__file__)), "day01.txt"))
