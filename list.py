blank_list = [] # Blank List

fruit_list = ["Apple" , "Mango" , "Strawberry"]

print(f"Length of the list is {len(fruit_list)}")

print(f"First Element: {fruit_list[0]}")
print(f"First Element: {fruit_list[2]} and also another way {fruit_list[-1]}")

fruit_list.append("Papaya")
print(fruit_list)

fruit_list.remove("Mango")

print(f"Update list: {fruit_list}")

fruit_list.sort()
print(f"Update list: {fruit_list}")

fruit_list.pop()
print(f"Updated list: {fruit_list}")

fruit_list.reverse()
print(f"Updated list: {fruit_list}")

fruit_list.clear()
print(f"Updated list: {fruit_list}")

