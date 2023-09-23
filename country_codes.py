from pygal_maps_world import i18n


def get_country_code(country_name):
    # Return the pygal 2-digit country codes for the given country.

    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code

    # if the country code wasn't found, return none.
    return None


""" print(get_country_code("Andorra"))
print(get_country_code("United Arab Emirates"))
print(get_country_code("India"))
print(get_country_code("Russian Federation"))"""




