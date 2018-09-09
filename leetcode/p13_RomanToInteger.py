# NOT SUBMITTED

# Special Rules
#   4   IV
#   9   IX
#   40  XL
#   90  XC
#   400 CD
#   900 CM

# Examples
#   III     1+1+1           3
#   IV      5-1             4
#   IX      10-1            9
#   LVIII   50+5+3          58
#   MCMXCIV 1000+900+90+4   1994

class Solution:
    value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    special = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        accum = 0

        while i < len(s):
            if i < len(s) - 1:
                # Has more than two characters left over -> can check for special cases
                toCheck = s[i:i+2]

                # Check if the two chars are special
                if toCheck in self.special:
                    accum += self.special[toCheck]

                    # Increment i again to account for second char
                    i += 1
                else:
                    accum += self.value[s[i]]
            else:
                accum += self.value[s[i]]

            i += 1
        
        return accum

