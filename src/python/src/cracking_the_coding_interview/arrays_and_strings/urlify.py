#  Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith " J 13 Output: "Mr%20J ohn%20Smith" Hints: #53, #7 78
def urlify(s: str, size: int) -> str:
    return s[:size].replace(" ", "%20")


def urlify_alternative(s: str, size: int) -> str:
    return "%20".join(s[:size].split(" "))


if __name__ == "__main__":
    print("Testing...")
    assert urlify("Mr John Smith ", 13) == "Mr%20John%20Smith"
    print("Done!")
