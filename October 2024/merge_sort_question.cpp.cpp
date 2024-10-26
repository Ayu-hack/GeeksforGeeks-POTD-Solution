#include <iostream>
using namespace std;

void merge(int arr[], int l, int mid, int r)
{
    int an = mid - l + 1;
    int bn = r - mid;
    int a[an];
    int b[bn];
    for (int i = 0; i < an; i++)
    {
        a[i] = arr[l + i];
    }
    for (int i = 0; i < bn; i++)
    {
        b[i] = arr[mid + 1 + i];
    }
    int i = 0; // for 1st half of array
    int j = 0; // for 2nd part of the array
    int k = l; // for final array
    while (i < an && j < bn)
    {
        if (a[i] < b[j])
        {
            arr[k++] = a[i++];
        }
        else
        {
            arr[k++] = b[j++];
        }
    }
    while (i < an)
    {
        arr[k++] = a[i++];
    }
    while (j < bn)
    {
        arr[k++] = b[j++];
    }
}

void mergeSort(int arr[], int l, int r)
{
    int mid = l + (r - l) / 2;

    // base case
    if (l >= r)
        return;
    mergeSort(arr, l, mid);
    mergeSort(arr, mid + 1, r);
    merge(arr, l, mid, r);
}

int main()
{
    int arr[] = {7, 4, 6, 8, 2, 1, 3, 5, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << ' ';
    }
    return 0;
}