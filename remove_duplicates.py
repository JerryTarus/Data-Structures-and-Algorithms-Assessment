#### ---Jerry Tarus--- ####

def remove_duplicates(sequence):
    watever = set()
    result = []

    for item in sequence:
        if item not in watever:
            result.append(item)
            watever.add(item)

    return result

# See if this is working

sample_numbers = [2000, 3002, 2300, 47, 53, 3002, 601, 715, 512]
result = remove_duplicates(sample_numbers)
print(result)  


#### ---Jerry Tarus--- ####