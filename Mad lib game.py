# Mad Libs Game in Python

def mad_libs():
    print("Welcome to the Mad Libs game!")
    print("Please provide the following words:\n")

    # User inputs
    adjective1 = input("Adjective: ")
    noun1 = input("Noun: ")
    verb_past_tense = input("Verb (past tense): ")
    adverb = input("Adverb: ")
    adjective2 = input("Another adjective: ")
    noun2 = input("Another noun: ")
    noun3 = input("One more noun: ")
    verb_ing = input("Verb ending in -ing: ")
    verb2 = input("Another verb: ")
    adjective3 = input("One last adjective: ")

    # Story template
    story = f"""
    Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.
    He {verb_past_tense} {adverb} through the large tunnel that led to its {adjective2} {noun2}.
    I got some peanuts and passed them through the cage to a gigantic {noun3} towering above my head.
    Feeding that animal made me hungry. I went to get a {verb_ing} ice cream cone.
    Afterwards, I had to {verb2} to catch our bus.
    When I got home, I felt {adjective3} about my day at the zoo!
    """

    print("\nHere's your Mad Libs story:")
    print(story)

# Run the game
mad_libs()
