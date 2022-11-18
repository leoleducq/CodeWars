fn rps(p1: &str, p2: &str) -> &'static str  {
    match (p1, p2) {
        ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock") => "Player 1 won!",
        ("rock", "paper") | ("scissors", "rock") | ("paper", "scissors") => "Player 2 won!",
        _ => "Draw!"
    }
}