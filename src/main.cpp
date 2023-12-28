#include <iostream>

#include "MyMath.h"
using namespace std;

int main() {
    cout << "Hello World!" << endl;
    cout << "This is a test" << endl;
    cout << "4 + 3 = " << MyMath::add(4, 3) << endl;
    cout << "4 - 3 = " << MyMath::subtract(4, 3) << endl;
    cout << "4 * 3 = " << MyMath::multiply(4, 3) << endl;
    cout << "4 / 3 = " << MyMath::divide(4, 3) << endl;
    return 0;
}
