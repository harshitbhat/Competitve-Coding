import java.util.*;

class FourA {

    public static void solve(int num) {
        if(num % 2 != 0 || num == 2) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
    }

    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        sc.close();
        solve(num);
    }
}
