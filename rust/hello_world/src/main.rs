
fn message() {

    println!("hello from the message function.");
}

fn formatting_examples() {

    // Declare one variable with no data type and one variablea as a string literal, using the &str keyword.
    let text1 = "apple";
    let text2:&str = "orange";

    println!("\nFormatting with brackets and comma: {} and {}", text1, text2);

    let example = "like this";
    println!("Better formatting - formatting with brackets only: {example}\n");

}

fn string_append_examples() {

    println!("String append examples:");

    // Declare one variable with no data type and one variable as a string literal, using the &str keyword.
    let text1 = "dog";
    let text2:&str = "cat";

    let text3 = format!("{text1} {text2}");
    println!("text3 using format!: {text3}");

    // to_string() method converts a given value to a string.
    let text3 = text1.to_string() + " hat " + text2;
    println!("text3 using to_string(): {text3}");

    // Declare two variables as a string literal.
    let text4:&str = "mouse";
    let text5:&str = "deer";

    // You can also declare these 2 variables in one line, using tuple destructuring.
    // Both variables are inferred as data type: string literal, or &str.
    // let (text4, text5) = ("mouse", "deer");

    // to_owned() method creates owned data from borrowed data.
    let text6 = text4.to_owned() + " " + text5;
    println!("text6 using to_owned(): {text6}");

    // Declare a mutable variable, string object with text: jump.
    let mut combined_str = String::from("jump");

    // Show different ways to concatenate strings.
    combined_str.push_str(" run");
    combined_str += " skip";

    let text7 = " fly";
    combined_str += text7;

    combined_str = combined_str + " hop";

    println!("combined_str: {combined_str}\n");

}


fn computations1() {

    // Declare variable age with data type: 32 bit signed integer.
    let age:i32 = 255;

    let weight:i64 = 256;
    let height = 257;
    let mut score = 258;

    score += 5;

    println!("age is {age}  weight is {weight}  height is {height}  score is {score}");

    let int_with_separator = 50_000;
    println!("int_with_separator is: {int_with_separator}");

    let letter1:char = 'A';
    println!("letter1 is: {letter1}");

    let int1 = 5;
    let int2 = 10;
    let int3 = sum(int1, int2);
    println!("The value of int3 is: {int3}\n");
}

fn sum(int1:i32, int2:i32) -> i32 {

    let sum = int1 + int2;
    let threshold_num = 20;

    println!("The sum of {int1} and {int2} is: {sum}");

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
    // Then updating its value in different ways.
    let mut text3 = String::new();
    text3.push_str("blue");
    text3 += " house";
    println!("empty_string_example: {text3}\n");

}

fn main() {

    println!("\nhello from the main function.");
    message();

    formatting_examples();
    string_append_examples();

    computations1();
    empty_string_example();
}
