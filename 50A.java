import java.util.Scanner;

class FiftyA {

    public static void solve(int l, int b) {
        System.out.println( (l * b) / 2);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int l = sc.nextInt();
        int b = sc.nextInt();

        solve(l, b);

        sc.close();
    }
    
}
