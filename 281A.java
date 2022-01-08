import java.util.Scanner;

class TwoEightyOneA {

    public static void solve(String str) {

        String ans = String.valueOf(str.charAt(0)).toUpperCase();

        System.out.println(ans + str.substring(1));

    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        solve(str);

        sc.close();
    }
    
}
