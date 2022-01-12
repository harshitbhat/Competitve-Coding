import java.util.Scanner;

class OneHundredTHirtySixA {

    public static void solve(int []arr, int n) {
        int temp[] = new int[n];

        for(int i = 0; i < n; i++) {
            temp[arr[i] - 1] = i + 1;
        }

        for(int i = 0; i < n; i++) {
            System.out.print(temp[i] + " ");
        }
        System.out.println();
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int arr[] = new int[n];

        for(int i = 0; i < n ; i++) {
            arr[i] = sc.nextInt();
        }

        solve(arr, n);

        sc.close();
    }
    
}
