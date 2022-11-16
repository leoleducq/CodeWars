fn find_smallest_int(arr: &[i32]) -> i32 {
    let mut smallest = arr[0];
    for i in arr {
        if *i < smallest {
            smallest = *i;
        }
    }
    smallest
}