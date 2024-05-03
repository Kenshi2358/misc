/*
Rust Notes:

Rust is a statically typed language.
Rust is a compiled language, while Python is an interpeted language.

Clippy is a widely used linter in Rust and usually already comes installed.
To use it, navigate to the related directory and then type: cargo clippy

To run a check on your Rust program using Rust's built in linter, type: cargo check

Rust uses multi-line comments with /* */
Rust uses single line comments with //

The fn keyword defines a function.

There are 2 ways to run a rust program:
1) Compile the code by typing: rustc main.rs
Run the compiled code with: ./main

2) run: cargo run

On a macOS, there is no .exe file extension like on Windows.
MacOS relies on the Unix-like convention where executables don't have any specific extension.

The ./ prefix specifies that the file is in the current directory.
The main() function is a predefined function that acts as an entry point to the program.

To check your versin of Rust, type: rustc -V
To check your version of Cargo, type: cargo -V
To update rust, type: rustup update

To create a new cargo package, type: cargo new project_name
Then compile and run with: cargo run

Rust packages tend to be more self-contained than pip with Python.

In Python, pip requires a requirements.txt file for the dependencies.
In Rust, cargo uses the Cargo.toml file for the dependencies. Cargo uses Lockfiles, while pip does not.

The toml file for each package is called it's manifest.

The root directory of your Rust project is your project name. In this case, its: hello_world
The Cargo.toml file is the heart of your project configuration.
The src/ directory contains your rust source code.
The main.rs file is the entry point of your executable.

The Cargo.lock file records the exact version of dependencies used in your project.
The target folder is the output location for compiled artifacts (binaries and libraries) produced by cargo.
Always ignore the target folder when working with a version control like Git.

The datatype: %str is a string literal.
Used when the value of a string is known at compile time.

The ! in println! denotes that this function is a macro.
It helps Rust distinguish between macros and regular functions.

To debug a rust program in VSCode on a macOS, you need to install the extension: CodeLLDB
Then in the launch.json file, specify:
"type": "lldb",
"request": "launch",
"program": "${workspaceFolder}/rust/hello_world/target/debug/hello_world",

*/

fn main() {

    println!("hello from the main function.");
    message();

    formatting_examples();
    computations1();
    empty_string_example();
}

fn formatting_examples() {

    let text1 = "apple";
    let text2:&str = "orange";
    println!("\nFormatting with brackets and comma: {} and {}", text1, text2);

    let example = "like this";
    println!("Better formatting - formatting with brackets only: {example}\n");
}

fn message() {

    println!("hello from the message function.");
}

fn computations1() {

    let age = 255;

    let weight = 256;
    let height = 257;
    let mut score = 258;

    score += 5;

    println!("age is {age}  weight is {weight}  height is {height}  score is {score}");

    let int_with_separator = 50_000;
    println!("int value is: {int_with_separator}");

    let alphabet:char = 'A';
    println!("alphabet is: {alphabet}");

    let int1 = 5;
    let int2 = 10;
    let int3 = sum(int1, int2);
    println!("The value of int3 is: {int3}");
}

fn sum(int1:i32, int2:i32) -> i32 {

    let sum = int1 + int2;

    println!("The sum of {int1} and {int2} is: {sum}");

    let threshold_num = 20;

    if sum > threshold_num {
        println!("The sum is greater than {threshold_num}.");
    } else {
        println!("The sum is less than or equal to {threshold_num}.");
    }

    // The convention for returning values in a function,
    // is to give the expression with no keyword return or semicolon.
    // The last expression is implicitly returned.
    sum

}

fn empty_string_example() {

    // Creating an empty string object using the new() method.
    // Then setting its value to the word cat.
    let mut text3 = String::new();
    text3.push_str("cat");
    println!("text3 is: {text3}");

}