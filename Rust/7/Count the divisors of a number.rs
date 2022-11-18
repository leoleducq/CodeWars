fn divisors(n: u32) -> u32 {
    (1..=n).filter(|x| n % x == 0).count() as u32
}