def find_bob_occurrences(text):
    count = 0
    index = 0

    while index < len(text):
        bob_index = text.find("Bob", index)

        if bob_index == -1:
            break

        if text[index:bob_index].startswith("b"):
            count += 1

        index = bob_index + 3

    return count


text = "bYellowBob, bBlueBob, dBobBob"
print(find_bob_occurrences(text))
