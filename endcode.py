file = open("file.edc", "r", 1, "utf-8")
raw_data = file.readlines()
for string in raw_data:
    if string != "\n" or string != "":

        print(string)
