


# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

import random


# LISTS of FEATURES

destinations = ['New York City', 'Los Angeles', 'Houston', 'Schenectady', 'Atlanta']
restaurants = ['Pizza Hut', 'Margaritaville', 'Orange Dragon', 'Empanada Mama', 'Red Lobster']
entertainments = ['The Fair', 'Concert', 'Puppet Show', 'The Zoo', 'Silent Disco']
transportations = ['Train', 'Plane', 'Car', 'Bus', 'Heelys']

destination = random.choice(destinations)
restaurant = random.choice(restaurants)
entertainment = random.choice(entertainments)
transportation = random.choice(transportations)

day_trip = (f'Destination: {destination}, Restaurant: {restaurant}, Entertainment: {entertainment}, Transportation: {transportation}')

print(day_trip)

confirm_choice = input(f'Does this sound like fun? Please enter YES or NO to confirm these day trip options.')

# print(f' Have fun going to {destination}, dining at {restaurant}, going to {entertainment} all via {transportation}!' )

def new_dest(confirm_choice):
    while confirm_choice != 'YES':
        destination = random.choice(destinations)
        confirm_choice = input(f'We have selected {destination} as another trip option. Does that work for you? ')
        if confirm_choice == 'NO':
            destination = random.choice(destinations)
            confirm_choice = input(f'How about {destination}?')
        elif confirm_choice == 'YES':
             print(f'You selected {destination} as your trip destination! ')
             return destination
        else:
            print('Rain check.')
    

def new_rest(confirm_choice):
    while confirm_choice != 'YES':   
        restaurant = random.choice(restaurants)
        confirm_choice = input(f'We have selected {restaurant} as another dine out option. Does that work for you? ')
        if confirm_choice == 'NO':
            restaurant = random.choice(restaurants)
            confirm_choice = input(f'How about {restaurant}?')
        elif confirm_choice == 'YES':
            print(f'You selected {restaurant} as your dine out option! ')
            return restaurant
        else:
            print('Maybe later.')


def new_ent(confirm_choice):
    while confirm_choice != 'YES':
        entertainment = random.choice(entertainments)
        confirm_choice = input(f'We have selected {entertainment} as another entertainment option. Does that work for you?')
        if confirm_choice == 'NO':
            entertainment = random.choice(entertainments)
            confirm_choice = input(f'How about {entertainment}?')
        elif confirm_choice == 'YES':
            print(f'You selected {entertainment}. Sounds fun! ')
            return entertainment 
        else:
            print('Oh well.')



def new_trans(confirm_choice):
        while confirm_choice != 'YES':
            transportation = random.choice(transportations)
            confirm_choice = input(f'We have selected {transportation} as another transportation option. Does that work for you?')
            if confirm_choice == 'NO':
                transportation = random.choice(transportations)
                confirm_choice = input(f'How about {transportation}?')
            elif confirm_choice == 'YES':
                print(f'You selected {transportation} as your transportation option! ')
                return transportation 
            else:
                print(f'See you in the funny papers.')



# print(f'Your day trip is: {destination}, {restaurant}, {entertainment}, all en route by {transportation}! Have fun!')


destination = new_dest(destinations)
restaurant = new_rest(restaurants)
entertainment = new_ent(entertainments)
transportation = new_trans(transportations)

print(f'Your day trip is: {destination}, {restaurant}, {entertainment}, all en route by {transportation}! Have fun!')