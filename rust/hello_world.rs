/* Your first rust program.
Rust uses multi-line comments with /* */
Rust uses single line comments with //

The fn keyword is used to define a function.

To run this program:
1) you must compile is first by typing: rustc hello_world.rs
2) run the compiled code with: ./hello_world

On a macOS, there is no .exe file extension like on Windows.
MacOS relies on the Unix-like convention where executables don't have any specific extension.

The ./ prefix specifies are the file in the current directory.
The main() function is a predefined function that acts as an entry point to the program.
*/

fn main() {

    println!("Rust says Hello from the main function.");
    message();

}
fn message() {

    println!("This is a sentence.");
}