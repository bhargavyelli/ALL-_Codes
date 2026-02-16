with open("data_log.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        if  "ERROR" in line:
            print(line) 