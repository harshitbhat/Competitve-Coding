import java.util.*;

class TwoThirtyOneA {

    public static boolean solve(int arr[]) {
        int can = 0;
        for(int i = 0; i < 3; i++) {
            if(arr[i] == 1) {
                can++;
            } 
        }
        return can >= 2 ? true : false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        int arr[] = new int[3];

        int ans = 0;

        while(T > 0) {
            T--;
            for(int i = 0; i < 3; i++) {
                arr[i] = sc.nextInt();
            }

            boolean isPossible = solve(arr);
            if(isPossible) {
                ans++;
            }
        }

        System.out.println(ans);

        sc.close();
    }
    
}
