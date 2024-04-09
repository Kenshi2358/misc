/* Your first rust program.
This defines a function called main.
The fn keyword is used to define a function. */

// fn
// main(){
//     println!("Rust says Hello")
// }

// This is a single line comment.

/* This is a
Multi-line comment
*/

// To run this program, you must compile it first by typing:
// rustc hello_world.rs
// Then run the compiled code with: ./hello_world

fn main() {

    message();

}
fn message() {

    println!("This is a sentence.");
}