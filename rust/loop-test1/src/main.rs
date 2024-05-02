/*
Example showing all types of Rust loops.
Also includes continue and break statements.
*/

fn main() {
    
    // The upper bound is not inclusive.
    for i in 1..11 {
        if i == 5 {
            continue;
        }

        println!("for loop: i is: {i}");
    }

    let mut k = 3;
    while k < 6 {
        k += 1;
        println!("while loop: k is: {k}");
    }

    let mut n = 0;
    loop {
        n += 1;
        println!("loop loop: n is: {n}");

        if n == 5 {
            break;
        }
    }
}
