# jhkjhk


def get_count(s):
    counts = {}
    for c in s:
        if c in counts: 
            counts[c] += 1
        else: 
            counts[c] = 1
    return counts

def get_counts(s):
    return (get_count(s[::2]), get_count(s[1::2]))

def twins(a, b):
    returnedArray = []
    counter = 0
    for i in a:
        if len(a) != len(b) and counter == min(len(a), len(b)):
            for i in range(0, abs(len(a) - len(b))):
                returnedArray.append("No")
            return returnedArray
        elif get_counts(a[counter]) == get_counts(b[counter]):
            returnedArray.append("Yes")
        else:
            returnedArray.append("No")
        counter += 1
    return returnedArray

