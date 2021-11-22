operator = ''


with open('odds.txt', 'r', encoding="utf-8") as rf:
    for line in rf:
        new_line = line.split('>>')
        name = new_line[0]
        odd_1 = new_line[1]
        odd_2 = new_line[2]
        odd_3 = new_line[3]
        odd_2 = odd_2.replace('%', '')
        odd_3 = odd_3.replace('%', '')
        odd_3 = int(odd_3)/100
        if odd_3 >= 0.8:
            print(name, odd_1, odd_2, odd_3)
