def count_substring_occurances(string, substring):
    '''returns number of times substring occurs in string using sliding window approach'''
    count = 0
    start = 0
    substring_index = 0

    for end in range(len(string)):

        # slide open window
        if string[end] == substring[substring_index]:
            substring_index += 1
        else:
            substring_index = 0
            start = end  # slide close window
        
        # if window is opened to size of substring, it means substring is found
        if end - start + 1 == len(substring):
            count += 1
            start += 1
            substring_index -= 1

    return count


print(count_substring_occurances('GCGCG', 'GCG'))
# print(f"correct answer: {3}")
# print("GCGCG".count("GCG"))
print(count_substring_occurances('AAAA', 'AAA'))
# print(f"correct answer: {2}")
print(count_substring_occurances('AAAA', 'AA'))
# print(f"correct answer: {3}")
print(count_substring_occurances('AAAA', 'A'))
