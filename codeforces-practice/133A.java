import java.util.Scanner;

class OneHundredThirtyThreeA {

    public static void solve(String str) {
        if(str.contains("H") || str.contains("Q") || str.contains("9")) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        solve(str);

        sc.close();
    }
    
}
