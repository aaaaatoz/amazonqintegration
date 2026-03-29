def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    if not numbers:
        return 0
    return total / len(numbers)


def find_item(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def reverse_string(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result


def count_words(sentence):
    words = sentence.split(" ")
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


if __name__ == "__main__":
    print(calculate_average([10, 20, 30]))
    print(find_item(["apple", "banana", "cherry"], "banana"))
    print(reverse_string("hello"))
    print(count_words("the cat sat on the mat the cat"))
