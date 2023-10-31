def find_all_occurrences(haystack, needle):
    start = 0
    occurrences = []

    while start < len(haystack):
        start = haystack.find(needle, start)

        if start == -1:
            break

        occurrences.append(start)
        start += len(needle)

    return occurrences

haystack = 'sadbutsad'
needle = 'sad'
print(find_all_occurrences(haystack, needle))
