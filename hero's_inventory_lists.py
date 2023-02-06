# Hero's Inventory
# Demonstrates Lists

# create a list with some items and display a for loop.

inventory = ["Sword", "armor", "shield", "healing potion"]
print("Your items.")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")

# get the length of a list
#len function returns the number of items in an object
print("You have", len(inventory), "items in your posession.")

input("\nPress the enter key to continue.")

#test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# 
