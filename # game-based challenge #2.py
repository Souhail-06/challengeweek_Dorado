# game-based challenge 
import time
def print_slow(tekst, vertraging=1):
    print(tekst)
    time.sleep(vertraging)  

inventaris = []
def start():
    print_slow("Welkom bij de zoektocht naar de Verloren Stad El Dorado!", 3)
    print_slow("Je begint je avontuur in een klein dorp aan de rand van het oerwoud.", 3)
    print_slow("De legende vertelt dat El Dorado ergens diep in de jungle verborgen ligt, vol met schatten en mysteries.", 3)
    print_slow("Maar wees gewaarschuwd, het pad er naartoe is gevaarlijk en vol uitdagingen.", 2)
    print("\nJe staat nu op het dorpsplein. Wat wil je doen?")

    while True: 
        print("\n1. Praat met de dorpsgek.")
        print("2. Koop equipment van de markt.")
        keuze = input("\nWelke van de twee kies je?: ")

        if keuze == '1':
            print_slow("\nJe besluit om met de dorpsgek te praten. Als dat maar goed gaat...", 1)
            bezoek_de_dorpsgek()
            break  
        elif keuze == '2':
            print_slow("\nJe gaat naar de markt. Altijd handig om wat equipment te halen voor de reis.", 1)
            ga_naar_de_markt()
            break  
        else:
            print_slow("\nOngeldige keuze. Probeer opnieuw.", 1)

def bezoek_de_dorpsgek():
    print_slow("\nJe ziet de dorpsgek staan. Het is een oude man met een langen baard en vieze kleren.", 2)
    print_slow("Je vraagt of hij iets weet over de verloren stad el Dorado.", 2)
    print_slow('Hij zegt dat hij er zelf ooit is geweest, maar dat niemand hem ooit heeft geloofd.', 1)
    print_slow('Het enige wat hij nog over heeft van zijn bezoek is een amulet, maar of die ook echt afkomstig is van el Doraldo is een mysterie.', 5)
    print_slow("\nHij geeft jou het amulet in de hoop dat jij er wel wat aan hebt", 4)

    inventaris.append('amulet')
    print_slow("\nJe hebt nu een amulet aan je inventaris toegevoegd!", 2)
    print(f"Je inventaris: {inventaris}")
    de_jungle_in()
    
def ga_naar_de_markt():

    while True:
        print('Je hebt genoeg geld voor een klimhaak, kapmes of een zaklamp.')
        keuze2 = input('\nWelke kies je?: ').lower()

        if keuze2 == 'klimhaak':
            inventaris.append(keuze2)
            print_slow('\nJe hebt nu een klimhaak aan je inventaris toegevoegd.', 1)
            print(f'Je inventaris: {inventaris}')
            de_jungle_in()
            break
        elif keuze2 == 'kapmes':
            inventaris.append(keuze2)
            print_slow('\nJe hebt nu een kapmes aan je inventaris toegevoegd.', 1)
            print(f'Je inventaris: {inventaris}')
            de_jungle_in()
            break
        elif keuze2 == 'zaklamp':
            inventaris.append(keuze2)
            print_slow('\nJe hebt nu een zaklamp aan je inventaris toegevoegd.', 1)
            print(f'Je inventaris: {inventaris}')
            de_jungle_in()
            break
        else:
            print_slow("\nOngeldige keuze. Probeer opnieuw.", 1)

def de_jungle_in():
    print_slow("\nJe betreedt het oerwoud. Het is donker en mysterieus...", 2)
    print_slow("Je komt bij een splitsing met vier paden:", 2)
    print_slow("1. Een wankele hangbrug.", 2)
    print_slow("2. Een donkere grot.", 2)
    print_slow("3. Een dichtbegroeid pad.", 2)
    print_slow("4. Een verborgen tempel.", 2)
    
    while True:
        keuze = input("\nWelk pad kies je? (1, 2, 3 of 4): ")

        if keuze == '1':  
            if 'klimhaak' in inventaris:
                print_slow("\nJe gebruikt je klimhaak om veilig over de hangbrug te klimmen.", 2)
                print_slow("Aan de andere kant vind je een verborgen schat, het is een gouden beeltje", 2)
                inventaris.append('gouden beeltje')
                print(f"Je inventaris: {inventaris}")
                gouden_beeltje_opdracht()
                break
            else:
                print_slow("\nZonder klimhaak is de hangbrug te gevaarlijk om over te steken.", 2)
                print_slow("Wat wil je doen?", 1)
                print("1. Een ander pad kiezen.")
                print("2. Terugkeren naar het dorp om equipment te kopen.")
                sub_keuze = input("\nKies een optie (1 of 2): ")

                if sub_keuze == '1':
                    continue  
                elif sub_keuze == '2':
                    print_slow("\nJe besluit terug te keren naar het dorp.", 2)
                    ga_naar_de_markt()
                    break
                else:
                    print_slow("\nOngeldige keuze. Probeer opnieuw.", 1)

        elif keuze == '2':  
            if 'zaklamp' in inventaris:
                print_slow("\nJe gebruikt je zaklamp om de grot te verkennen.", 2)
                print_slow("Diep in de grot vind je een oude kaart!", 2)
                inventaris.append('kaart')
                print(f"Je inventaris: {inventaris}")
                kaart_opdracht()
                break
            else:
                print_slow("\nZonder zaklamp is de grot te donker om te betreden.", 2)
                print_slow("Wat wil je doen?", 1)
                print("1. Een ander pad kiezen.")
                print("2. Terugkeren naar het dorp om equipment te kopen.")
                sub_keuze = input("\nKies een optie (1 of 2): ")

                if sub_keuze == '1':
                    continue  
                elif sub_keuze == '2':
                    print_slow("\nJe besluit terug te keren naar het dorp.", 2)
                    ga_naar_de_markt()
                    break
                else:
                    print_slow("\nOngeldige keuze. Probeer opnieuw.", 1)

        elif keuze == '3':  
            if 'kapmes' in inventaris:
                print_slow("\nJe gebruikt je mes om het pad vrij te maken.", 2)
                print_slow("Aan het einde van het pad vind je een verborgen waterval, achter de waterval vind je een code", 2)
                inventaris.append('code')
                print(f"Je inventaris: {inventaris}")
                code_ontcijferen()
                break
            else:
                print_slow("\nZonder mes kun je het dichtbegroeide pad niet passeren.", 2)
                print_slow("Wat wil je doen?", 1)
                print("1. Een ander pad kiezen.")
                print("2. Terugkeren naar het dorp om equipment te kopen.")
                sub_keuze = input("\nKies een optie (1 of 2): ")

                if sub_keuze == '1':
                    continue  
                elif sub_keuze == '2':
                    print_slow("\nJe besluit terug te keren naar het dorp.", 2)
                    ga_naar_de_markt()
                    break
                else:
                    print_slow("\nOngeldige keuze. Probeer opnieuw.", 1)

        elif keuze == '4':  
            if 'amulet' in inventaris:
                print_slow("\nJe gebruikt de amulet om de verborgen tempel binnen te gaan.", 2)
                print_slow("Binnen vind je een oud altaar met een inscriptie die de locatie van El Dorado onthult!", 3)
                inventaris.append('inscriptie')
                print(f"Je inventaris: {inventaris}")
                inscriptie()
                break
            else:
                print_slow("\nZonder de amulet kun je de tempel niet betreden.", 2)
                print_slow("Wat wil je doen?", 1)
                print("1. Een ander pad kiezen.")
                print("2. Terugkeren naar het dorp om equipment te kopen.")
                sub_keuze = input("\nKies een optie (1 of 2): ")

                if sub_keuze == '1':
                    continue  
                elif sub_keuze == '2':
                    print_slow("\nJe besluit terug te keren naar het dorp.", 2)
                    ga_naar_de_markt()
                    break
                else:
                    print_slow("\nOngeldige keuze. Probeer opnieuw.", 1)

        else:
            print_slow("\nOngeldige keuze. Probeer opnieuw.", 1)


def gouden_beeltje_opdracht():
    print_slow('\nIn het beeldje zitten de coördinaten van el Dordo.',2)
    print_slow("Echter zie je in de verte een leger aan soldaten.", 2)
    print_slow("Je hebt twee opties.", 2)
    print("1. Je rent weg.")
    print("2. je verstopt je achter een boom in de hoop dat ze je niet zien.")

    while True:
        keuze3 = input("Welke van de twee opties kies je?: ")

        if keuze3 == '1':
            print_slow("Je rent zo hard als je kan maar dan....", 3)
            print("AAAH! Je struiket over een banaan en het leger pakt je... je had beter voor optie 2 kunnen gaan!")
            game_over()
        elif keuze3 == '2':
            print_slow("Je houdt je adem in terwijl de soldaten voorbij lopen... Éen van hen kijkt even jouw kant op, maar loopt dan door. Je hebt geluk gehad--voor nu.", 5)
            print_slow("Je opent het beeldje en daar staan de coördinaten van el Dorado.",2)
            print("je vervolgt je weg naar de coördinaten.")
            eiland_van_vuur()
        else:
            print("\nOngeldige keuze. Probeer opnieuw.")

def code_ontcijferen():
    print_slow("\nDe code is: V-IX-XII-I-XIV-IV-XXII-XIV-I-XXII-XXI-XXI-XVIII", 3)

    geheime_code = input("Ontcijfer de code: ").lower()

    while True:
        if geheime_code == 'eiland van vuur':
            print_slow('\nJe hebt de code ontcijfert, vervolg je weg naar et eiland van vuur.', 3)
            eiland_van_vuur()
            break
        else:
            print('Fout, probeer opnieuw.')
            break

def inscriptie():
    print_slow("\nJe bestudeert de inscriptie op het altaar.", 2)
    print_slow("De inscriptie vertelt over een mysterieus Eiland van Vuur, ergens ver in de oceaan.", 3)
    print_slow("Het eiland zou de sleutel bevatten om El Dorado te vinden.", 2)
    
    while True:
        print("\nWat wil je doen?")
        print("1. Volg de aanwijzingen naar het Eiland van Vuur.")
        print("2. Keer terug naar het dorp om je voor te bereiden.")
        keuze = input("\nKies een optie (1 of 2): ")

        if keuze == '1':
            print_slow("\nJe besluit het avontuur aan te gaan en naar het Eiland van Vuur te reizen.", 2)
            eiland_van_vuur()  
            break
        elif keuze == '2':
            print_slow("\nJe besluit terug te keren naar het dorp om je beter voor te bereiden.", 2)
            start() 
            break
        else:
            print_slow("\nOngeldige keuze. Probeer opnieuw.", 1)

def kaart_opdracht():
    print_slow("\nJe bekijkt de oude kaart die je hebt gevonden.", 2)
    print_slow("De kaart toont een route met drie symbolen:", 2)
    print_slow("1. Een boom met een X erop.", 2)
    print_slow("2. Een rivier met een pijl.", 2)
    print_slow("3. Een rots met een cirkel.", 2)
    print_slow("Volg de symbolen in de juiste volgorde om de verborgen route te vinden.", 2)
    
   #fakka
    juiste_volgorde = ['1', '2', '3']
    speler_volgorde = []
    
    while len(speler_volgorde) < 3:
        print("\nKies een symbool om te volgen:")
        print("1. Boom met X")
        print("2. Rivier met pijl")
        print("3. Rots met cirkel")
        keuze = input("\nKies een symbool (1, 2 of 3): ")
        
        if keuze in ['1', '2', '3']:
            speler_volgorde.append(keuze)
            print_slow(f"\nJe volgt symbool {keuze}.", 1)
        else:
            print_slow("\nOngeldige keuze. Probeer opnieuw.", 1)
    
   
    if speler_volgorde == juiste_volgorde:
        print_slow("\nJe hebt de juiste route gevonden!", 2)
        print_slow("Je komt aan bij een eiland!", 3)
        eiland_van_vuur()
    else:
        print_slow("\nHelaas, je bent verdwaald. Probeer het opnieuw.", 2)
        kaart_opdracht()  

def eiland_van_vuur():
    print_slow("\nJe arriveert op het Eiland van Vuur. De lucht is heet en vulkanen rommelen in de verte.", 2)
    print_slow("Plotseling verschijnt er een mysterieuze figuur voor je: de Wachter van El Dorado!", 3)
    print_slow("De Wachter spreekt: 'Als je El Dorado wilt vinden, moet je eerst mijn raadsel oplossen.'", 2)
    print_slow("'Je hebt drie kansen. Luister goed...'", 2)
    
    raadsel = "Ik ben geel, ik glim, en ik ben waardevol. Wat ben ik?"
    juiste_antwoord = "goud"
    kansen = 3
    
    while kansen > 0:
        print_slow(f"\nRaadsel: {raadsel}", 2)
        antwoord = input("\nWat is je antwoord? ").lower()
        
        if antwoord == juiste_antwoord:
            print_slow("\nDe Wachter lacht. 'Goed gedaan! Jij bent het waard om El Dorado te vinden.'", 3)
            print_slow("De Wachter wijst je naar een verborgen pad dat naar El Dorado leidt.", 2)
            vind_el_dorado() 
            break
        else:
            kansen -= 1
            if kansen > 0:
                print_slow(f"\nFout! Je hebt nog {kansen} {'kans' if kansen == 1 else 'kansen'} over.", 2)
            else:
                print_slow("\nHelaas, je hebt geen kansen meer over.", 2)
                print_slow("De Wachter schudt zijn hoofd. 'Je bent niet waardig.'", 2)
                game_over()  
                break

def vind_el_dorado():
    print_slow("\nJe volgt het verborgen pad en komt aan bij de legendarische stad El Dorado!", 3)
    print_slow("De stad glinstert in de zon, vol met goud en schatten.", 2)
    print_slow("Je hebt het avontuur voltooid en El Dorado gevonden!", 3)
    print_slow("Gefeliciteerd, je bent een echte ontdekkingsreiziger!", 2)
    exit()  


def game_over():
    print("GAME OVER.")
    exit()


start()