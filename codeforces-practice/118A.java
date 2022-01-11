import java.util.Scanner;

class OneHundredEighteenA {

    public static boolean isVowel(char ch) {
        if(ch == 'a' || ch == 'o' || ch == 'y' || ch == 'e' || ch == 'u' || ch == 'i') {
            return true;
        }
        return false;
    }

    public static void solve(String str) {

        str = str.toLowerCase();
        String ans = "";

        for(int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if(!isVowel(ch)) {
                ans += "." + ch;
            }
        }
        
        System.out.println(ans);

    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        solve(str);

        sc.close();
    }
    
}
