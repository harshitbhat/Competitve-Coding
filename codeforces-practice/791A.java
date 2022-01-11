import java.util.Scanner;

class SevenHundredNinetyOneA {

    public static void solve(int a, int b) {
        int n = 1;

        while( ( a * Math.pow(3, n)) <= ( b * Math.pow(2, n)) ) {
            n++;
        }
        System.out.println(n);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        solve(a,b);

        sc.close();
    }
    
}
