import java.util.Scanner;

class FiftyNineA {

    public static void solve(String str) {
        int l = 0;
        int u = 0;

        for(int i = 0; i < str.length(); i++) {
            if(Character.isUpperCase(str.charAt(i))) {
                u++;
            } else {
                l++;
            }
        }

        if( u <= l) {
            System.out.println(str.toLowerCase());
        } else {
            System.out.println(str.toUpperCase());
        }

    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        solve(str);

        sc.close();
    }
    
}
