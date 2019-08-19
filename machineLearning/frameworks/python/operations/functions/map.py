# Mapping functions in python

# create a python list
component = ['plant computer', 'soft drones', 'web service']

# map the components
mapped = map(lambda x: 'component: ' + x, component)
for component in mapped:
    print(component)

