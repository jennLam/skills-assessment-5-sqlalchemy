"""

This file is the place to write solutions for the
practice part of skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes by just their
class name (and not model.ClassName).

"""

from model import *

init_app()

# -----------------
# PART TWO: QUERIES
# -----------------

# Get the human with the id 2.
q1 = Human.query.get(2)

# Get the *first* animal with the species 'fish'
q2 = Animal.query.filter_by(animal_species='fish').first()

# Get all of the animals for the human with the id 5 and the animal species 'dog'
q3 = Animal.query.filter_by(human_id=5, animal_species='dog').all()

# Get all the animals that were born after 2015 (do not include animals without birth years).
q4 = Animal.query.filter(Animal.birth_year > 2015).all()

# Find the humans with first names that start with 'J'
q5 = Human.query.filter(Human.fname.like('J%')).all()

# Find all the animals without birth years in the database.
q6 = Animal.query.filter(Animal.birth_year == None).all()

# Find all animals that are either fish or rabbits
q7 = Animal.query.filter((Animal.animal_species == 'fish') | (Animal.animal_species == 'rabbit')).all()

# Find all the humans whose email addresses do not contain 'gmail'
q8 = Human.query.filter(db.not_(Human.email.like('%gmail%'))).all()

# ---------------------
# PART THREE: FUNCTIONS
# ---------------------

# ***Do not use more than one query for each function***

# 1. Write a function, print_directory, which does not take any arguments
#    and prints out each human (once) with a list of their animals.

#    The output should look like this (with tabs to indent each animal name under
#    a human's name)

#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)


def print_directory():
    """Prints human and a list of their animals."""

    # Query to get a list of human first name, human last name, animal name and animal species
    human_animal_info = db.session.query(Human.fname, Human.lname, Animal.name,
                                         Animal.animal_species).join(Animal).order_by("fname").all()

    # Create a dictionary to hold all the humans and animals
    human_animal_dict = {}
    # Loop through each item in the the list of humans and their animals
    for fname, lname, name, animal_species in human_animal_info:
        # Concatenate the human's first and last name
        human_name = fname + " " + lname
        # Concatenate the animal's name and species
        animal_info = name + " (" + animal_species + ")"

        # Check if human is already in the dictionary
        if human_animal_dict.get(human_name):
            # If yes, append the animal to the list of values
            human_animal_dict[human_name].append(animal_info)
        else:
            # If not, create a key with the human's name and a value with a list
            # of its animal
            human_animal_dict[human_name] = [animal_info]

    # Loop to print human and animal information from dictionary
    # in correct format
    for human, animals in human_animal_dict.items():
        print human
        for animal in animals:
            print "\t" + animal

# 2. Write a function, get_animals_by_name, which takes in a string representing
#    an animal name (or part of an animal name) and *returns a list* of animals
#    whose names contain that string.


def get_animals_by_name(name):
    """Returns a list of animal objects that match an animal name or part of an
    animal name provided."""

    # Query to get animals with a particular name or part of name
    animal_list = Animal.query.filter(Animal.name.like('%' + name + '%')).all()

    return animal_list

# 3. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of the humans who have animals of
#    that species.


def find_humans_by_animal_species(species):
    """Returns a list of human objects who have animals of the species listed."""

    # Query to get humans who have a particular animal species
    human_list = db.session.query(Human).join(Animal).filter(Animal.animal_species == species).all()

    return human_list
