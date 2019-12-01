import json
from pygal.maps import world
from pygal.style import RotateStyle
from country_codes import get_country_code


filename = 'gdp_json.json'

with open(filename) as f:
    gdp_data = json.load(f)


cc_gdp = {}
for gdp_dict in gdp_data:
    country_name = gdp_dict['Country']
    gdp = int(gdp_dict['GDP(nominal 2017)'].replace('$', ''))
    code = get_country_code(country_name)
    if code:
        cc_gdp[code] = gdp
    else:
        print('ERROR - ' + country_name)


wm_style = RotateStyle('#336699')
wm = world.World(style=wm_style)
wm.title = 'World GDP in 2017, by Country'
wm.add('2017', cc_gdp)
wm.render_to_file('world_gdp.svg')
