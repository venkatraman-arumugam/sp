import java.util.Scanner;

class SAMER{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int[] squares = new int[101];
        int tmp = 0;
        for(int i=0;i<101;i++){
            tmp += i*i;
            squares[i] = tmp;
        }
        while(true){
            int n = s.nextInt();
            if(n == 0){
                break;
            }
            System.out.println(squares[n]);
        }
    }
}