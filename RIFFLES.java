import java.util.Scanner;

class RIFFLES {

    public static void riffle(int []arr) {
        int n = arr.length;

        int arr1[] = new int [n/2];
        int arr2[] = new int [n/2];

        int j = 0;

        for(int i = 0; i < n; i += 2) {
            arr1[j++] = arr[i];
        }
        j = 0;
        for(int i = 1; i < n; i += 2) {
            arr2[j++] = arr[i];
        }

        j = 0;
        for(int i = 0; i < n / 2; i++) {
            arr[j++] = arr1[i];
        }
        for(int i = 0; i < n / 2; i++) {
            arr[j++] = arr2[i];
        }
        
    }

    public static void solve(int n, int k) {

        int arr[] = new int[n];

        for(int i = 1; i <= n; i++) {
            arr[i-1] = i;
        }

        while( k > 0) {
            k--;
            riffle(arr);
        }

        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while(T > 0) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            solve(n,k);
        }

        sc.close();
    }
    
}
