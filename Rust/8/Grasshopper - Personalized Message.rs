fn greet(name: &str, owner: &str) -> String {
    if name == owner {
        "Hello boss".to_string()
    } else {
        "Hello guest".to_string()
    }
}