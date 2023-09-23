from pygal_maps_world.maps import World

# Create a world map object
worldmap = World()

# Set the title of the map
worldmap.title = 'Countries of the World'

# Add data to the map
worldmap.add('North America', ["ca", 'us', 'mx'])  # Canada, USA, Mexico
worldmap.add('Central America', ["bz", 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
worldmap.add('south America', ["ar", 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe',
                               'py', 'sr', 'uy', 've'])
worldmap.add('asia', ['in', 'pk', 'cn'])

# Render the map to an SVG file
worldmap.render_to_file('countries_map.svg')
