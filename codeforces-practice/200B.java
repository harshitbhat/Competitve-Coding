import java.util.Scanner;

class TwoHundredB {

    public static void solve(int n, int []arr) {
        int sum = 0;
        for(int x : arr) {
            sum += x;
        }
        double ans = sum / (n * 100.0);
        System.out.println(String.format("%.12f", ans * 100));
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int []arr = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        solve(n, arr);

        sc.close();
    }
    
}
