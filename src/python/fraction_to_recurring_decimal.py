class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        result = ""
        if (numerator < 0) ^ (denominator < 0):
            result += "-"
        numerator, denominator = abs(numerator), abs(denominator)
        result += str(numerator//denominator)
        if numerator % denominator == 0:
            return result
        result += "."

        remainder_dict = {}
        remainder = numerator % denominator
        while remainder != 0 and remainder not in remainder_dict:
            remainder_dict[remainder] = len(result)
            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator
        
        if remainder in remainder_dict:
            result = result[:remainder_dict[remainder]] + "(" + result[remainder_dict[remainder]:] + ")"
        
        return result
    
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator*denominator<0 else ''
        n, rem = divmod(abs(numerator), abs(denominator))
        
        res = [sign + str(n), '.']
            
        m = { }
        while rem not in m:
            m[rem] = len(res)
            n, rem = divmod(rem * 10, abs(denominator))
            res.append(str(n))

        res.insert(m[rem], '(')
        res.append(')')
        
        return ''.join(res).replace('(0)', '').strip('.')


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.fractionToDecimal(1, 2) == "0.5"
    assert s.fractionToDecimal(2, 1) == "2"
    assert s.fractionToDecimal(4, 333) == "0.(012)"
    print("Done!")

