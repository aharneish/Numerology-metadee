def is_valid_date(date_str):
    """Check if the date string is in YYYY-MM-DD format and is a valid date."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
import datetime

# Mapping the english letters to pythogorean system to calculate the Destiny /Expression Number, Soul Urge, Personality Number etc
LETTER_VALUES={
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'I':9,
    'J':1,
    'K':2,
    'L':3,
    'M':4,
    'N':5,
    'O':6,
    'P':7,
    'Q':8,
    'R':9,
    'S':1,
    'T':2,
    'U':3,
    'V':4,
    'W':5,
    'X':6,
    'Y':7,
    'Z':8,
}
VOWELS=set("AEIOU")

def reduce_to_single_digit(n):
    while n>9 and n not in (11,22,33):
        n=sum(int(d) for d in str(n))
    return n

def get_life_path(dob):
    if not is_valid_date(dob):
        raise ValueError(f"Invalid date format or date: {dob}. Please use YYYY-MM-DD and ensure the date is valid.")
    digits = ''.join(dob.split('-')) #YYYYMMDD
    return reduce_to_single_digit(sum(int(d) for d in digits))

def get_destiny(name):
    total=sum(LETTER_VALUES.get(c,0) for c in name.upper() if c in VOWELS)
    return reduce_to_single_digit(total)

def get_soul_urge(name):
    total=sum(LETTER_VALUES.get(c,0) for c in name.upper() if c in VOWELS)
    return reduce_to_single_digit(total)

def get_numerology_profile(name,dob):
    if not is_valid_date(dob):
        raise ValueError(f"Invalid date format or date: {dob}. Please use YYYY-MM-DD and ensure the date is valid.")
    life_path = get_life_path(dob)
    destiny = get_destiny(name)
    soul_urge = get_soul_urge(name)
    master_numbers = {11, 22, 33}
    profile = {
        "name": name,
        "dob": dob,
        "life_path": life_path,
        "destiny": destiny,
        "soul_urge": soul_urge,
        "is_master": life_path in master_numbers or destiny in master_numbers or soul_urge in master_numbers
    }
    return profile