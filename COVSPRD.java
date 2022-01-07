import java.util.Scanner;
import java.lang.Math;

class COVSPRD {

    public static void solve(int n, int d) {
        if( d > 21) {
            System.out.println(n);
            return;
        }

        double ans;

        if(d > 10) {
            ans = Math.pow(2,10) * Math.pow(3, d - 10);
        } else {
            ans = Math.pow(2, d);
        }

        if(ans > n){
            System.out.println(n);
        } else {
            System.out.println((int) ans);
        }
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while(T > 0) {
            T--;
            int n = sc.nextInt();
            int d = sc.nextInt();
            solve(n, d);
        }

        sc.close();
    }
    
}
