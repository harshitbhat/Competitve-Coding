import java.util.Scanner;

class PINBS {

    public static void solve(String str) {

        String common[] = { 
            "11", 
            "101", 
            "10001", 
            "10000000", 
            "100000000000000000000000000000001"
        };

        for(int i = 0; i < common.length; i++) {
            if(str.contains(common[i])) {
                System.out.println("Yes");
                return;
            }
        }
        System.out.println("No");
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while(T > 0) {
            T--;
            String s = sc.next();
            solve(s);
        }

        sc.close();
    }
    
}

// Wrong idea. Think again.
