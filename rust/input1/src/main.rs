// Importing the io library from the standard library.
use std::io;

fn main() {
    let mut user_input1 = String::new();
    println!("Enter your name:");

    io::stdin()
        .read_line(&mut user_input1)
        .expect("Failed to read line");

    println!("Good day {user_input1}");
}
