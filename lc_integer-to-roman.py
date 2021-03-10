class Solution:
    def intToRoman(self, num: int) -> str:
        myHash = {
            0 : '',
            1 : 'I',
            2 : 'II',
            3 : 'III',
            4 : 'IV',
            5 : 'V',
            6 : 'VI',
            7 : 'VII',
            8 : 'VIII',
            9 : 'IX',
            10 : 'X',
            20 : 'XX',
            30 : 'XXX',
            40 : 'XL',
            50 : 'L',
            60 : 'LX',
            70 : 'LXX',
            80 : 'LXXX',
            90 : 'XC',
            100 : 'C',
            200 : 'CC',
            300 : 'CCC',
            400 : 'CD',
            500 : 'D',
            600 : 'DC',
            700 : 'DCC',
            800 : 'DCCC',
            900 : 'CM',
            1000 : 'M',
            2000 : 'MM',
            3000 : 'MMM',
        }
        
        th = num // 1000
        th = th * 1000
        num = num % 1000
        h = num // 100
        h = h * 100
        num = num % 100 
        t = num // 10
        t = t * 10
        o = num % 10
        
        ans = f"{myHash[th]}{myHash[h]}{myHash[t]}{myHash[o]}"
        return ans