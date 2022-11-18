fn expressions_matter(a: u64, b: u64, c: u64) -> u64 {
    let mut max = 0;
    let mut temp = 0;
    temp = a + b + c;
    if temp > max {
        max = temp;
    }
    temp = a * b * c;
    if temp > max {
        max = temp;
    }
    temp = a * (b + c);
    if temp > max {
        max = temp;
    }
    temp = (a + b) * c;
    if temp > max {
        max = temp;
    }
    temp = a + b * c;
    if temp > max {
        max = temp;
    }
    temp = a * b + c;
    if temp > max {
        max = temp;
    }
    max
}