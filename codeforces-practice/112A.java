import java.util.Scanner;

class OneHundredTwelveA {

    public static int solve(String a, String b) {

        a = a.toLowerCase();
        b = b.toLowerCase();

        for(int i = 0; i < a.length(); i++) {
            char ch1 = a.charAt(i);
            char ch2 = b.charAt(i);
            if(ch1 < ch2) {
                return -1;
            } else if (ch1 > ch2) {
                return 1;
            }
        }
        
        return 0;
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String one = sc.next();
        String two = sc.next();

        int ans = solve(one,two);

        System.out.println(ans);

        sc.close();
    }
    
}
