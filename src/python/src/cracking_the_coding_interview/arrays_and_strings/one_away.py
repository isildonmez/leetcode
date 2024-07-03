# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.


def one_away(left: str, right: str) -> bool:
    if left == right:
        return True
    if abs(len(left) - len(right)) > 1:
        return False
    editted = False
    if len(left) == len(right):
        for i in range(len(left)):
            if left[i] != right[i]:
                if editted == True:
                    return False
                editted = True
        return True
    shorter, larger = (right, left) if len(right) < len(left) else (left, right)
    i = 0
    for j in range(len(shorter)):
        if shorter[i] != larger[j]:
            if editted == True:
                return False
            editted = True
        else:
            i += 1
    return True


if __name__ == "__main__":
    print("Testing...")
    assert one_away("pale", "ple") == True
    assert one_away("ple", "pale") == True
    assert one_away("pales", "pale") == True
    assert one_away("pale", "pales") == True
    assert one_away("pale", "bale") == True
    assert one_away("bale", "pale") == True
    assert one_away("pale", "bake") == False
    assert one_away("bake", "pale") == False
    print("Done!")
