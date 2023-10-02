
'''creating  a function that uses recursion'''
def string_permuation(t):
    '''A function that will be used by the string_permuation'''
    def Check(t,charac):
        '''Return the empty results if the string is empty'''
        if not t:
            return ""
        # t has only one character, and if the character is not in the charac,
        # the character has already been seen.
        elif t[0] in charac:
            '''Return the results of the sub problem'''
            return Check(t[1:], charac)
        else:
            return t[0] + Check(t[1:], {*charac, t[0]})
    return Check(t, set())

'''Run the Function string_permulation using few different names
with the non-repetative character'''
print("1: " + string_permuation("eunice"))
print("2: " + string_permuation("michelle"))
print("3: " + string_permuation("Mutefe"))
print("4: " + string_permuation("character"))
print("5: " + string_permuation("institution"))