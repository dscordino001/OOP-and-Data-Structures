# Dom Scordino
# CSC145B
# April 8, 2022
# Assignment 5

# this code creates a hash table that you can put, set, and remove items from

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        # size of the hash table
        self.size = 10
        # slots is none. for every value in the size of the table put in an empty slot
        self.slots = [None for i in range(self.size)]
        # accumulator for amounts of items in the table. since there are no items in the table
        self.count = 0

    def hash(self, key):
        mult = 1
        hash_value = 0
        for ch in key:
            hash_value += mult * ord(ch)
            mult += 1
        return hash_value % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        spot_in_ht = self.hash(key)

        # if spot spot_in_ht in the table is filled with something other than None
        while self.slots[spot_in_ht] is not None:
            # if the key we are trying to put in is already in that spot
            if self.slots[spot_in_ht].key is key:
                # get out of loop because it's already there
                break
                # if the spot is filled with a different key, add one to hash value to try the next slot
            spot_in_ht = (spot_in_ht + 1) % self.size

        # if spot spot_in_ht is filled with None
        if self.slots[spot_in_ht] is None:
            # add one to the total count of the items in the table
            self.count += 1
            # assign item object to the slot spot_in_ht in the table
            self.slots[spot_in_ht] = item

    def get(self, key):
        # value we got from hashing the key
        spot_in_ht = self.hash(key)
        # if spot spot_in_ht in the table is filled
        while self.slots[spot_in_ht] is not None:
            # if that spots key is the one we are looking for
            if self.slots[spot_in_ht].key is key:
                # return value of the slot
                return self.slots[spot_in_ht].value
        # because there's nothing in the table
        return None

    def remove(self, key):
        # value we got from hashing the key
        spot_in_ht = self.hash(key)
        # if spot spot_in_ht in the table is filled
        while self.slots[spot_in_ht] is not None:
            # if that spots key is the one we are looking for
            if self.slots[spot_in_ht].key is key:
                # set the slot to None
                self.slots[spot_in_ht] = None
                # set the count to go down by one
                self.count -= 1
            else:
                # if the spot is filled with a different key, add one to hash value to try the next slot
                spot_in_ht = (spot_in_ht + 1) % self.size

        # Pseudocode
        # get has value
        # while slot of hash value is not empty
            # if that slot's key is the key
                # set the slot to be None
                # decrease hash table's count by 1

            # if slots key is not the key
                # keep searching through the table

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

def print_items(table):
    # for a key regarding the 7 hash values listed below (good, better, etc.)
    for key in ("good", "better", "best", "worst", "ad", "foobarbar", "data"):
        key4table = table[key]
        print(key4table)
    print("\nThe number of elements is: {}\n".format(table.count))

ht = HashTable()
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["foobarbar"] = "collide"
ht["data"] = "value"

print_items(ht)
ht.remove("ad")
print_items(ht)

# UML DIAGRAM

# ---------------------------------|
# DTSHashTable                     |
# ---------------------------------|
# size                             |
# slots                            |
# count                            |
# ---------------------------------|
# __init__                         |
# hash(key)                        |
# put(key, value)                  |
# get(key)                         |
# remove(key)                      |
# __setitem__(key, value)          |
# __getitem__(key)                 |
# print_items(table)               |
# -------------------------------- |