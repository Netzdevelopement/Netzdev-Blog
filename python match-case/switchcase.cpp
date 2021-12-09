#include <iostream>
 
int main()
{
    const int i =0;
    std::cout << "Input number: "; 
    std::cin >> i;
    switch (i) {
        case 1: std::cout << "1";
        case 2: std::cout << "2"; 
        case 3: std::cout << "3"; 
        case 4: std::cout << "4";
        case 5: std::cout << "5";
        case 6: std::cout << "6";
        default: std::cout << "default";
    }
}