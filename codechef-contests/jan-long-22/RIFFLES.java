import java.util.Arrays;
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

    public static int[] solve(int n, int k) {

        int arr1[] = new int[n];
        int arr2[] = new int[n];

        for(int i = 1; i <= n; i++) {
            arr1[i-1] = i;
            arr2[i-1] = i;
        }

        int count = 0;

        do {
            count++;
            riffle(arr2);
            if(count == k) {
                return arr2;
            }
        } while(!Arrays.equals(arr1, arr2));

        k = k % count;

        while( k > 0 ) {
            k--;
            riffle(arr1);
        }
        return arr1;
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while(T > 0) {
            T--;
            int n = sc.nextInt();
            int k = sc.nextInt();
            int []ans = solve(n,k);
            for(int i = 0; i < ans.length; i++) {
                System.out.print(ans[i] + " ");
            }
            System.out.println();
        }

        sc.close();
    }
    
}
