import json
import webbrowser

f = open("tree.json","r")
tree = json.loads(f.read())
f.close()

#get to the next node of the tree
def getNextLevel(tree, input):
    input = int(input)
    nextLevelTree = tree[input]
    return nextLevelTree


#sort the list by imdbRating
def sortList(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(list[j]["imdbRating"]) < float(list[j+1]["imdbRating"]):
                list[j], list[j+1] = list[j+1], list[j]


#user interactive design
while True:
    print("Welcome!")
    print(tree[0])
    while True:
        userInputR = input("Please enter 1, 2 or exit: ")
        if userInputR == "exit":
            print("Bye!")
            quit()
        elif userInputR.isnumeric():
            if int(userInputR) != 1 and int(userInputR) != 2:
                print("Please enter a valid number.")
                continue
            else:
                secTree = getNextLevel(tree, userInputR)
                print(secTree[0])
                while True:
                    userInputY = input("Please enter 1, 2, 3, back or exit: ")
                    if userInputY == "exit":
                        print("Bye!")
                        quit()
                    elif userInputY == "back":
                        print("Back to previous menu...")
                        print(tree[0])
                        break
                    elif userInputY.isnumeric():
                        validNumberY = [1,2,3]
                        if int(userInputY) not in validNumberY:
                            print("Please enter a valid number.")
                            continue
                        else:
                            thirdTree = getNextLevel(secTree, userInputY)
                            print(thirdTree[0])
                            while True:
                                userInputG = input("Please enter number between 1~11, back or exit: ")
                                if  userInputG == "exit":
                                    print("Bye!")
                                    quit()
                                elif userInputG == "back":
                                    print("Back to previous menu...")
                                    print(secTree[0])
                                    break
                                elif userInputG.isnumeric():
                                    validNumberG = [1,2,3,4,5,6,7,8,9,10,11]
                                    if int(userInputG) not in validNumberG:
                                        print("Please enter a valid number.")
                                        continue
                                    else:
                                        movieList = getNextLevel(thirdTree, userInputG)
                                        sortList(movieList)
                                        i = 0
                                        if len(movieList) == 0:
                                            print("There is no movie of your choice in the library.")
                                            continue
                                        elif len(movieList) >= 10:
                                            print("Below is the top 10 movie of your choice: ")
                                            while i < 10:
                                                print(i+1, "<<",movieList[i]["Title"], ">>","   (imdbRating: ", movieList[i]["imdbRating"],")","    [", movieList[i]["Runtime"], "]")
                                                i += 1
                                        elif len(movieList) < 10:
                                            print("There are less than 10 movies, below is all the movies of your choice: ")
                                            while i < len(movieList):
                                                print(i+1, "<<",movieList[i]["Title"], ">>","   (imdbRating: ", movieList[i]["imdbRating"],")","    [", movieList[i]["Runtime"], "]")
                                                i += 1
                                        while True:
                                            print("Please select the movie you want to preview.")
                                            userIn = input("Enter the number before the movie title, back or exit: ")
                                            if userIn == "exit":
                                                print("Bye!")
                                                quit()
                                            elif userIn == "back":
                                                print("Back to previous menu...")
                                                print(thirdTree[0])
                                                break
                                            elif userIn.isnumeric():
                                                validMaxInput = min([len(movieList), 10])
                                                if int(userIn) < 1 or int(userIn) > validMaxInput:
                                                    print("Please enter a valid input.")
                                                    continue
                                                else:
                                                    print()
                                                    print("Below is the information of the movie: ")
                                                    print("******************************")
                                                    print("The plot of the movie: ")
                                                    print(movieList[int(userIn)-1]["Plot"])
                                                    print()
                                                    print("The rated of the movie: ")
                                                    print(movieList[int(userIn)-1]["Rated"])
                                                    print()
                                                    print("The poster of the movie: ")
                                                    print(movieList[int(userIn)-1]["Poster"])
                                                    if movieList[int(userIn)-1]["Poster"] == "N/A":
                                                        print("There is no poster of the movie.")
                                                    else:
                                                        print("Launching...")
                                                        webbrowser.open(movieList[int(userIn)-1]["Poster"], new=2)
                                                    print("*****************************.")
                                                    print()
                                                    continue
                                            else:
                                                print("Please input a valid input.")
                                                continue
                                else:
                                    print("Please input a valid input.")
                                    continue
                    else:
                        print("Please input a valid input.")
                        continue
        else:
            print("Please input a valid input.")
            continue
