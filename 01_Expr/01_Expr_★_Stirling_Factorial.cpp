#include <iostream>
#include <cmath>

int main(){
    int n;
    std::cin >> n;
    float pi = 3.14159265358979323846;
    float tmp = pow(sqrt(pi*2)*n,(n+0.5));
    std::cout << tmp;
}
