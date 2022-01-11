import java.util.Scanner;

class FiftyEightA {

    public static void solve(String str) {
        char hello[] = {'h','e','l','l','o'};
        char strArr[] = str.toCharArray();

        int i,j;
        i = j = 0;

        while(j < strArr.length) {
            if(strArr[j] == hello[i]) {
                i++;
            }
            if( i == hello.length) {
                break;
            }
            j++;
        }
        if(i == hello.length) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        solve(str);

        sc.close();
    }
    
}
