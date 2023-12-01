use std::fs;


// First iteration - only designed to solve part 2
// Remove replace_words to get the solution for part 1
// pub fn day1_sol(filename: &str) -> i32 {
//     let content = fs::read_to_string(&filename)
//         .expect("Failed to read the file");

//     let calibrations = content.lines();

//     let mut rolling_sum: i32 = 0;

//     for calibration in calibrations {
//         let mut numbers_tracker = Vec::new();
//         let calibration = replace_words(calibration);

//         for ch in calibration.chars() {
//             if ch.is_digit(10) {
//                 numbers_tracker.push(ch);
//             }
//         }

//         rolling_sum += format!("{}{}",
//             numbers_tracker[0],
//             numbers_tracker[numbers_tracker.len() - 1])
//             .parse::<i32>()
//             .unwrap();
//     }

//     return rolling_sum

// }


// Working solution to both parts
pub fn day1_sol(filename: &str) -> (i32, i32) {
    let content = fs::read_to_string(&filename)
        .expect("Failed to read the file");

    let calibrations = content.lines();

    let mut sum_part1 = 0;
    let mut sum_part2 = 0;

    for calibration in calibrations {
        let initial_numbers = extract_first_last(calibration);
        sum_part1 += initial_numbers;

        let replaced_calibration = replace_words(calibration);
        let replaced_numbers = extract_first_last(&replaced_calibration);
        sum_part2 += replaced_numbers;
    }

    return (sum_part1, sum_part2)
}

fn extract_first_last(input: &str) -> i32 {
    let numbers: Vec<char> = input.chars().filter(|ch| ch.is_digit(10)).collect();

    // There's always a first and a last number, so we don't need to check length
    return format!("{}{}", numbers.first().unwrap(), numbers.last().unwrap())
        .parse::<i32>()
        .unwrap_or(0)

}

fn replace_words(input: &str) -> String {
    input
        .replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
}
