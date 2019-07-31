const GOLDEN_RATIO = (1 + Math.sqrt(5)) / 2;

function get_fib_num(k) {
  const num = GOLDEN_RATIO ** k - (-GOLDEN_RATIO) ** -k;

  return num / Math.sqrt(5);
}

function get_even_sum(n) {
  sum = 3;
  let i = 3;
  let fib_num = get_fib_num(i);
  while (fib_num <= n) {
    sum += fib_num;
    i += 3;
    fib_num = get_fib_num(i);
  }
  return sum;
}

console.log(get_even_sum(100));
