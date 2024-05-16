import pandas

# frames and content for export

recipe_dict = {
    "Ingredient": ["Flour", "Eggs", "Milk"],
    "Quantity": [2, 3, 50],
    "Weight": ["Kg", "pieces", "mL"],
    "Price": [5, 12, 3]
}

recipe_frame = pandas.DataFrame(recipe_dict)

# change frame to a string so that we can export it to file
recipe_txt = pandas.DataFrame.to_string(recipe_frame)

recipe_name = "chunky eggs test"
serving_size = "4"

to_write = [recipe_name, serving_size, recipe_txt]

# write output to file
# create file to hold data (add .txt extension)
file_name = f"{recipe_name}.txt"
text_file = open(file_name, "w+")

# heading
# print output
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# close file
text_file.close()

# Print stuff
for item in to_write:
    print(item)
    print()
