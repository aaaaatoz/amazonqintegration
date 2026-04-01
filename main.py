def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_item(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1


def reverse_string(s):
    return s[::-1]


def count_words(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    print(calculate_average([10, 20, 30]))
    print(find_item(["apple", "banana", "cherry"], "banana"))
    print(reverse_string("hello"))
    print(count_words("the cat sat on the mat the cat"))
