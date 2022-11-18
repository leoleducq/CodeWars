fn feast(beast: &str, dish: &str) -> bool {
    beast.chars().next() == dish.chars().next() && beast.chars().last() == dish.chars().last()
}