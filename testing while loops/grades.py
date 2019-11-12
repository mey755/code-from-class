def main():
    gradesFile = open("grades.txt", "r")

    # for line in gradesFile:
    #     print(line)

    count = 0
    theSum = 0
    line = gradesFile.readline().rstrip()
    # if there's nothing to read on the next file it reads nothing, no more lines are readable

    #checking no longer for "" lines but the word -END- and excepts blank linefeed
    while line != "-END-":
        student = line.split(",")
        theSum += float(student[1])
        count += 1
        print(line.rstrip())
        #this is a readable string
        line = gradesFile.readline().rstrip()
    print(theSum/count)

    gradesFile.close()

main()


