/*
Example showing all types of Rust loops.
Also includes continue and break statements.
*/

fn main() {
    
    // The upper bound is not inclusive. Iterates on i = 1, 2, 4.
    for i in 1..5 {
        if i == 3 {
            continue;
        }
        println!("for loop: i is: {i}");
    }

    // Iterates on k = 4, 5, 6
    let mut k = 3;
    while k < 6 {
        k += 1;
        println!("while loop: k is: {k}");
    }

    // Iterates on n = 1, 2, 3.
    let mut n = 0;
    loop {
        n += 1;
        println!("loop loop: n is: {n}");

        if n == 3 {
            break;
        }
    }
}
