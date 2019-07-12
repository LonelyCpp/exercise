/*
Add Without Plus: Write a function that adds two numbers.
You should not use+ or any arithmetic operators.
*/

#include <iostream>
#include <string>
#include <utility>

std::pair<int, int> full_adder(unsigned a, unsigned b, unsigned carry_in)
{
  int sum = a ^ b ^ carry_in;
  int carry_out = (carry_in & (a ^ b)) | (a & b);
  return std::pair<int, int>(sum, carry_out);
}
/**
 * only supports unsigned integers for now
 */
int add(unsigned num1, unsigned num2)
{
  int carry = 0;
  int sum = 0;
  int i;
  for (i = 0; num1 | num2; i++)
  {
    int lsb1 = num1 & 1;
    int lsb2 = num2 & 1;
    std::pair<int, int> res = full_adder(lsb1, lsb2, carry);
    carry = res.second;
    sum = sum | (res.first << i);
    num1 = num1 >> 1;
    num2 = num2 >> 1;
  }
  sum = sum | (carry << i);
  return sum;
}

std::string test(int calculated, int expected)
{
  return calculated == expected ? "pass" : "fail";
}

int main()
{
  std::cout << test(add(1, 1), 2) << std::endl;
  std::cout << test(add(1, 2), 3) << std::endl;
  std::cout << test(add(0, 10), 10) << std::endl;
  std::cout << test(add(22, 14), 36) << std::endl;

  return 0;
}