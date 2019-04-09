import random

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
weather_styles = ['snowy', 'rainy', 'sunny', 'foggy']

pick_weekday = random.choice(weekdays)

random.choice(weekdays)

print('Today is ' + pick_weekday + ' and it is: ' + random.choice(weather_styles))

#for day in weekdays:
#    print('Today is ' + day + ' and it is: ' + random.choice(weather_styles))

