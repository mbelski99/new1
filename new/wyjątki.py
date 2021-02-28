try:
    txt_file = open('plik.txt', 'w')
    txt_file.write('Wynik dzielenia: ')
    division_result = int(input('dzielna: ')) / int(input('dzielnik: '))
    txt_file.write(str(division_result))
    txt_file.close()
except (IOError, ZeroDivisionError) as e:
    print(e)