def minFlips(a, b, c):
    ans = 0

    for i in range(32):
        bitA = (a >> i) & 1
        bitB = (b >> i) & 1
        bitC = (c >> i) & 1

        if (bitA | bitB) != bitC:
            if bitC == 0:
                if bitA == 1 and bitB == 1:
                    ans += 2
                else:
                    ans += 1
            else:
                ans += 1

    return ans

a = 2;
b = 6;
c = 5

print(f'Min Flips required to make two numbers equal to third is : {minFlips (a, b, c)}'); 