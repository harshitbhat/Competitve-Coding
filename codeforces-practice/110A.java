import java.util.Scanner;

class OneHundredTenA {

    public static void solve(String str) {
        char num[] = str.toCharArray();

        int ct = 0;
        for(char x: num) {
            if(x == '4' || x == '7') {
                ct++;
            }
        }

        if(ct == 4 || ct == 7) {
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
