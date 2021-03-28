# ile ukrytych słów papadam znajduje się w napisie. Na przykład w napisie:  ppapadaaaamaaapaappaddmppaapadaaaamppaa 

def papadam(wyraz):
    temp = 'papadam'
    count = 0
    wynik = 0
    while len(wyraz) != 0:
        if wyraz[0] == temp[0]:
            wyraz = wyraz[1:]
            temp = temp[1:]
            count = count + 1
            if count == 7:
                temp = 'papadam'
                count = 0
                wynik = wynik + 1
        else:
            wyraz = wyraz[1:]
    print(wynik)
