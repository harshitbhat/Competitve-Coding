import java.util.Scanner;
import java.lang.Math;

class KEPLERSLAW {

    public static void solve(int t1,int t2, int r1, int r2) {
        double ratio1 = Math.pow(t1,2) / Math.pow(r1, 3);
        double ratio2 = Math.pow(t2,2) / Math.pow(r2, 3);

        if(ratio1 == ratio2) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while(T > 0) {
            T--;
            int t1 = sc.nextInt();
            int t2 = sc.nextInt();
            int r1 = sc.nextInt();
            int r2 = sc.nextInt();
            solve(t1,t2,r1,r2);
        }

        sc.close();
    }
    
}
