"""

Inventory Update

Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. Update the
current existing inventory item quantities (in arr1). If an item cannot be found, add the new item and quantity
into the inventory array. The returned inventory array should be in alphabetical order by item.

"""

def updateInventory(arr1, arr2):

    items_dict = {item: quantity for quantity, item in arr1}
    answer = []
    for item in arr2:
        if item[1] in items_dict.keys():
            items_dict[item[1]] += item[0]
        else:
            items_dict[item[1]] = item[0]

    for key, value in items_dict.items():
        answer += [[value, key]]

    return answer


print(updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]))
print(updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], []))
print(updateInventory([], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]))
print(updateInventory([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]))