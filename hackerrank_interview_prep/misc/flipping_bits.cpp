/**
 * You will be given a list of 32 bit unsigned integers.
 * Flip all the bits ( and ) and print the result as an
 * unsigned integer.
 */
#include <iostream>
#include <bitset>

using namespace std;

long long flippingBitsEasy(long n)
{
  bitset<32> num(n);
  num.flip();
  return num.to_ullong();
}

long flippingBits(long n)
{
  long flipped = 0;
  for (int i = 0; i < 32; i++)
  {
    long lastBit = !(n & 1);
    lastBit = lastBit << i;
    flipped = flipped | lastBit;
    n = n >> 1;
  }
  return flipped;
}

int main()
{
  cout << flippingBitsEasy(9) << endl;
  cout << flippingBits(9) << endl;
  return 0;
}
