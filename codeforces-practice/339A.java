import java.util.Scanner;
import java.util.Arrays;
import java.util.regex.Pattern;

class ThreeHundredThirtyNineA {

    public static void solve(String s) {

        if(s.contains("+")) {
            String parts[] = s.split(Pattern.quote("+"));
            Arrays.sort(parts);
            String ans = "";
            for(int i = 0; i < parts.length - 1; i++) {
                ans += parts[i] + "+";
            }
            ans += parts[parts.length - 1];
            System.out.println(ans);
        } else {
            System.out.println(s);
        }
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        solve(str);

        sc.close();
    }
    
}
