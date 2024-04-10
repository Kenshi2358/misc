/*
Rust uses multi-line comments with /* */
Rust uses single line comments with //

The fn keyword is used to define a function.

To run this program:
1) you must compile is first by typing: rustc hello_world.rs
2) run the compiled code with: ./hello_world

Alternatively, you can run: cargo run to do both

On a macOS, there is no .exe file extension like on Windows.
MacOS relies on the Unix-like convention where executables don't have any specific extension.

The ./ prefix specifies are the file in the current directory.
The main() function is a predefined function that acts as an entry point to the program.

To check your versin of Rust, type: rustc -V
To check your version of Cargo, type: cargo -V
To update rust, type: rustup update

To create a new cargo package, type: cargo new project_name

Then you can quickly compile and run this with: cargo run

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

*/

fn main() {

    let works = "works";
    println!("I hope this {works}");
    println!("format {} arguments", "some");
    println!("Rust says Hello from the main function.");
    message();

}
fn message() {

    println!("This is a sentence.");
}