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
random_event = 0
random_job = 0
time_for_new_job = 0
percent_of_salary = 1
salary = 0.0
events_dispo = 7
jobs_dispo = 8
event_name_display = "Aucun évenement en cours"
version = 1.0
job_name = "sans emploi"
argent = 100.0
events_list = []
jobs_list = []
x = 1
day = 1
for i in range(events_dispo):
    events_list.append(x)
    x += 1
x = 1
for i in range(jobs_dispo):
    jobs_list.append(x)
    x += 1
def event_presentation(event_name, luck_level, day, description, effect1, effect2, effect3, effect4):
    global event_name_display
    if luck_level == 1:
        chance = f"{colorama.Fore.GREEN}Oui"
    if luck_level == 2:
        chance = f"{colorama.Fore.YELLOW}Bof"
    if luck_level == 3:
        chance = f"{colorama.Fore.RED}Non"
    event_name_display = event_name
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
    os.system(f'title Jour n°{day} - Argent : {argent}€ - Event en cours : {event_name_display}')
def event(x):
    global argent
    global percent_of_salary
    global precedent_event
    global random_event
    precedent_event = random_event
    while random_event == precedent_event:
        random_event = random.choice(events_list)
    if random_event == 1:
        event_presentation("Tomber Malade", 3, day, "Vous êtes tomber malade, vous devez donc aller chez le médecin.", "-50% salaire du jour --> Vous ne pouvez pas aller travailler", "-20€ --> prix de la consultation", "-10€ --> Prix des médicaments", "")
        argent = argent - 30
        time.sleep(1.0)
        print(f"{colorama.Fore.RED}30€ ont été retiré de votre compte (argent + médicament).")
        print(f"{colorama.Fore.BLUE}Il vous reste donc {argent}€")
        percent_of_salary = 0.5
    if random_event == 2:
        event_presentation("Appel de la radio", 1, day, "La radio vous appelle et vous pose une questions pour essayer de gagner de l'argent", "+100€ --> Si bonne réponse", "", "", "")
        print(f"{colorama.Fore.YELLOW}")
        answer = input(f"Question >>> Qui est votre dévelopeur préféré ? >>> ").lower()
        percent_of_salary = 1
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
    if random_event == 3:
        event_presentation("Boss de bonne humeur", 1, day, "Votre boss est de bonne humeur et vous fait une augmentation de salaire pour 1 jour et vous donne 10€ pour vous remercier de votre travail.", "+50% salaire du jour", "+10€", "","")
        percent_of_salary = 1.5
        argent = argent + 10
        time.sleep(2.0)
        print(f"{colorama.Fore.GREEN}10€ ont étés rajouté à votre compte!")
        print(f"{colorama.Fore.YELLOW}Vous avez maintenant {argent}€")
    if random_event == 4:
        event_presentation("Trouver une pièce", 2, day, "Vous avez trouvé sur le trotoir en rentrant de chez vous une pièce de 2€", "+2€", "", "", "")
        percent_of_salary = 1.0
        argent = argent + 2
        time.sleep(2.0)
        print(f"{colorama.Fore.GREEN}2€ ont étés rajouté à votre compte!")
        print(f"{colorama.Fore.YELLOW}Vous avez maintenant {argent}€")
    if random_event == 5:
        global job_name
        global salary
        global time_for_new_job
        event_presentation("Faillite", 2, day, "L'entreprise dans laquelle vous travaillez fait faillite... Vous pouvez retrouver un emploi sans délai.", "Plus de travail", "plus de salaire", "temps pour retrouver un travail à 0", "+200€ de dédomagement")
        job_name = "sans emploi"
        salary = 0
        time_for_new_job = 0
        argent = argent + 200
        percent_of_salary = 1.0
        print(f"{colorama.Fore.GREEN}200€ ont étés rajouté à votre compte!")
        print(f"{colorama.Fore.YELLOW}Vous avez maintenant {argent}€")
    if random_event == 6:
        event_presentation("Jour des courses", 3, day, "Votre frigo est vide et vous devez aller faire des courses pour vous nourir", "-100€ (courses)", "-10€ (transport)","","")
        argent = argent -110
        print(f"{colorama.Fore.RED}110€ ont étés retiré de votre compte!")
        print(f"{colorama.Fore.YELLOW}Vous avez maintenant {argent}€")
        percent_of_salary = 1.0
    if random_event == 7:
        event_presentation("Demande de recrutement", 1, day, "Une entreprise vous a envoyé une lettre pour vous demander si vous voulez travailler pour eux..", "Temps avant de pouvoir changé de travail remis à 0", "-30% de salaire (votre patron doute de vous)", "", "")
        time_for_new_job = 0
        percent_of_salary = 0.70



def space():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def entrer():
    print(f"{colorama.Fore.WHITE}")
    input("Appuyez sur entrée...")
def get_a_job():
    global job_name
    global salary
    global precedent_job
    global random_job
    precedent_job = random_job
    random_job = random.choice(jobs_list)
    while random_job == precedent_job:
        random_job = random.choice(jobs_list)
    if random_job == 1:
        job_name = "Caissier"
        salary = 44.3
    if random_job == 2:
        job_name = "Pilote d'avions de ligne"
        salary = 160
    if random_job == 3:
        job_name = "Pompier"
        salary = 70
    if random_job == 4:
        job_name = "Professeur"
        salary = 90
    if random_job == 5:
        job_name = "Astronaute"
        salary = 320
    if random_job == 6:
        job_name = "Chirurgien"
        salary = 130
    if random_job == 7:
        job_name = "Forgeron"
        salary = 75
    if random_job == 8:
        job_name = "Travailleur agricole"
        salary = 60
def available_choices(time_for_new_job):
    if time_for_new_job <= 0:
        possible_to_change_job = "[ V ]"
    if time_for_new_job > 0:
        possible_to_change_job = "[ X ]"
    print(f"""{colorama.Fore.YELLOW}

Options:    
{colorama.Fore.CYAN}[01] {colorama.Fore.RED}>>> {colorama.Fore.YELLOW}Passer au jour suivant (nouvel envent) {colorama.Fore.WHITE}[ V ]
{colorama.Fore.CYAN}[02] {colorama.Fore.RED}>>> {colorama.Fore.YELLOW}Obtenir un nouveau travail             {colorama.Fore.WHITE}{possible_to_change_job}
    
    """)
while True:
    os.system(f'title Jour n°{day} - Argent : {argent}€ - Event en cours : {event_name_display} - Job : {job_name} - Salaire : {salary}€')
    available_choices(time_for_new_job)
    print(f"\n {colorama.Fore.LIGHTBLUE_EX}")
    choice = int(input("Veuillez entrer le numéro de l'option voulue >>> "))
    if choice == 1:
        salaire_recu = salary * percent_of_salary
        print(f"Salaire de base : {salary}€")
        print(f"Salaire reçu : {salaire_recu}€")
        previous_money = argent
        argent = argent + salaire_recu
        print(f"Argent : {previous_money}€ --> {argent}€")
        os.system(f'title Jour n°{day} - Argent : {argent}€ - Event en cours : {event_name_display} - Job : {job_name} - Salaire : {salary}€')
        entrer()
        space()
        day += 1
        time_for_new_job = time_for_new_job - 1
        event(1)
        os.system(f'title Jour n°{day} - Argent : {argent}€ - Event en cours : {event_name_display} - Job : {job_name} - Salaire : {salary}€')
        entrer()
        space()
    if choice == 2:
        if time_for_new_job <= 0:
            get_a_job()
            print(f"{colorama.Fore.GREEN}Félicitations vous venz d'obtenir un nouveau métier !")
            print(f"{colorama.Fore.YELLOW}Nouveau métier : {job_name}")
            print(f"{colorama.Fore.CYAN}Salaire par jour : {salary}€")
            salary_per_month = salary * 30
            print(f"{colorama.Fore.GREEN}Salaire par mois : {salary_per_month}€")
            time_for_new_job = 10
            os.system(f'title Jour n°{day} - Argent : {argent}€ - Event en cours : {event_name_display} - Job : {job_name} - Salaire : {salary}€')
            entrer()
            space()
        else:
            print(f"Vous devez attendre {time_for_new_job} jours avant d'avoir un nouveau travail !")
            os.system(f'title Jour n°{day} - Argent : {argent}€ - Event en cours : {event_name_display} - Job : {job_name} - Salaire : {salary}€')
            entrer()
            space()
