#match statements with guard statements
#They are extra conditions -add if

age = 20

match age:
    case x if x < 18:
        print("Minor")
    case x if x >= 18:
        print("Adult")
