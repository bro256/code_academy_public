skysti_produktai = ['pienas', 'surelis','varske', 'jogurtas', 'suris']
kieti_produktai = ['kvieciu miltai', 'rugiu miltai', 'kukuruzu miltai', 'ryziu miltai', 'makaronai penne', 'bociu duona', 'kruasanas', 'meduoliai', 'krekeriai', 'saldyti varskeciai']
paruosti_patiekalai = [
    'krosanai', 'amerikietiški blyneliai',
    'lietiniai blynai', 'spurgos',
]

import os
os.system('cls')

while True:
#    os.system('cls')

    print('------- Meniu -------')
    print('1: Pirmas')
    print('2: Antras')
    print('3: Trecias')
    print('4: Ketvirtas')
    print('0: išeiti')

    pasirinkimas = input('Pasirinkite: ')

    if pasirinkimas == "0":
        os.system('cls')
        print('------- Viso gero -------')
        break

    elif pasirinkimas == "1":
 #       os.system('cls')
        print ('pirmas')

    elif pasirinkimas == "2":
 #       os.system('cls')
        print ('antras')

    else:
 #       os.system('cls')
        print ('netinka')