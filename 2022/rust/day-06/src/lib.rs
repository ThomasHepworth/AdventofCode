use std::collections::HashSet;

pub fn simple_for(stream: &str) -> usize {
    // A less elegant form of the function below...
    let n = 14;
    let length = stream.len()-n;

    for idx in 0..length {
        let mut unique_chars = HashSet::new();
        for c in stream.chars().skip(idx).take(n) {
            unique_chars.insert(c);
        }
        if unique_chars.len() == n {
            return idx+n
        }
    }
    return length
}

pub fn simple(stream: &str) -> usize {

    // Inefficient, but simple solution
    let position = stream.as_bytes()
    .windows(14)
    .position(|w| w.iter().collect::<HashSet<_>>().len() == 14);

    // return position; -- returns Some(usize)
    return position.unwrap();
}


pub fn simple_stopper(stream: &str) -> usize {
    // More efficient solution, exiting the hashset if a duplicate is found
    // rather than checking the len of the hashset of 14 chars

   let window_size = 14;

    'hashset_counter: for (n, w) in stream.as_bytes()
        .windows(window_size).enumerate() {
        let mut hash_set = HashSet::new();
        for c in w.into_iter() {

            if hash_set.contains(c) {
                continue 'hashset_counter;
            }
            hash_set.insert(c);
        }
        return n
    }
    return stream.len()

}
