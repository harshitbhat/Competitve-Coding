import java.util.Scanner;

class ThreeHundredFourtyFourA {

    public static void solve(String []magnets, int n) {
        int groups = 1;
        char prevPole = magnets[0].charAt(1);

        for(int i = 1; i < n; i++) {
            char currentPole = magnets[i].charAt(0);
            if(currentPole == prevPole) {
                groups++;
                prevPole = magnets[i].charAt(1);
            }
        }
        System.out.println(groups);
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String magnets[] = new String[n];
        for(int i = 0; i < n; i++) {
            magnets[i] = sc.next();
        }
        solve(magnets, n);
        sc.close();
    }
    
}
