/**
 * Complete the primality function in the editor below.
 * It should return Prime if  is prime, or Not prime.
 */
function primality(n) {
  for (let i = 2; i < Math.sqrt(n); i++) {
    if (n % i == 0) {
      return 'NOT PRIME';
    }
  }
  return 'PRIME';
}

console.log(primality(12));
console.log(primality(5));
console.log(primality(7));
