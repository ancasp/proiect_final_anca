# Creati un o functie care foloseste OPENAI API si primeste ca argumente o listă de ingrediente
# (un număr nedeterminat, *args sau **kwargs) și trebuie să vă dea o rețetă de mâncare ca răspuns.
# ** Implică să vă faceți un cont pe openai website și să faceți link la cardul cu bani.
# Dar vă recomand să puneți o limită infimă de gen 5 USD ca maxim/lună,

# un exemplu de cum puteți crea o astfel de funcție în Python, iar apoi puteți să o utilizați pe baza
# documentației API OpenAI. Mai întâi, asigurați-vă că v-ați înregistrat pe site-ul OpenAI și ați obținut cheia
# API necesară pentru autentificare. Apoi, puteți utiliza biblioteca openai pentru a efectua cereri la API-ul OpenAI.
# Instalați mai întâi biblioteca folosind pip:  pip install openai
# Iată un exemplu simplu de funcție care primește o listă de ingrediente și folosește API-ul OpenAI pentru a
# genera o rețetă de mâncare:

import openai

def generate_recipe(*ingredients):
    # Înlocuiți 'YOUR_API_KEY' cu cheia dvs. API OpenAI
    openai.api_key = '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'

    # Verificăm dacă avem cel puțin un ingredient în listă
    if not ingredients:
        return "Vă rugăm să furnizați cel puțin un ingredient pentru a genera o rețetă."

    # Concatenăm ingredientele într-o singură șir de caractere
    ingredient_string = ', '.join(ingredients)

    # Cerem API-ului OpenAI să genereze o rețetă
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generează o rețetă de mâncare folosind următoarele ingrediente: {ingredient_string}",
        max_tokens=1000  # Ajustați acest număr în funcție de lungimea dorită a rețetei
    )
    # Returnăm răspunsul generat de API
    return response.choices[0].text.strip()


# Exemplu de utilizare
ingredients = ["unt", "peste", "broccolli", "usturoi"]
recipe = generate_recipe(*ingredients)
print(recipe)

# Asigurați-vă că ați înlocuit 'YOUR_API_KEY' cu cheia API corectă și ați ajustat opțiunile API după necesitățile dvs.
# Puteți consulta documentația OpenAI pentru a afla mai multe despre modul de utilizare a API-ului lor:
# https://beta.openai.com/docs/.
# Rețineți că aceasta este doar o implementare simplă de bază. Puteți personaliza și rafina această funcție pentru a
# satisface mai bine cerințele dvs.

# openai.Completion.create: Aceasta este o metodă furnizată de biblioteca openai, care este utilizată pentru a trimite
# cereri către API-ul OpenAI. Metoda Completion.create este utilizată în acest caz pentru a genera un text complet
# (în cazul dvs., o rețetă) pe baza prompt-ului dat.

# engine="davinci": Specifică motorul (sau modelul) de limbă pe care doriți să-l utilizați pentru generarea textului.
# "Davinci" este unul dintre motoarele puternice oferite de OpenAI.

# prompt=f"Generează o rețetă de mâncare folosind următoarele ingrediente: {ingredient_string}": Aceasta este propoziția
# sau fragmentul de text pe baza căruia modelul va genera rețeta. Se utilizează formatul f-string pentru a insera
# variabila ingredient_string în prompt. Prompt-ul indică modelului ceea ce doriți să realizați, adică să genereze o
# rețetă de mâncare pe baza ingredientelor furnizate.

# max_tokens=100: Această opțiune specifică numărul maxim de "token-uri" (unități de text, care pot fi cuvinte sau
# caractere) pe care modelul le poate genera. Dacă doriți o rețetă mai lungă, puteți crește acest număr. Dacă îl
# scădeți, rețeta generată va fi mai scurtă.

# În esență, această cerere îi spune modelului "davinci" să genereze o rețetă de mâncare, având în vedere ingredientele
# furnizate și să limiteze lungimea rețetei la cel mult 100 de token-uri. Modelul va răspunde cu o rețetă generată în
# funcție de prompt-ul furnizat.

