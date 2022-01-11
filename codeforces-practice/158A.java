import java.util.Scanner;

class OneHundredFiftyEightA {

    public static void solve(int arr[], int n, int k) {
        int score = arr[k-1];
        int ans = 0;

        for(int i = 0; i < n; i++) {
            if(arr[i] > 0 && arr[i] >= score) {
                ans++;
            }
        }

        System.out.println(ans);
    }

    public static void main(String []args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int arr[] = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        solve(arr,n,k);

        sc.close();
        
    }

}