stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley") 
#prints ['Croy', 'Cumbernauld', 'Falkirk High', 'Linlithgow', 'Livingston', 'Haymarket', 'Edinburgh Waverley']

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St") 
#prints ['Glasgow Queen St', 'Croy', 'Cumbernauld', 'Falkirk High', 'Linlithgow', 'Livingston', 'Haymarket', 'Edinburgh Waverley']

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont") 
#prints ['Glasgow Queen St', 'Croy', 'Cumbernauld', 'Falkirk High', 'Polmont', 'Linlithgow', 'Livingston', 'Haymarket', 'Edinburgh Waverley']

#4. Print out the index position of "Linlithgow"
print(stops.index("Linlithgow")) 
#prints 5

#5. Remove "Livingston" from the list using its name
stops.remove("Livingston") 
#prints ['Glasgow Queen St', 'Croy', 'Cumbernauld', 'Falkirk High', 'Polmont', 'Linlithgow', 'Haymarket', 'Edinburgh Waverley']

#6. Delete "Cumbernauld" from the list by index
stops.pop(2) 
#prints ['Glasgow Queen St', 'Croy', 'Falkirk High', 'Polmont', 'Linlithgow', 'Haymarket', 'Edinburgh Waverley']

#7. Print the number of stops there are in the list
print(len(stops)) 
#prints 7

#8. Sort the list alphabetically
stops.sort() 
#prints ['Croy', 'Edinburgh Waverley', 'Falkirk High', 'Glasgow Queen St', 'Haymarket', 'Linlithgow', 'Polmont']

#9. Reverse the positions of the stops in the list
stops.sort(reverse = True) 
#prints ['Polmont', 'Linlithgow', 'Haymarket', 'Glasgow Queen St', 'Falkirk High', 'Edinburgh Waverley', 'Croy']

#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)
#prints:
# Polmont
# Linlithgow
# Haymarket
# Glasgow Queen St
# Falkirk High
# Edinburgh Waverley
# Croy 