import java.util.HashMap;
import java.util.Scanner;

class TwoHundredThirtySixA {

    public static void solve(String str) {
        HashMap<Character, Boolean> hmap = new HashMap<>();

        for(int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if(!hmap.containsKey(ch)) {
                hmap.put(ch, true);
            }
        }

        if(hmap.size() % 2 == 0) {
            System.out.println("CHAT WITH HER!");
        } else {
            System.out.println("IGNORE HIM!");
        }
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        solve(str);

        sc.close();
    }
    
}
