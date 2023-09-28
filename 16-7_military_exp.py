"""import csv

from pygal_maps_world.maps import World
from country_codes import get_country_code

filename = "military expenditure.csv"
with open(filename) as f:
    Reader = csv.reader(f)
    # header_row = next(Reader)

    # print(header_row[])
    # skip the first four rows
    for _ in range(4):
        next(Reader)

    # Now, you are at line 5 which contains the column headers
    header_row = next(Reader)

    """""" 
    # print the column header
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Find the index of the column containing "Country Name"
    country_name_index = header_row.index("Country Name")

    # Initialize a list to store the country names
    country_names = []

    # iterate through the rows in the CSV file, starting from line 6 (index 5),
    # and extract the country names
    for row in Reader:
        country_name = row[country_name_index]
        country_names.append(country_name)

    # print the list of country names
    for index, country_name in enumerate(country_names):
        print(index, country_name) """""""

    # Build a dictionary of a population data
    cc_military_exp = {}

    # creating dict. to store 2010 military exp.
    for row in Reader:
        country_name = row[5]
        military_exp = row[55]

        # Check if the military expenditure value is not empty
        if military_exp and military_exp != "":
            try:
                military_exp = int(float(military_exp))
                code = get_country_code(country_name)
                if code is not None:
                    cc_military_exp[code] = military_exp
                    print(code + ":" + str(military_exp))
                else:
                    print("Error:", country_name)
            except ValueError:
                # Handle invalid or non-numeric values gracefully
                print("Invalid military expenditure value : ", military_exp)

# Create a pygal world map
wm = World()
wm.title = "Military Expenditure 2010(USD)"
wm.add("2010", cc_military_exp)

# Render the map to svg file
wm.render_to_file("military_exp_2010.svg") """










