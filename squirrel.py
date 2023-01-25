import pandas

squirrel_data = pandas.read_csv("Squirrel_Data.csv")
# print(squirrel_data)

list_of_color = ["Gray", "Cinnamon", "Black"]
color_count = []

for color in list_of_color:
    color_count.append(len(squirrel_data[squirrel_data["Primary Fur Color"] == color]))

squirrel_dict = {
    "squirrrel_color": list_of_color,
    "color_count": color_count
}

squirrel_data_table = pandas.DataFrame(squirrel_dict)
squirrel_data_table.to_csv("squirrel_count")
print(squirrel_data_table)







# color_data = list(squirrel_data["Primary Fur Color"])
# squirrel_color = list(set(color_data))
# print(squirrel_color)
# print(color_data)
#
#
# squirrel_color_dict = {}
# color_count_list = []
# for color in squirrel_color:
#     color_count_list.append(int(color_data.count(color)))
#
# print(color_count_list)
# # print(squirrel_color_dict)

# squirrel_table = pandas.DataFrame(squirrel_color_dict)


# squirrel_color = {'Gray': 2473,'Cinnamon': 392, 'Black': 103}
# squirrel_table = pandas.DataFrame(squirrel_color)


# Total_gray = color_data.count("Gray")
# print(Total_gray)


