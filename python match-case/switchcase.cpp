#include <iostream>
 
int main()
{
    const int i =0;
    std::cout << "Input number: "; 
    std::cin >> i;
    switch (i) {
        case 1: 
            std::cout << "1";
            break;
        case 2: 
            std::cout << "2";
            break; 
        case 3: 
            std::cout << "3"; 
            break;
        case 4: 
            std::cout << "4";
            break;
        case 5: 
            std::cout << "5";
            break;
        case 6: 
            std::cout << "6";
            break;
        default: 
            std::cout << "default";
            break;
    }
}