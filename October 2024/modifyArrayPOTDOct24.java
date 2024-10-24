import java.util.ArrayList;
import java.util.Scanner;

class modifyArrayPOTDOct24 {

    static ArrayList<Integer> modifyAndRearrangeArr(int arr[]) {
        ArrayList<Integer> list = new ArrayList<>();
        int zeroCount = 0;

        for (int i = 0; i < arr.length; i++) {
            if (i < arr.length - 1 && arr[i] == arr[i + 1] && arr[i] != 0) {
                arr[i] = 2 * arr[i];  
                arr[i + 1] = 0;       
            }
            
            if (arr[i] != 0) {
                list.add(arr[i]);  
            } else {
                zeroCount++;       
            }
        }

        while (zeroCount != 0) {
            list.add(0);
            zeroCount--;
        }

        return list;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the size of the array:");
        int size = sc.nextInt();

        int arr[] = new int[size];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < size; i++) {
            arr[i] = sc.nextInt();
        }

        ArrayList<Integer> result = modifyAndRearrangeArr(arr);

        System.out.println("Modified and rearranged array:");
        System.out.println(result);

        sc.close();
    }
}
