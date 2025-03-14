
fn container_examples() {

    // A tuple is a compound data type. It has a fixed length and the index starts from 0.
    // Declare a tuple with 3 string literals.
    let colors: (&str, &str, &str) = ("blue", "green", "red");
    println!("\ncolors: {:?}", colors);
    println!("The 1st item: {:?}, 2nd: {:?}, 3rd: {:?}", colors.0, colors.1, colors.2);

    // Convert a tuple into an array.
    let colors_array: [&str; 3] = colors.into();
    println!("colors converted into array: {:?}", colors_array);

    // Loop through the array.
    for each_item in colors_array.iter() {
        println!("color: {each_item}");

        // Option 1:
        // if each_item.to_string() == "red" {
        //     println!();
        // }

        // Option 2:
        if *each_item == "red" {
            println!();
        }
    }

    // Declare a mutable array of fixed size 3, with 3 string literals.
    let types: [&str; 3] = ["grass", "fire", "water"];

    println!("types array: {:?} - has length: {}", types, types.len());
    // Loop through the array.
    for each_item in types.iter() {
        println!("type: {each_item}");
        if *each_item == "water" {
            println!();
        }
    }

    // Declare a vector of strings. Vectors are dynamic arrays that can modified.
    let mut v_types: Vec<&str> = vec!["grass", "fire", "water"];

    // Add more elements to the vector.
    v_types.push("electric");
    v_types.push("ground");

    println!("v_types vector: {:?}", v_types);
    println!("The first item is: {}", v_types[0]);

    for each_item in v_types.iter() {
        println!("v_type: {each_item}");

        if *each_item == "ground" {
            println!();
        }
    }

    let dog:&str = "Logan";
    print_type("dog", &dog);
    println!();

}
fn print_type<T>(var_name: &str, _: &T) {
    // Identifies the data type. To use, type: print_type(&variable_name).
    // You must use the character & before the name.
    // The & symbol is used to reference the variable rather than passing the variable itself.
    println!("Variable name: {} - data type: {}", var_name, std::any::type_name::<T>());
}

fn main() {
    container_examples();
}
