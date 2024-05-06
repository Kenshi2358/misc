use std::io;

fn main() {
    let mut user_input1 = String::new();
    println!("Enter your name:");

    let b1 = io::stdin().read_line(&mut user_input1).unwrap();
    user_input1 += " Smith";

    println!("Good day {user_input1}");
    println!("# of bytes: {}", b1);
}
