full_dot = '●'
empty_dot = '○'


def create_stat(stat_points):
    total_points = 10
    points = full_dot * stat_points
    remaining_points = empty_dot * (total_points - stat_points)

    return points + remaining_points


def create_character(char_name, strength, intelligence, charisma):

    
    if not isinstance(char_name, str):
        return "The character name should be a string"
    if len(char_name) > 10:
        return "The character name is too long"
    if " " in char_name:
        return "The character name should not contain spaces"

    if type(strength) is not int or type(intelligence) is not int or type(charisma) is not int:
        return "All stats should be integers"

    
    if (strength < 1) or (intelligence < 1) or (charisma < 1):
        return "All stats should be no less than 1"

    if (strength > 4) or (intelligence > 4) or (charisma > 4):
        return "All stats should be no more than 4"
    
    sum_of_stats = strength + intelligence + charisma
    
    if sum_of_stats != 7:
        return "The character should start with 7 points"
    
    str_points = create_stat(strength)
    int_points = create_stat(intelligence)
    cha_points = create_stat(charisma)

    
    return (f"{char_name}\n"
    f"STR {str_points}\n"
    f"INT {int_points}\n"
    f"CHA {cha_points}")

print(create_character("ren", 4, 2, 1))