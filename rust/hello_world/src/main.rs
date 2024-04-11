/*
Rust uses multi-line comments with /* */
Rust uses single line comments with //

The fn keyword is used to define a function.

To run this program:
1) you must compile is first by typing: rustc hello_world.rs
2) run the compiled code with: ./hello_world

Alternatively, you can run: cargo run

On a macOS, there is no .exe file extension like on Windows.
MacOS relies on the Unix-like convention where executables don't have any specific extension.

The ./ prefix specifies are the file in the current directory.
The main() function is a predefined function that acts as an entry point to the program.

To check your versin of Rust, type: rustc -V
To check your version of Cargo, type: cargo -V
To update rust, type: rustup update

To create a new cargo package, type: cargo new project_name
You can compile and run with: cargo run

Rust packages tend to be more self-contained than pip with Python.

In Python, pip requires a requirements.txt file for the dependencies.
In Rust, cargo uses the Cargo.toml file for the dependencies. Cargo uses Lockfiles, while pip does not.

The root directory of your Rust project is: hello_world
The Cargo.toml file is the heart of your project configuration.
The src/ directory contains your rust source code.
The main.rs file is the entry point of your executable.

The Cargo.lock file records the exact version of dependencies used in your project.
The target folder servers as the output location for compiled artifacts (binaries and libraries) produced by cargo.
Always ignore the target folder when working with a version control like Git.

Rust is a statically typed language.

Rust is a compiled language, while Python is an interpeted language.

Clippy is a widely used linter in Rust and usually already comes installed.
To use it, navigate to the related directory and then type: cargo clippy

To run a check on your Rust program using Rust's built in linter, type: cargo check

The datatype: %str is a string literal.
Used when the value of a string is known at compile time.

*/

fn main() {

    let example = "like this";
    println!("\nbetter way to format strings: {example}");

    let text1 = "apple";
    let text2:&str = "orange";
    println!("format twice with: {} and {}", text1, text2);

    println!("hello from the main function.");

    message();
    computations1();

    let int1 = 5;
    let int2 = 10;
    let int3 = sum(int1, int2);
    println!("The value of int3 is: {int3}");

    // Example: Creating an empty string object using the new() method.
    // Then setting its value to hello.
    let mut text3 = String::new();
    text3.push_str("example of setting the value of a string object");
    println!("{text3}"
)
}
fn message() {

    println!("This is a sentence from the message function.");
}

fn computations1() {

    let age = 255;

    let weight = 256;
    let height = 257;
    let mut score = 258;

    score += 5;

    println!("age is {age} ");
    println!("weight is {weight}");
    println!("height is {height}");
    println!("score is {score}");

    let int_with_separator = 50_000;
    println!("int value {int_with_separator}");

    let alphabet:char = 'A';
    println!("alphabet is {}",alphabet);
}

fn sum(int1:i32, int2:i32) -> i32 {

    let sum = int1 + int2;

    println!("The sum of {int1} and {int2} is: {sum}");

    // The convention for returning values in a function in Rust,
    // is to simply give the expression with no keyword return or semicolon.
    // The last expression is implicitly returned.
    sum

}