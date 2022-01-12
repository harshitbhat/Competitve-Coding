import java.util.HashMap;
import java.util.Scanner;

class TwoHundredSeventyOneA {

    public static boolean isDistinct(int n) {
        HashMap<Integer, Boolean> map = new HashMap<>();
        while( n > 0 ) {
            int last = n % 10;
            if(!map.containsKey(last)) {
                map.put(last, true);
            } else {
                return false;
            }
            n = n / 10;
        }
        return true;
    }

    public static void solve(int n) {
        for(int i = n+1; ;i++) {
            if(isDistinct(i)) {
                System.out.println(i);
                return;
            }
        }
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        solve(n);
        sc.close();
    }
    
}
