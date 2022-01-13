import java.util.Scanner;

class ThreeHundredEighteenA {

    public static void solve(long n, long k) {
        long half = n / 2;
        long ans;

        if(n % 2 == 0) {
            if( k <= half ) {
                ans = 2 * k - 1;
            } else {
                k = k - half;
                ans = 2 * k;
            }
        } else {
            if( k <= half + 1 ) {
                ans = 2 * k - 1;
            } else {
                k = k - half - 1;
                ans = 2 * k;
            }
        }

        System.out.println(ans);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        long n = sc.nextLong();
        long k = sc.nextLong();

        solve(n,k);

        sc.close();
    }
    
}

/*

9
1 3 5 7 9 2 4 6 8

*/