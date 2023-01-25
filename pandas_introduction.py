import pandas
#
# def convert_c_to_f(temperature_in_c):
#     f_temp = (temperature_in_c*1.8) + 32
#     return f_temp


# weather_data = pandas.read_csv("/Users/hgaje/PycharmProjects/Day_25_project/weather_data.csv")
# print(weather_data)
# print(weather_data['temp']) or print(weather_data.temp) # Both has same effect

# print(weather_data[1:2])
# print(weather_data[weather_data.day == "Tuesday"])


# print(weather_data[weather_data.temp == weather_data.temp.max()])

# Monday_data = weather_data[weather_data.day == "Monday"]
# C_temp = (Monday_data.temp)
# F_temp = convert_c_to_f(C_temp)
# print(F_temp)


# Create data from scratch
my_score_dict = {
    "student_names": ["Harshal", "Kunal", "Manish"],
    "score": ["89", "87", "92"]
}
score = pandas.DataFrame(my_score_dict)
score.to_csv("score")

# name_score_list = [["student_names", "Harshal", "Kunal", "Manish"], ["score", "89", "87", "92"]]
# print(pandas.DataFrame(name_score_list))


