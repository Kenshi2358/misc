/*
General Notes:

Call the thread_rng() function and use the gen_range method().
gen_range is inclusive on the lower and upper bounds.

read_line puts what the user enters into a string.
read_line returns a Result value. A Result is an enumeration and is often called an enum.
An enum can be one of multiple possible states and each possible state is called a variant.

Result's variants are Ok and Err. The Ok variant indicates that the operation was successful.
The Err variant means that the operation failed.
We want to crash the program when a problem occurs, so we are using the expect method.

The parse method returns a Result type and Result is an enum with variants: Ok and Err.

Convert user_guess1 string to an unsigned 32-bit integer.
Trim any whitespace with the trim() method. Parse any carriage returns iwth the parse() method.

The cmp method compares 2 values and can be called on anything that can be compared.
Ordering is another enum and has variants: Less, Greater, and Equal.

*/

// Importing the io and cmp libraries from the standard library.
use std::io;
use std::cmp::Ordering;
// Importing the rand library.
use rand::Rng;


fn main() {

    let start_num = 1;
    let end_num = 20;

    println!("Guess the number! -- Guess a number between {start_num} and {end_num} --");

    let secret_number = rand::thread_rng().gen_range(start_num..=end_num);
    // println!("The secret number is: {secret_number}");

    let mut num_guesses = 1;
    loop {

        println!("Enter your guess:");
        let mut user_guess1 = String::new();

        io::stdin()
            .read_line(&mut user_guess1)
            .expect("Failed to read line");

        let user_guess1: u32 = match user_guess1.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {user_guess1}");

        match user_guess1.cmp(&secret_number) {
            Ordering::Less => println!("Too small! # guesses: {num_guesses}"),
            Ordering::Greater => println!("Too big! # guesses: {num_guesses}"),
            Ordering::Equal => {
                println!("You win! # guesses: {num_guesses}");
                break;
            }
        }

        num_guesses += 1;
    }
}
