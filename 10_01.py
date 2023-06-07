
# s = "breakCamelCase"



# def func(s):
#     result = ""
#     for i in s:
#         if i.isupper():
#             result += " " + i
#         else:
#             result += i
#     return result
# print(func(s))

name = "bravo"
def are_you_playing_banjo(name):
    # if name[0].lower() == 'r':
    #     return name + " plays banjo"
    # else:
    #     return name + " does not play banjo"
    return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"
print(are_you_playing_banjo(name))