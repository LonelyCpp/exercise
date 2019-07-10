/*
Given a string, write a function to check if it
is a permutation of a palin­ drome. A palindrome
is a word or phrase that is the same forwards
and backwards. A permutation is a rearrangement
of letters. The palindrome does not need to be
limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
*/

#include <iostream>
#include <map>
#include <string>

std::string permuPal(std::string str)
{
  std::map<char, int> counter;
  for (char c : str)
    ++counter[c];

  const int STR_LEN = str.length();
  bool odd_flag = false;
  for (auto itr = counter.begin(); itr != counter.end(); itr++)
  {
    if (itr->second % 2 == 0)
      continue;

    if (STR_LEN % 2 == 0)
      return "false";

    if (!odd_flag)
    {
      odd_flag = true;
    }
    else
    {
      return "false";
    }
  }
  return "true";
}

int main()
{
  std::cout << permuPal("hello") << std::endl;
  std::cout << permuPal("abcba") << std::endl;
  std::cout << permuPal("abcfba") << std::endl;
  std::cout << permuPal("aaaaav") << std::endl;
  std::cout << permuPal("aaaaavv") << std::endl;
  return 0;
}
