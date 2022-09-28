


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

print (day_trip)
confirm_choice = input('Please enter y/n to confirm these travel options.')

