import java.util.Scanner;

class OneThousandThirtyA {

    public static void solve(int[] arr) {
        String is = "EASY";

        for(int x: arr) {
            if(x == 1) {
                is = "HARD";
                break;
            }
        }
        System.out.println(is);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        solve(arr);

        sc.close();
    }
    
}
