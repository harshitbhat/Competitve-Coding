import java.util.Scanner;

class OneHundredSixteenA {

    public static void solve(Scanner sc, int n) {

        int present = 0;
        int ans = 0;

        for(int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            present += b - a;
            ans = Math.max(present, ans);
        }

        System.out.println(ans);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        solve(sc, n);

        sc.close();
    }
    
}
