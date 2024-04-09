def pepper_data(input_string):
    """Adds noise to the input string."""
    return "".join([chr(ord(c) + 2) for c in input_string])

def unpepper_data(input_string):
    """Removes noise from the input string."""
    return "".join([chr(ord(c) - 2) for c in input_string])

def sprinkle_salt(input_list):
    """Transforms string into a list with added elements."""
    return [ord(c) + 1 for c in input_list]

def wash_salt(input_list):
    """Reverts the transformation of the list back into a string."""
    return "".join([chr(c - 1) for c in input_list])

def cut_vegetables(text):
    """Splits text into even and odd indexed characters."""
    even_chars = text[::2]
    odd_chars = text[1::2]
    return even_chars, odd_chars

def mix_ingredients(even_chars, odd_chars):
    """Recombines characters into a single string."""
    return ''.join(e + o for e, o in zip(even_chars, odd_chars + ' '))

def prepare_dish(input_string):
    """Main function to encrypt the input string."""
    mixed = mix_ingredients(*cut_vegetables(input_string))
    salted = sprinkle_salt(mixed)
    final_dish = pepper_data(salted)
    return final_dish

def taste_dish(input_string):
    """Main function to decrypt the input string."""
    tasted = unpepper_data(input_string)
    unsalted = wash_salt(tasted)
    original_flavor = mix_ingredients(*cut_vegetables(unsalted))
    return original_flavor