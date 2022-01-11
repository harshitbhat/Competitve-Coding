import java.util.Scanner;

class OneHundredTwentyTwoA {

    public static void solve(int n) {
        int lucky[] = {4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777 };
        for(int i = 0; i < lucky.length; i++) {
            if(n % lucky[i] == 0) {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        solve(n);
        sc.close();
    }
    
}
