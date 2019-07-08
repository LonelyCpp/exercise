#include <string>
#include <iostream>

std::string trim(std::string str)
{

  int first_char_pos = -1;
  int last_char_pos = -1;

  // loop to determine where the first non-space-character occurs
  for (int i = 0; i < str.length(); i++)
  {
    if (str[i] == ' ')
      continue;
    first_char_pos = i;
    break;
  }

  // whole string is made of spaces
  if (first_char_pos == -1)
  {
    return "";
  }

  // loop to determine where the last non-space-character occurs
  for (int i = str.length() - 1; i >= 0; i--)
  {
    if (str[i] == ' ')
      continue;
    last_char_pos = i;
    break;
  }

  int sub_str_size = last_char_pos - first_char_pos + 1;
  return str.substr(first_char_pos, sub_str_size);
}

int main()
{
  std::cout << "'";
  std::cout << trim("  hello world  ");
  std::cout << "'" << std::endl;

  std::cout << "'";
  std::cout << trim("  hello world");
  std::cout << "'" << std::endl;

  std::cout << "'";
  std::cout << trim("hello world");
  std::cout << "'" << std::endl;

  std::cout << "'";
  std::cout << trim("");
  std::cout << "'" << std::endl;

  std::cout << "'";
  std::cout << trim("     ");
  std::cout << "'" << std::endl;

  std::cout << "'";
  std::cout << trim("   -  ");
  std::cout << "'" << std::endl;

  std::cout << "'";
  std::cout << trim("7");
  std::cout << "'" << std::endl;
  return 0;
}