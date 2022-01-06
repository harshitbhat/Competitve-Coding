import java.util.*;

class SeventyOneA {

    public static void solve(String s) {
        if(s.length() <= 10) {
            System.out.println(s);
        } else {
            System.out.println(String.valueOf(s.charAt(0)) + (s.length() - 2) + String.valueOf(s.charAt(s.length() - 1)) );
        }
    }

    public static void main(String [] args) {

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while(T > 0) {
            String str = sc.next();
            solve(str);
            T--;
        }
        sc.close();
    }
    
}
