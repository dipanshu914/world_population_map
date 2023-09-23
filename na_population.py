from pygal_maps_world.maps import World

wm = World()
wm.title = "Populations of Countries in North America and aisa"
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.add('asia', {'in': 1224615000, 'cn': 1338300000, 'pk': 173593000})

wm.render_to_file('na_populations.svg')


