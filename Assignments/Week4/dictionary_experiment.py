if __name__ == "__main__":
    inventory ={}

    inventory["Amul"] = ["Mystic Mocha",55]
    print(inventory)
    inventory["Amul, Mystic Mocha"] = 55
    # print(inventory)
    # inventory[["Amul", "Mystic Mocha"]] = 55
    print(inventory)
    inventory[("Amul","Mystic Mocha")] = 55
    print(inventory)

    marks = {"Quizzes":{"Mahesh":[3,5,7,8],"Suresh":[9,4,8,8],"Uma":[9,9,7,6]},"Exams":{"Mahesh":[37],"Uma":[36]}}
    # marks["Exams"]["Suresh"][0:] = [44]
    # print(marks)
    # marks["Exams"]["Suresh"].append(44)
    # print(marks)
    marks["Exams"]["Suresh"] = [44]
    print(marks)
    marks["Exams"]["Suresh"].extend([44])
    print(marks)

    runs = {"Test":{"Rahul":[90,14,35],"Kohli":[3,103,73,42],"Pujara":[53,15,133,8]},"ODI":{"Sharma":[37,99],"Kohli":[63,47]}}
    # runs["ODI"]["Rahul"].append([74])
    # runs["ODI"]["Rahul"].extend([74])
    # runs["ODI"]["Rahul"][0]=74
    runs["ODI"]["Rahul"]=[74]


