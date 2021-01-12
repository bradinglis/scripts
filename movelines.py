
fp = open("input.txt", "r")

data = fp.read()

fp.close()

for i in range(50, 83):
    data.replace("+ " + str(i), "+ " + str(i + 20)

fp = open("output.txt", "w")
fp.write(data)
fp.close()
