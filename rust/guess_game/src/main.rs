// Importing the io library from the standard library.
use std::io;

fn main() {
    let mut user_input1 = String::new();
    println!("Guess the number!");
    println!("Enter your guess:");

    // read_line puts what the user enters into a string.
    // It also returns a Result value. A Result is an enumeration and is often called an enum.
    io::stdin()
        .read_line(&mut user_input1)
        .expect("Failed to read line");

    println!("You guessed: {user_input1}");
}
