import json

from country_codes import get_country_code
from pygal_maps_world.maps import World
# from pygal.style import RotateStyle as RS

filename = "global_gdp.json"
with open(filename) as f:
    gdp_data = json.load(f)

    """ for index, country in enumerate(gdp_data, 1):
        print(index, country) """

cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict["Year"] == "2014":
        country_name = gdp_dict["Country Name"]
        gdp = int(float(gdp_dict["Value"]))

        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp

# groups the country in 3 level
# less than 5 billion,less than 50 billion, >=50 billion
# Also convert to billions for displaying values

cc_gdp_1, cc_gpd_2, cc_gdp_3 = {}, {}, {}
for cc, gdp in cc_gdp.items():
    if gdp < 5000000000:
        cc_gdp_1[cc] = round(gdp/1000000000)
    elif gdp < 50000000000:
        cc_gpd_2[cc] = round(gdp/1000000000)
    else:
        cc_gdp_3[cc] = round(gdp/1000000000)

# See how many country are in each level
print(len(cc_gdp_1), len(cc_gpd_2), len(cc_gdp_3))


# wm_style = RS('#336699')
wm = World()
wm.title = "2014 - countries gdp data"
wm.add("0 to 5bn", cc_gdp_1)
wm.add("5bn to 50bn", cc_gpd_2)
wm.add("above 50bn", cc_gdp_3)
wm.render_to_file("worlds_gdp_2014.svg")
