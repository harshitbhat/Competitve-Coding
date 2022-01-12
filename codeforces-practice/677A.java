import java.util.Scanner;

class SixHundredSeventySevenA {

    public static void solve(Scanner sc, int n, int h) {
        int ans = 0;
        for(int i = 0; i < n; i++) {
            int x = sc.nextInt();
            if(x > h) {
                ans += 2;
            } else {
                ans++;
            }
        }
        System.out.println(ans);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int h = sc.nextInt();

        solve(sc, n, h);

        sc.close();
    }
    
}
