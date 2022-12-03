import re
import days
from days import *


def main():
    solved_days = [int(re.split("(\d+)", st)[1]) for st in days.__all__]
    solved_days.sort()
    try:
        while True:
            try:
                ch = int(input(f"\nDays available: {solved_days}\nWhich day to show? (0=quit): "))
                if ch > 25 or ch < 0:
                    print("\nNumber must be between 0 and 25")
                    continue
                if ch == 0:
                    break
                print()
                exec(f"day{ch}.main()")
            except ValueError:
                print("\nEnter a number")
                continue
    except KeyboardInterrupt:
        print()
    print("\nQuitting")


if __name__ == "__main__":
    main()

