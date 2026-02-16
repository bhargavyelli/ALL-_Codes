with open("data_log.txt","r") as file:
    content = file.read()
    print("Number of times Info occurs:",content.count("INFO"))
    print("Number of times DEBUG occurs:",content.count("DEBUG"))
    print("Number of times WARNING occurs:",content.count("WARNING"))
    print("Number of times ERROR occurs:",content.count("ERROR"))
