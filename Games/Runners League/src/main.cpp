#include <iostream>
#include <string>
using namespace std;

void mainMenu()
{
    int user_choice;
    cout << string(5, '*') << " Welcome to Runners League! " << string(5, '*') << endl;
    cout << '*' << " 1. Enter Game                      " << "*" << endl;
    cout << '*' << " 2. Settings                        " << "*" << endl;
    cout << '*' << " 3. Exit Game                       " << "*" << endl;
    cout << "Enter a number: ";
    cin >> user_choice;
    cout << user_choice << endl;
}

int main()
{
    mainMenu();
    return 0;
}