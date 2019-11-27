def get_city_country(city, country, population=''):
    if population:
        city_country = city + ', ' + country
        city_population = ' - population ' + population
        return city_country.title() + city_population
    else:
        city_country = city + ', ' + country
        return city_country.title()
