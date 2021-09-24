print('Day 3')
print()

friend_1_name = 'Mykhailo Hupalo'
friend_1_email = 'mykhailo.hupalo@example.com'
friend_1_age = 42
friend_1_the_best = True

friend_2_name = 'Maria Nepyivoda'
friend_2_email = 'maria.nepyivoda@example.com'
friend_2_age = 36
friend_2_the_best = False

friend_3_name = 'Tetiana Cheh'
friend_3_email = 'tetiana.cheh@example.com'
friend_3_age = 29
friend_3_the_best = True

friend_4_name = 'Bogdan Gutsulyak'
friend_4_email = 'bohdan.gutsulyak@example.com'
friend_4_age = 33
friend_4_the_best = True

friend_5_name = 'Ivan Petrov'
friend_5_email = 'ivan.petrov@example.com'
friend_5_age = 57
friend_5_the_best = False

friend_1 = [friend_1_name, friend_1_email, friend_1_age, friend_1_the_best]
friend_2 = [friend_2_name, friend_2_email, friend_2_age, friend_2_the_best]
friend_3 = [friend_3_name, friend_3_email, friend_3_age, friend_3_the_best]
friend_4 = [friend_4_name, friend_4_email, friend_4_age, friend_4_the_best]
friend_5 = [friend_5_name, friend_5_email, friend_5_age, friend_5_the_best]
friends = [friend_1, friend_2, friend_3, friend_4, friend_5]
for item in friends:
    print(f'"{item[0]}, {item[2]} years old. Email: {item[1]}"')
print()
for item in friends:
    if item[3] == True:
        print(f'"My best friend {item[0]}, {item[2]} years old. Email: {item[1]}"')
print()

phone_numbers = ['38ab725877', 'agchbab725877', '3809625338', '3806318349', '3806/18349', '3,14159265', '3806725877']
for item in phone_numbers:
    if len(item)==10 and item.isnumeric():
        print(f'{item} is a valid phone number')
    else:
        print(f'{item} is not a phone number') 