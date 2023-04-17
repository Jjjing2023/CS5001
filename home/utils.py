"""
This module contains a function that takes a month and a date as input and returns
the corresponding astrological sign. It also contains two dictionaries
with information about the personality traits and a picture associated with each astrological sign.
"""


def get_astro_type(month, date):
    """
    This function takes a month and a date as input and returns the corresponding astrological.
    Args:
        month (int): The month of the date as an integer.
        date (int): The date of the month as an integer.
    Returns:
        str: The corresponding astrological sign as a string. If the date is invalid,
             returns "Invalid date".
    """
    if (month == 3 and date >= 21) or (month == 4 and date <= 19):
        return "Aries"
    elif (month == 4 and date >= 20) or (month == 5 and date <= 20):
        return "Taurus"
    elif (month == 5 and date >= 21) or (month == 6 and date <= 20):
        return "Gemini"
    elif (month == 6 and date >= 21) or (month == 7 and date <= 22):
        return "Cancer"
    elif (month == 7 and date >= 23) or (month == 8 and date <= 22):
        return "Leo"
    elif (month == 8 and date >= 23) or (month == 9 and date <= 22):
        return "Virgo"
    elif (month == 9 and date >= 23) or (month == 10 and date <= 22):
        return "Libra"
    elif (month == 10 and date >= 23) or (month == 11 and date <= 21):
        return "Scorpio"
    elif (month == 11 and date >= 22) or (month == 12 and date <= 21):
        return "Sagittarius"
    elif (month == 12 and date >= 22) or (month == 1 and date <= 19):
        return "Capricorn"
    elif (month == 1 and date >= 20) or (month == 2 and date <= 18):
        return "Aquarius"
    elif (month == 2 and date >= 19) or (month == 3 and date <= 20):
        return "Pisces"
    else:
        return "Invalid date"


"""
A dictionary that contains information about the personality traits associated with each astrological sign.
Keys(str): The name of the astrological sign.
Values(str): The personality traits associated with the astrological sign.
"""
astro_dict_desc = {
    "Aquarius": 'You are a forward-thinking and independent person who values freedom and individuality',
    'Pisces': 'You are a sensitive and imaginative person with a deep connection to your emotions and the '
              'world around you.',
    'Aries': 'You are a natural leader with a strong drive to succeed. You have a dynamic and competitive personality.',
    'Taurus': 'You are known for your stubbornness, but also for your loyalty and practicality. You have a deep '
              'appreciation for beauty and the finer things in life.',
    'Gemini': 'You are a curious and versatile person who loves to communicate and learn new things about the world.',
    'Cancer': 'You are a sensitive and intuitive person who values home and family above all else.',
    'Leo': 'You have a magnetic personality and a natural flair for the dramatic. You love to be the center of '
           'attention and have a strong sense of self.',
    'Virgo': 'You are an analytical and detail-oriented person with a strong sense of duty and responsibility.',
    'Libra': 'You have a strong sense of justice and a desire for harmony and balance. You are known for your '
             'charm and social grace.',
    'Scorpio': 'You are a passionate and intense person with a deep need for emotional connection and intimacy',
    'Sagittarius': 'You are an adventurous and free-spirited person who loves to explore and learn new things',
    'Capricorn': 'You are a practical and ambitious person with a strong sense of discipline and responsibility.'
}


"""
A dictionary that contains links to images of each astrological sign.
Keys(str): The name of the astrological sign.
Values(str): The URL of the image associated with the astrological sign.
"""
astro_dict_url = {
    "Aquarius": 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
                '//static.oprah.com/2018/04/201804-orig-best-mantra-aquarius-re-949x534.jpg',
    'Pisces': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
              '//static.oprah.com/2018/04/201804-orig-best-mantra-pisces-re-949x534.jpg',
    'Aries': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
             '//static.oprah.com/2018/04/201804-orig-best-mantra-aries-re-949x534.jpg',
    'Taurus': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
              '//static.oprah.com/2018/04/201804-orig-best-mantra-taurus-re-949x534.jpg',
    'Gemini': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
              '//static.oprah.com/2018/04/201804-orig-best-mantra-gemini-re-949x534.jpg',
    'Cancer': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
              '//static.oprah.com/2018/04/201804-orig-best-mantra-cancer-re-949x534.jpg',
    'Leo': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
           '//static.oprah.com/2018/04/201804-orig-best-mantra-leo-re-949x534.jpg',
    'Virgo': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
             '//static.oprah.com/2018/04/201804-orig-best-mantra-virgo-re-949x534.jpg',
    'Libra': 'https://static.oprah.com/2018/04/201804-orig-best-mantra-libra-949x534.jpg',
    'Scorpio': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
               '//static.oprah.com/2018/04/201804-orig-best-mantra-scorpio-re-949x534.jpg',
    'Sagittarius': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
                   '//static.oprah.com/2018/04/201804-orig-best-mantra-sagitarrius-re-949x534.jpg',
    'Capricorn': 'https://www.oprah.com/g/image-resizer?width=670&link=https:'
                 '//static.oprah.com/2018/04/201804-orig-best-mantra-capricorn-re-949x534.jpg'
}
