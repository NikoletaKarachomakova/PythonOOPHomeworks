def vowel_filter(function):
    def wrapper():
        letters = function()
        result = [l for l in letters if l.lower() in ['a', 'e', 'i', 'o', 'u']]
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
