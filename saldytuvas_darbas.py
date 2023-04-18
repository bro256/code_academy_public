skysti_produktai = ['pienas', 'jogurtas', 'kefyras', 'gira', 'degtine', 'obuoliu sultys']
kieti_produktai = ['kvieciu miltai', 'rugiu miltai', 'kukuruzu miltai', 'ryziu miltai', 'makaronai penne']
paruosti_patiekalai = ['krosanai', 'amerikietiški blyneliai','lietiniai blynai', 'spurgos']

saldytuvo_produktai = skysti_produktai + kieti_produktai + paruosti_patiekalai

import os
os.system('cls')

saldytuvas = {}

while True:
#    os.system('cls')

    print('------- Meniu -------')
    print('1: Įdėti produktus')
    print('2: Išimti produktus')
    print('3: Peržiūrėti sarašą')
    print('4: Bendras svoris')
    print('0: išeiti')

    

    def prideti_produktus():
        print(f"{'Numeracija':<10} {'Produktai'}")  # string formating to add column names for 'task index' & 'task name'
        for i, task in enumerate(saldytuvo_produktai):
            print("{:<10} {}".format(i, task))  # formated & descriptive in terminal / harder to read as code
            produkto_pasirinkimas = input('Įveskite norima produktą: ')
            produktu_kiekis = float(input('Įveskite produkto kiekį (kg/L): '))
        return[produkto_pasirinkimas, produktu_kiekis]
    
    def isimti_produktus():
        return
    
    def perziureti_sarasa():
        return
    
    def bendras_svoris():
        return
    

        

    pasirinkimas = input('Pasirinkite: ')

    if pasirinkimas == "0":
        os.system('cls')
        print('------- Viso gero -------')
        break

    elif pasirinkimas == "1":

 #       os.system('cls')
        prideti_produktus()

    elif pasirinkimas == "2":
 #       os.system('cls')
        isimti_produktus()

    elif pasirinkimas == "3":
 #       os.system('cls')
        perziureti_sarasa()

    elif pasirinkimas == "4":
 #       os.system('cls')
        bendras_svoris()

    else:
 #       os.system('cls')
        print ('netinka')