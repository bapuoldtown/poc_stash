def greet_english():
    return "Hello World!!!"


def greet_hindi():
    return "Namastey Bharat!!"


def greet_german():
    return "Guten Morgen World!!"


def dictionary_update():
    return {**{"guru": "oldtown"}, **{"krisha": "bangalore"}}


if __name__ == '__main__':
    print(greet_english())
    print(greet_hindi())
    print(greet_german())
    print(dictionary_update())