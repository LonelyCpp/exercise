/**
 * You have an array with all the numbers from 1 to N,
 * where N is at most 32,000. The array may have duplicate
 * entries and you do not know what N is. With only
 * 4 kilobytes of memory available, how would you print
 * all duplicate elements in the array?
 */

class BitSet {
  constructor(size, initialVal = false) {
    this.arr = Array(size).fill(initialVal);
  }

  set(index) {
    this.arr[index] = true;
  }

  unset(index) {
    this.arr[index] = false;
  }

  check(index) {
    return this.arr[index];
  }

  toString() {
    return String(this.arr);
  }
}

function findDuplicates(arr) {
  const table = new BitSet(arr.length);
  arr.forEach(element => {
    if (table.check(element)) {
      console.log(element);
    } else {
      table.set(element);
    }
  });
}

inp = [1, 2, 3, 4, 5, 6, 6, 7, 8];
findDuplicates(inp);
inp = [1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 2, 7, 9, 10];
findDuplicates(inp);
