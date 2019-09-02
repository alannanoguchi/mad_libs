# The Story:

# I have a __(noun)__ in my pocket.
# It feels __(adj)__. You can touch it, feed it and __(verb)__ it. When it is happy, it smells __(adj)__.
# It is best friends with a __(noun)__.

# A list of blank words:
wordBlanks = list()

# Create:
def create(item):
    # Adding items into the list:
    wordBlanks.append(item)

# User fills in the blanks
def insert_words(item):
    insert_words = input(item)
    return insert_words

# Mad Libs:
def mad_libs():
    # This is the beginning of the Mad libs story:
    print("Welcome!")

    # User is asked to enter in appropriate part of speech:
    noun1 = insert_words("Enter a noun: ")
    # Append the word into the list of word blanks:
    create(noun1)

    adjective1 = insert_words("Enter adjective: ")
    create(adjective1)

    verb1 = insert_words("Enter verb: ")
    create(verb1)

    adjective2 = insert_words("Enter another adjective: ")
    create(adjective2)

    noun2 = insert_words("Enter another noun: ")
    create(noun2)

    # Separate the user input from the story:
    print("----------------------------")

    # The story with the Users inserted words:
    print("My Mad Libs Story:")
    print("I have a(an) " + noun1 + " in my pocket.")
    print("It feels " + adjective1 + ".")
    print("You can touch it, feel it and " + verb1 + " it.")
    print("When it is happy, it smells " + adjective2 + ".")
    print("It is best friends with a " + noun2 + ".")
    print("The end.")

# Run the Function:
mad_libs()
