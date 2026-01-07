# Match Statements (compare values against multiple statements)(Instead of using many if else conditions)

flower="rose"
match flower:
    case "tulip":
        print("pink")
    case "rose":
        print("red")
    case "lily":
        print("white")
    case _:
        print("yellow")


#multiple values in one case(|)
day=3
match day:
    case 1|2|3|4|5:
        print("Weekday")
    case 6|7:
        print("Weekend")

