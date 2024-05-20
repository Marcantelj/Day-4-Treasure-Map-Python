line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Column A through C and Row 1 through 3: Example B3\n ") # Where do you want to put the treasure? Column A through C and Row 1 through 3.

#Gets the line 1-3
columnIndex = int(position[1])

#Gets the position in the line A = 0 B = 1 C = 2 
if position[0] == "A":
  rowIndex = 0
elif position[0] == "B":
  rowIndex = 1
else:
  rowIndex = 2

#puts an X at the map position
map[columnIndex - 1][rowIndex] = "X"

#prints the map with treasure location
print(f"{line1}\n{line2}\n{line3}")