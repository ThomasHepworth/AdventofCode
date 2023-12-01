fn modulo(a: i32, modulo: i32) -> i32 {
    return ((a % modulo) + modulo) % modulo
}

pub fn day2_sol(game_sheet: &str) -> (i32, i32) {

    let mut part1: i32 = 0;
    let mut part2: i32 = 0;

    for game in game_sheet.lines() {

        let game_plan: Vec<i32> = game
            .split_whitespace()
            .map(|play| ((play.as_bytes()[0] - b'A')%23) as i32)
            .collect();

        let (a, b) = (game_plan[0], game_plan[1]);

        part1 += vec![b+1, modulo(b-a+1, 3)*3].iter().sum::<i32>();
        part2 += vec![b*3, modulo(a+b-1, 3)+1].iter().sum::<i32>();

    }

    return (part1, part2)

}
