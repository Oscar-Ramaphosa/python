
'''the hash table class'''
class HashTable:
    def __init__(self):
        self.maximum = 200
        self.array = [None for A in range(self.maximum)]

    '''This is a function that uses the division approach to obtain the hash function'''
    def hash(self, i):
        has = 0
        for char in i:
            has += ord(char)
        return has % self.maximum

    '''The setting a price value for each item function'''
    def __setitem__(self, t, value):
        A = self.hash(t)
        self.array[A] = value

    '''This is the retrieving price value function '''
    def __getitem__(self, i):
         A = self.hash(i)
         return self.array[A]

    '''The deleting a price values per item Function'''
    def __delitem__(self, t):
         A = self.hash(t)
         self.array[A] = None

''' Adding item to Hash Table'''
items = HashTable()
items["Boxy T-Shirt"] = 140
items["U Neck Tank"] = 220
items["Rib-Knit Sweater"] = 230
items["Gwyneth Cupro-Bllend Slip Dress"] = 230
items["Double-Breasted Jacket"] = 500
items["Padded Bomber Jacket"] = 500
items["Mason Pant"] = 1780
items["Full Length Pants"] = 350
items["Wide-Leg Pants"] = 370
items["Knee-High Boots"] = 700
items["Daybreak Sneaker"] = 1200
items["Ruched Midi Dress"] = 1150
items["Baller Flats in Leather"] = 50
items["Laguna Waterproof boot"] = 1700
items["Measa Pleated Woven Whide-Leg Cargo Pants"] = 2100
items["Oversized Single Breasted Jacket"] = 755
items["Louisa Lady Jacket in Maritime Tweed"] = 3500

'''Printing out few items'''
print("U Neck Tank : " + str(items.hash("U Neck Tank")))
print("Rib-Knit Sweater : " + str(items.hash("Rib-Knit Sweater")))
print("Double-Breasted Jacket : " + str(items.hash("Double-Breasted Jacket")))
print("Padded Bomber Jacket : " + str(items.hash("Padded Bomber Jacketk")))
print("Mason Pant : " + str(items.hash("Mason Pant")))
print("Daybreak Sneaker : " + str(items.hash("Daybreak Sneaker")))
print("Oversized Single Breasted Jacket : " + str(items.hash("Oversized Single Breasted Jacket")))


