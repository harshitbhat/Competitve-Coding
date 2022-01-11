import java.util.Scanner;
import java.lang.Math;

class OneA {
    public static void solve(long m, long n, long a) {

        long x = (long) Math.ceil((double) m / a);
        long y = (long) Math.ceil((double) n / a);

        if(x == 0) x = 1;
        if(y == 0) y = 1;

        System.out.println(x * y);
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        long m = sc.nextLong();
        long n = sc.nextLong();
        long a = sc.nextLong();

        solve(m, n, a);
        sc.close();
    }
}
