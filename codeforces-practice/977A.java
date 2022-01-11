import java.util.Scanner;

class NineHundredSeventySevenA {

    public static void solve(int n, int k) {
        while(k-- > 0) {
            if( n % 10 == 0) {
                n /= 10;
            } else {
                n--;
            }
        }
        System.out.println(n);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        solve(n, k);

        sc.close();
    }
    
}
