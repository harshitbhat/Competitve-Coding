import java.util.Scanner;

class SixtyNineA {

    public static void solve(int [][]coordinates, int n) {
        int x = 0;
        int y = 0;
        int z = 0;

        for(int i = 0; i < n; i++) {
            x += coordinates[i][0];
        }
        for(int i = 0; i < n; i++) {
            y += coordinates[i][1];
        }
        for(int i = 0; i < n; i++) {
            z += coordinates[i][2];
        }

        if( x == 0 && y == 0 && z == 0) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int [][]coordinates = new int[n][3];

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < 3; j++) {
                coordinates[i][j] = sc.nextInt();
            }
        }

        solve(coordinates, n);

        sc.close();
    }
    
}
