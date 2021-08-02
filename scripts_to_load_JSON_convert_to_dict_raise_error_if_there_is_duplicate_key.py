#For references https://github.com/realpython/python-scripts/blob/master/scripts/05_load_json_without_dupes.py

def dict_raise_on_duplicates(ordered_pairs):
    """reject duplicate keys"""
    my_dict = dict()
    for key, values in ordered_pairs:
        if key in my_dict:
            raise ValueError("Duplicate key: {}".format(key,))
            else: my_dict[key] = values
            return my_dict