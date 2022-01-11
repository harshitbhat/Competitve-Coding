import java.util.Scanner;

class TwoHundredSixtySixB {

    public static void solve(String str, int n, int t) {

        char []strArr = str.toCharArray();
        
        while(t-- > 0) {
            int i = 0;
            while( i < n - 1) {
                char ch1 = strArr[i];
                char ch2 = strArr[i+1];

                if(ch1 == 'B' && ch2 == 'G') {
                    strArr[i] = 'G';
                    strArr[i+1] = 'B';
                    i += 2;
                } else {
                    i++;
                }
            }
        }
        System.out.println(String.valueOf(strArr));
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int t = sc.nextInt();

        String str = sc.next();

        solve(str, n, t);

        sc.close();
    }
    
}
