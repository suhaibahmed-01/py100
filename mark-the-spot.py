row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = int(input("Where do you want to mark x in thr grid? "))

horizontal_position = (position[0])
vertical_position = (position[1])

map[vertical - 1] ="x"
map[horizontal - 1] = "x"

print(f"{row1}\n{row2}\n{row3}")


