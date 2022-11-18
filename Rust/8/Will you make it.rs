fn zero_fuel(distance_to_pump: u32, mpg: u32, gallons: u32) -> bool {
    mpg * gallons >= distance_to_pump
}