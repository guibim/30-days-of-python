#exc 1
import random
import string

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    user_id = ''.join(random.choices(characters, k=6))
    return user_id

print(random_user_id())



#exc 2
def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters per ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))
    characters = string.ascii_letters + string.digits

    for _ in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_chars))
        print(user_id)

user_id_gen_by_user()


def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

#lv 2
# 1️ Generates a list of random HEX colors
def list_of_hexa_colors(num):
    colors = []
    for _ in range(num):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(hex_color)
    return colors


# 2️ Generates a list of random RGB colors
def list_of_rgb_colors(num):
    colors = []
    for _ in range(num):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r},{g},{b})")
    return colors


# 3 Generates either HEX or RGB colors depending on user's choice
def generate_colors(color_type, num):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(num)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return "Invalid color type. Choose 'hexa' or 'rgb'."

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

#lv3 
# 1️ Shuffle a list
def shuffle_list(lst):
    shuffled = lst[:]       # copy the original list
    random.shuffle(shuffled)
    return shuffled


print(shuffle_list([1, 2, 3, 4, 5, 6, 7]))


# 2️ Generate seven unique random numbers (0–9)
def unique_random_numbers():
    return random.sample(range(10), 7)

8
print(unique_random_numbers())