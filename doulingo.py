words = {
    "the": "el",
    "and": "y",
    "in": "en",
    "to be": "ser",
    "to have": "tener",
    "to do": "hacer",
    "to be able to": "poder",
    "to say": "decir",
    "to go": "ir",
    "to see": "ver",
    "to give": "dar",
    "to know": "saber",
    "to want": "querer",
    "to arrive": "llegar",
    "to pass": "pasar",
    "to must": "deber",
    "to put": "poner",
    "to seem": "parecer",
    "to stay": "quedar",
    "to believe": "creer",
    "to speak": "hablar",
    "to carry": "llevar",
    "to leave": "dejar",
    "to follow": "seguir",
    "to find": "encontrar",
    "to come": "venir",
    "to think": "pensar",
    "to go out": "salir",
    "to return": "volver",
    "to take": "tomar",
    "to know (meet)": "conocer",
    "to live": "vivir",
    "to feel": "sentir",
    "to try": "tratar",
    "to look at": "mirar",
    "to count": "contar",
    "to begin": "empezar",
    "to wait": "esperar",
    "to look for": "buscar",
    "to exist": "existir",
    "to enter": "entrar",
    "to work": "trabajar",
    "to write": "escribir",
    "to lose": "perder",
    "to produce": "producir",
    "to occur": "ocurrir",
    "to understand": "entender",
    "to ask for": "pedir",
    "to receive": "recibir",
    "to remember": "recordar",
    "to finish": "terminar",
    "to permit": "permitir",
    "to appear": "aparecer",
    "to get": "conseguir",
    "to serve": "servir",
    "to take out": "sacar",
    "to need": "necesitar",
    "to maintain": "mantener",
    "to result in": "resultar",
    "to read": "leer",
    "to fall": "caer",
    "to change": "cambiar",
    "to present": "presentar",
    "to create": "crear",
    "to open": "abrir",
    "to consider": "considerar",
    "to hear": "oír",
    "to finish (end)": "acabar",
    "to convert": "convertir",
    "to win": "ganar",
    "to form": "formar",
    "to bring": "traer",
    "to leave (depart)": "partir",
    "to die": "morir",
    "to accept": "aceptar",
    "to achieve": "realizar",
    "to suppose": "suponer",
    "to understand (comprehend)": "comprender",
    "to reach": "lograr",
    "to explain": "explicar",
    "to ask": "preguntar",
    "to touch": "tocar",
    "to study": "estudiar",
    "to reach (achieve)": "alcanzar",
    "to be born": "nacer",
    "to direct": "dirigir",
    "to run": "correr",
    "to use": "utilizar",
    "to pay": "pagar",
    "to help": "ayudar",
    "to like": "gustar",
    "to play": "jugar",
    "to listen": "escuchar",
    "to fulfill": "cumplir",
    "to offer": "ofrecer",
    "to discover": "descubrir",
    "to lift": "levantar",
    "to try (attempt)": "intentar",
    "to use (utilize)": "usar"
}

def quiz(words):
    score = 0
    for word, translation in words.items():
        answer = input(f"What is the translation of '{word}'? ")
        if answer == translation:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct translation is '{translation}'.")
    print(f"Your score is {score}/{len(words)}")

def duolingo():
    print("Flashcards App: Learn Spanish with Flashcards")
    quiz(words)

if __name__ == "__main__":
    duolingo()