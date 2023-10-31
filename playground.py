import collections.abc  # Import from collections.abc

my_dict = {'key1': 'value1', 'key2': 'value2'}

# Check if it's a mapping object using collections.abc.Mapping
if isinstance(my_dict, collections.abc.Mapping):
    print('my_dict is a mapping object')
else:
    print('my_dict is not a mapping object')
