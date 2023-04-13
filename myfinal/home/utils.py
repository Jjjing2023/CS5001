

def get_astro_type(month, date):
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


# def get_astro_detail(astro_type):
#     # Return the description and icon for the given astrological sign
#     return astro_dict[astro_type]['description'], astro_dict[astro_type]['icon_url']
