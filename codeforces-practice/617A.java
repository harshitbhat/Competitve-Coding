import java.util.Scanner;

class SixHundredSeventeenA {

    public static void solve(int n) {
        int ans = 0;
        
        for(int i = 5; i > 0; i--) {
            int steps = n / i;
            n -= steps * i;
            ans += steps;
        }

        System.out.println(ans);

    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();

        solve(x);

        sc.close();
    }
    
}
