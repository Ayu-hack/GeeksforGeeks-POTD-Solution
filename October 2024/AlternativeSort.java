import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class AlternativeSort {
    private int[] arr; // Array to hold user input

    // Constructor to initialize the array
    public AlternativeSort(int[] arr) {
        this.arr = arr;
    }

    // Method to perform alternate sorting
    public ArrayList<Integer> alternateSort() {
        Arrays.sort(arr);
        int n = arr.length;
        ArrayList<Integer> list = new ArrayList<>(n);
        int left = 0;
        int right = n - 1;

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                list.add(arr[right--]);
            } else {
                list.add(arr[left++]);
            }
        }
        return list;
    }

    // Main method to interact with the user
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // User input for array size
        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        int[] arr = new int[n];

        // User input for array elements
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        // Initialize Solution instance and call alternateSort
        AlternativeSort solution = new AlternativeSort(arr);
        ArrayList<Integer> sortedList = solution.alternateSort();

        // Display result
        System.out.println("Array after alternate sorting: " + sortedList);
        scanner.close();
    }
}
