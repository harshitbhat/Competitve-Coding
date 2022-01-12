import java.util.Arrays;
import java.util.Scanner;

class OneHundredSixtyA {

    public static void solve(int n, int arr[]) {
        Arrays.sort(arr);
        int sum = 0;
        for(int x: arr) {
            sum += x;
        }
        int ans = 0;
        int sol = 0;
        for(int i = n - 1; i >= 0; i--) {
            ans += arr[i];
            sum -= arr[i];
            sol++;
            if(ans > sum) {
               break;
            }
        }
        System.out.println(sol);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int arr[] = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        solve(n, arr);

        sc.close();
    }
    
}
