#By Fire5917 | github >>> github.com/Fire5917/game
import os, time, random
try:
    import colorama
except:
    os.system('pip install colorama')
    import colorama
try:
    import requests
except:
    os.system('pip install requests')
    import requests
colorama.init()
events_dispo = 2
version = 1.0
argent = 100
events_list = []
x = 1
day = 1
for i in range(events_dispo):
    events_list.append(x)
    x += 1
def event_presentation(event_name, luck_level, day, description, effect1, effect2, effect3, effect4):
    if luck_level == 1:
        chance = f"{colorama.Fore.GREEN}Oui"
    if luck_level == 2:
        chance = f"{colorama.Fore.YELLOW}Bof"
    if luck_level == 3:
        chance = f"{colorama.Fore.RED}Non"
    print(f"""
{colorama.Fore.YELLOW}Jour {day}  ---  Evénement obtenu : {event_name}  ---  Chance : {chance}
{colorama.Fore.RED}__________________________________________________________________________________
{colorama.Fore.LIGHTRED_EX}                Event : {event_name}

{colorama.Fore.CYAN}Description : {description}    
{colorama.Fore.GREEN}Effets :
- {effect1}
- {effect2}
- {effect3}
- {effect4}

{colorama.Fore.RED}__________________________________________________________________________________   
    """)
def event(x):
    global argent
    random_event = random.choice(events_list)
    if random_event == 1:
        event_presentation("Tomber Malade", 3, day, "Vous êtes tomber malade, vous devez donc aller chez le médecin.", "-50% salaire du jour --> Vous ne pouvez pas aller travailler", "-20€ --> prix de la consultation", "-10€ --> Prix des médicaments", "")
        argent = argent - 30
        time.sleep(1.0)
        print(f"{colorama.Fore.RED}30€ ont été retiré de votre compte (argent + médicament).")
        print(f"{colorama.Fore.BLUE}Il vous reste donc {argent}€")
    if random_event == 2:
        event_presentation("Appel de la radio", 1, day, "La radio vous appelle et vous pose une questions pour essayer de gagner de l'argent", "+100€ --> Si bonne réponse", "", "", "")
        print(f"{colorama.Fore.YELLOW}")
        answer = input(f"Question >>> Qui est votre dévelopeur préféré ? >>> ").lower()
        if answer == "fire5917":
            print(f"{colorama.Fore.RED}Et")
            argent = argent + 100
            time.sleep(2.0)
            print(f"{colorama.Fore.GREEN}C'est la bonne réponse !!!")
            time.sleep(2.0)
            print(f"Vous venez de gagner {colorama.Fore.YELLOW}100€")
            print(f"{colorama.Fore.BLUE}Vous avez maintenant {argent}€")
        else:
            print(f"{colorama.Fore.RED}Et")
            time.sleep(2.0)
            print(f"C'est la mauvaise réponse")
            time.sleep(1.0)
            print("Vous n'avez rien gagné")
event(1)
input("")
