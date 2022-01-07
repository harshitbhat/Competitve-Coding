import java.util.Scanner;
import java.lang.Math;

class TwoSixtyThreeA {

    public static void solve(int [][]matrix) {
        int x,y;

        x = y = 0;

        for(int i = 0; i < 5; i++) {
            for(int j = 0; j < 5; j++) {
                if(matrix[i][j] == 1) {
                    x = i;
                    y = j;
                }
            }
        }

        System.out.println(Math.abs(x - 2) + Math.abs(y - 2));
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int matrix[][] = new int[5][5];

        for(int i = 0; i < 5; i++) {
            for(int j = 0; j < 5; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        solve(matrix);

        sc.close();
    }
    
}
