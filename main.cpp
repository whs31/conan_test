#include <iostream>
#include <spdlog/spdlog.h>

int main()
{
  std::cout << "Hello, World!" << std::endl;
  spdlog::warn("{}", 1);
  spdlog::error("{}", 2);
  return 0;
}
