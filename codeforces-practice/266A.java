import java.util.Scanner;

class TwoSixtySixA {

    public static void solve(String s, int n) {
        int ans = 0;
        char prev = s.charAt(0);

        for(int i = 1; i < s.length(); i++) {
            if(s.charAt(i) == prev) {
                ans++;
            } else {
                prev = s.charAt(i);
            }
        }
        System.out.println(ans);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String str = sc.next();

        solve(str,n);

        sc.close();
    }
    
}
