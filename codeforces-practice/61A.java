import java.util.Scanner;

class SixtyOneA {

    public static void solve(String a, String b) {
        String ans = "";
        for(int i = a.length() - 1; i >= 0; i--) {
            int x = a.charAt(i) - '0';
            int y = b.charAt(i) - '0';
            ans = Integer.toString(x ^ y) + ans;
        }
        System.out.println(ans);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();

        solve(a, b);

        sc.close();
    }
    
}
