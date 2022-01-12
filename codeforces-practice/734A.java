import java.util.Scanner;

class SevenHundredThirtyFourA {

    public static void solve(String s, int n) {
        int a = 0;
        int d = 0;

        for(int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if(ch == 'A') {
                a++;
            } else {
                d++;
            }
        }
        if(a == d) {
            System.out.println("Friendship");
        } else if ( a > d ) {
            System.out.println("Anton");
        } else {
            System.out.println("Danik");
        }
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        solve(s,n);
        sc.close();
    }
    
}
