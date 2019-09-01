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
    # This is the beginning of Mad libs:
    print("Welcome.")

    # User is asked to enter in part of speech:
    noun1 = insert_words("Enter a noun: ")
    # Append the word into the list of word word blanks:
    create(noun1)

    adjective1 = insert_words("Enter adjective: ")
    create(adjective1)

    verb1 = insert_words("Enter verb: ")
    create(verb1)

    adjective2 = insert_words("Enter another adjective: ")
    create(adjective2)

    noun2 = insert_words("Enter another noun: ")
    create(noun2)

    # The story with the Users inserted words:
    print("I have a " + noun1 + " in my pocket.")
    print("It feels " + adjective1 + ".")
    print("You can touch it, feels it and " + verb1 + " it.")
    print(" When it is happy, it smells " + adjective2 + ".")
    print("It is best friends with a " + noun2 + ".")
    

# Run the Function:
mad_libs()
