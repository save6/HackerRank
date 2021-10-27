# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

checks = {
    "num":lambda credit: re.match(r"[456][0-9]{15}$",credit) or re.match(r"[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$",credit),
    "repeat":lambda credit:not re.search(r"([\d])\1\1\1",credit.replace("-", ""))
}

def main():
    for _ in range(int(input())):
        credit = input()
        print("Valid" if all(checks[check](credit) for check in checks.keys()) else "Invalid")

if __name__=="__main__":
    main()
