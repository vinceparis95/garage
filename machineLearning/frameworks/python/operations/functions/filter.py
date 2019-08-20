# Filtering functions in python

# create a list of components
component = ['plant computer', 'soft drones', 'tf_js service']

# filter the list with a value
filtered = filter(lambda x: x == 'soft drones', component)
for component in filtered:
    print(component)

