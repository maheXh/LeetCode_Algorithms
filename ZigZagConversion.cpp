#include <iostream>
using namespace std;

int main()
{
    int r;
    string s;
    cout << "Enter the string: ";
    getline(cin, s);
    cout << "Enter the number of rows: ";
    cin >> r;

    int c = s.length();

    char a[r][c] = {' '};

    int t = 0;
    int r1 = 0, c1 = 0;

    /* The code block you provided is responsible for filling a 2D character array `a` with characters
    from the input string `s` in a zigzag pattern. */
    while (t != c)
    {
        for (int i = 0; i < r - 1 && t != c; i++)
        {
            a[r1++][c1] = s[t++];
        }
        if (t == c)
        {
            break;
        }
        a[r1][c1] = s[t++];
        for (int i = 0; i < r - 2 && t != c; i++)
        {
            a[--r1][++c1] = s[t++];
        }
        r1--;
        c1++;
    }

    /* The code block you provided is responsible for printing the characters stored in the 2D
    character array `a` in a zigzag pattern. */
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (a[i][j] != ' ' && isalpha(a[i][j]) )
            {
                cout << a[i][j];
            }
        }
    }

    return 0;
}
