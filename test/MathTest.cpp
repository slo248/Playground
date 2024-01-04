#include <iostream>
#include <stdexcept>

#include "MyMath.h"

int main() {
    try {
        if (MyMath::add(1, 2) != 3) throw std::runtime_error("1 + 2 != 3");
        if (MyMath::subtract(1, 2) != -1)
            throw std::runtime_error("1 - 2 != -1");
        if (MyMath::multiply(1, 2) != 2) throw std::runtime_error("1 * 2 != 2");
        if (MyMath::divide(1, 2) != 0) throw std::runtime_error("1 / 2 != 0");
    } catch (const std::exception& e) {
        std::cerr << e.what() << '\n';
    }

    return 0;
}
