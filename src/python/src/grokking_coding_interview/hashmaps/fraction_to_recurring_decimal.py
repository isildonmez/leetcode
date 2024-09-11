def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return "0"
    if denominator == 1:
        return str(numerator)
    res = ""
    if (numerator < 0) ^ (denominator < 0):
        res += "-"
    numerator = abs(numerator)
    denominator = abs(denominator)
    whole_number, remainder = divmod(numerator, denominator)
    res += str(whole_number)
    if remainder == 0:
        return res
    res += "."
    remainders = {remainder: 0}
    decimal = ""
    while remainder > 0:
        remainder *= 10
        quotient, remainder = divmod(remainder, denominator)
        decimal += str(quotient)
        if remainder in remainders:
            i = remainders[remainder]
            return f"{res}{decimal[:i]}({decimal[i:]})"
        else:
            remainders[remainder] = len(decimal)
    res += f"{decimal}"
    return res
