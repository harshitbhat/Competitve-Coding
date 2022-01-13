import java.util.Scanner;

class FourHundredSixtyEightA {

    public static void solve(long n) {
        long ans = n % 2 == 0 ? n / 2 : (-1 * ((n / 2) + 1));
        System.out.println(ans);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        long n = sc.nextLong();

        solve(n);

        sc.close();
    }
    
}

/*

f(n) =  - 1 + 2 - 3 + .. + ( - 1)^n

n (even) -> n/2 even, n/2 odd
n  (odd) -> n/2 even, (n+1)/2 odd

*/