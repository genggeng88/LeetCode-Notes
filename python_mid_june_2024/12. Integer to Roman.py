class Solution:
    def intToRoman(self, num: int) -> str:
        thous = ['', 'M', 'MM', 'MMM']
        hunds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

        return (thous[num//1000] + hunds[num%1000//100]
                + tens[num%100//10] + ones[num%10])