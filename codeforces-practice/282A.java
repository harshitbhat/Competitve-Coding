import java.util.Scanner;

class TwoEightyTwoA {

    public static void solve(Scanner sc) {

        int T = sc.nextInt();
        int x = 0;

        while(T > 0) {
            T--;
            String op = sc.next();
            if(op.contains("+")) {
                x++;
            } else {
                x--;
            }
        }

        System.out.println(x);
        
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        solve(sc);
        sc.close();
    }
    
}
