# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))


# f = open("demo.txt", "rt")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)
# f.close()

# f = open("demo.txt", "w")
# data = f.write("I am going to learn Modern Python.")
# print(data)

# with open("demo.txt", "w")as f:
#     data = f.write("new data")
#     print(f" Here ia the updates file: {data}.")

def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt", "r")as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(check_for_line())   