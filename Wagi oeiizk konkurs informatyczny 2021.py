"""Tolek każdej literze w słowie przypisuje liczbę całkowitą nieujemną, którą nazywa wagą litery.
Pierwsza i ostatnia litera słowa ma wagę 1, druga i przedostatnia wagę 2, trzecia od początku
i końca wagę 3, itd. Następnie wszystkim samogłoskom redukuje wagę o jeden, a spółgłoskom
zwiększa wagę o jeden. Wagę słowa oblicza sumując wszystkie wagi liter. Napisz program, który
ułoży słowa według ich wag od najmniejszej do największej. Jeśli dwa słowa mają taką samą wagę,
to występują wtedy w kolejności alfabetycznej. """

def wagi(tekst):
    samogloski = ['a', 'e', 'i' , 'o', 'u', 'y']
    wagi = [0 for i in range(len(tekst.split(' ')))]
    wyrazy = tekst.split(' ')
    print(wagi)
    for i, wyraz in enumerate(wyrazy):
        for j in range(int(len(wyraz)/2)):
            if len(wyraz) % 2 == 0:
                wagi[i] +=2*(j+1)
            else:
                wagi[i] = 2*(j+1) + (len(wyraz) // 2) + 1
    print(wagi)

    for i, wyraz in enumerate(wyrazy):
        for j in range(len(wyraz)):
            if wyraz[j] in samogloski:
                wagi[i] = wagi[i] - 1
            else:
                wagi[i] += 1
    print(wagi)

    print(sorted(wyrazy, key = lambda i: wagi[wyrazy.index(i)]))

wagi('ala kota ma')