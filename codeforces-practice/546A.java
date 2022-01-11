import java.util.Scanner;

class FiveHundredFourtySixA {

    public static void solve(int k, int n, int w) {
        int needed = 0;

        for(int i = 1; i <= w; i++) {
            needed += i * k;
        }

        if(needed < n) {
            System.out.println(0);
        } else {
            System.out.println(needed - n);
        }
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int k = sc.nextInt();
        int n = sc.nextInt();
        int w = sc.nextInt();

        solve(k, n ,w);

        sc.close();
    }
    
}
