def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

strings = [
    "0974101607733149676776769413377061014790",
    "2704702208931031198668911301398022074072",
    "4257304920394478392772938744930294037524",
    "7798338247658278460338648728567428338977"
]

not_palindromes = []
for string in strings:
    if not palindrome(string):
        not_palindromes.append(string)

print("Strings that are NOT palindromes:", not_palindromes)
