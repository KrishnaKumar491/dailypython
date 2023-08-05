
def capital_indexes(s):
    return [index for index, char in enumerate(s) if char.isupper()]

check=capital_indexes("HeLlO")
print(check)
