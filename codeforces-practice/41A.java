import java.util.Scanner;

class FortyOneA {

    public static void solve(String a, String b) {

        if(a.length() != b.length()) {
            System.out.println("NO");
            return;
        }

        int i = 0;
        int j = a.length() - 1;
        while( i < a.length() && j >= 0) {
            if(a.charAt(i) != b.charAt(j)) {
                System.out.println("NO");
                return;
            }
            i++;
            j--;
        }
        System.out.println("YES");
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String a,b;

        a = sc.next();
        b = sc.next();

        solve(a,b);

        sc.close();
    }
    
}
