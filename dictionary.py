# Empty dictionary 
my_dict = {}

#Dictionary with number keys

my_dict1 = {1:"Strawberry",
            2: "Mango",
            3: "Pinapple"}

my_dict_mix = {
    "name" : "Aleem",
    50: [6,5,5,5,7,2,6,6,6,2]
}

#Output or accessing specific element
print(my_dict_mix["name"])
print(my_dict_mix.get("name")) # That is another way of the line num.16

# Update or add values
my_dict["School"] = "Averroes International School"
print(my_dict) 