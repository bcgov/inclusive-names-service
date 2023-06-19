Graphemes are totally doable in C++ but the exercise is left in charge of the reader as I could not find a library to implement it quickly but as variables are just bytes you can easily implement something that follows the specification.

The library that looked the best was ICU
https://icu.unicode.org/

Compiled with g++ `g++ -std=c++17 utf8.cpp`