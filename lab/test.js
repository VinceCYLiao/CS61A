const search = fn => {
    let x = 0;
    while (!fn(x)) {
        x = x + 1;
    }
    return x;
}

const square = x => x * x;

const inverse = fn => y => search(x => fn(x) === y);

const sqrt = inverse(square);

console.log(sqrt(16));