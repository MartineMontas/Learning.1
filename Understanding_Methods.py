# Define the variables we're going to use
def get_value(question_input):
    print("Give me a "+question_input)
    input_from_user = input()
    while input_from_user == "":
        print("Please type something ")
        input_from_user = input()
    return input_from_user

# name of a pet
name = get_value("name")
# type of animal
animal = get_value("animal")
# verb you can do with a pet
verb1 = get_value("verb1")
# place at your house, apartment, or dorm (ex: yard or kitchen)
place = get_value("place")
# time of day
time = get_value("time")
# 3 descriptive adjectives (individual variables)
adj1 = get_value("adj1")
adj2 = get_value("adj2")
adj3 = get_value("adj3")
# favorite game
game = get_value("game")
# pronoun
pronoun = get_value("pronoun")
# another action verb (present tense)
verb2 = get_value("verb2")
# favorite item in your room
item = get_value("item")
# another time of the day
time2 = get_value("time2")
# a person in your life
person = get_value("person")
# a chore verb (ex: clean or wash)
verb3 = get_value("verb3")
# a chore (ex: do the dishes)
chore = get_value("chore")

print("All of my life I have wanted a single {} to {}".format(animal, verb1))
print("with in the {0}. I would name it {1}. {1} would be so".format(place, name.title()))
print("{}, {}, and {}. We would {} {}".format(adj1, adj2, adj3, verb1, game))
print("together every {} and {} would {}".format(time, pronoun, verb2))
print("next to my {} at {}. {} says I can’t".format(item, time2, person.capitalize()))
print("have get my {} until I learn to {} the {} and".format(animal, verb3, place))
print("{}. {}ing is not something I enjoy doing,".format(chore, verb3.capitalize()))
print("but I’ll do it if I can have just one {} {}".format(adj1, animal))
print("to {} with!".format(verb1))
