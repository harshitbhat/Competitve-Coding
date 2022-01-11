import java.util.Scanner;

class NinetySixA {

    public static void solve(String str) {

        int ct = 1;
        
        for(int i = 1; i < str.length(); i++) {
            if(str.charAt(i) == str.charAt(i-1)) {
                ct++;
            } else {
                ct = 1;
            }
            if(ct == 7) {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        solve(str);

        sc.close();
    }
    
}
