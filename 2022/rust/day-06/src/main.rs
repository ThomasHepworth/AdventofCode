use std::fs;
// use day_06::simple_for;
use day_06::simple;
use day_06::simple_stopper;

fn main() {
    // Define a string slice
    // let stream = fs::read_to_string("input.txt")
    // .expect("problem with the file");

    let stream: &str = "bvwbjplbgvbhsrlpgdmjqwftvncz";

    println!("Solution to part 2 - simple: {:#?}", simple(&stream));
    println!("Solution to part 2 - simple_stopper: {:#?}", simple_stopper(&stream));

}
