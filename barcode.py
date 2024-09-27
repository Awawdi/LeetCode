####
# A barcode scanner can be configured by scanning a series of barcodes in the correct order.
# The encoded configuration string is a series of <ordinal-index><configuration> pairs separated by |.
# The goals are to
# 1) validate the configuration string and
# 2) provide the configuration client the configuration values in the order required to successfully configure the barcode scanner.

# Validation conditions
# All configurations must be separated by a "|" character.
# Configuration value length is exactly 10 characters.
# Configurations cannot skip a number in the ordering. If there are three configuration strings, there must be a 1, 2, and 3 Index
# Ordinal indices may not repeat, for example there cannot be two occurrences of the number "1".
# Each configuration value is unique, configurations do not repeat. • "0000" is not a valid ordinal Index.
# If a configuration string is not valid, return ["Invalid configuration"],

# Examples
# "0002f7c22e7904|000176a3a4d214|000305d29f4a4b"
# Based on the order value, the expected output of this configuration string is:
# ['76a3a4d214', 'f7c22e7904', '05d29f4a4b']
####

def ordered_configuration(configuration:str)->list[str]:
    configs = configuration.split('|')
    map_of_values={}
    set_of_values=set()

    for config in configs:

        o_index = config[:4]
        c_value = config[4:]

        # Validation part
        if len(o_index) != 4 or not o_index.isdigit() or o_index == "0000":
            return ["Invalid configuration"]

        if len(c_value) != 10 or not c_value.isalnum():
            return ["Invalid configuration"]

        if c_value in set_of_values:
            return ["Invalid configuration"]

        set_of_values.add(c_value)
        map_of_values[int(o_index)] = c_value

    ordinal_indices = sorted(map_of_values.keys())
    for i in range(1, len(ordinal_indices) + 1):
        if ordinal_indices[i - 1] != i:
            return ["Invalid configuration"]

    return [map_of_values[i] for i in ordinal_indices]

if __name__ == '__main__':

    configurations = input("Enter configurations:").strip()
    result = ordered_configuration(configurations)
    print(result)