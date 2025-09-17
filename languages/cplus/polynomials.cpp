#include<iostream>
using namespace std;
const int MAX = 10;

class Poly
{
    private:
        struct term
        {
            int coeff;
            int exp;
        }t[MAX];
        int noofterms;

    public:
        Poly();
        void poly_append(int c, int e);
        void poly_add(Poly &p1, Poly &p2);
        void display();
}

Poly::Poly()
{
    noofterms = 0;
    for (int i = 0; i < MAX; i++)
    {
        t[i].coeff = 0;
        t[i].exp = 0;
    }
}

void Poly::poly_append(int c, int e)
{
    t[noofterms] = c;
    t[noofterms] = e;
    noofterms++;
}

void Poly::display()
{
    int flag = 0;
    for (int i = 0; i < noofterms; i++)
    {
        if (t[i].exp != 0)
        {
            cout << t[i].coff << "x^" << t[i].exp << "+";
        } else {
            cout << t[i].coeff;
            flag = 1;
        }

        if (flag)
            cout << "\b\b ";
    }
}

void Poly::poly_add(Poly &p1, Poly &p2)
{
    int c = (p1.noofterms > p2.noofterms)
            ? p1.noofterms
            : p2.noofterms;

    for (int i = 0, j = 0; i < c; noofterms++)
    {
        if (p1.t[i].coeff == 0 && p1.t[j].coeff == 0)
            break;
        if (p1.t[i].exp >= p2.t[j].exp)
        {
            if (p1.t[i].exp == p2.t[j].exp)
            {
                t[noofterms].coeff = p1.t[i].coeff + p2.t[j].coeff;
                t[noofterms].exp = p1.t[i].exp;
                i++;
                j++;
            }
            else
            {
                t[noofterms].coeff = p1.t[i].coeff;
                t[noofterms].exp = p1.t[i].exp;
                i++;
            }
        }
        else
        {
            t[noofterms].coeff = p2.t[j].coeff;
            t[noofterms].exp = p2.t[j].exp;
            j++;
        }
    }
}

int main()
{
    Poly p1;
    p1.poly_append(1, 7);
    p1.poly_append(2, 6);
    p1.poly_append(3, 5);
    p1.poly_append(4, 4);
    p1.poly_append(5, 2);

    Poly p2;
    p2.poly_append(1, 4);
    p2.poly_append(1, 3);
    p2.poly_append(1, 2);
    p2.poly_append(1, 1);
    p2.poly_append(2, 0);

    Poly p3;
    p3.poly_add(p1, p2);

    cout << endl << "First Polynomial: " << endl;
    p1.display();

    cout << endl << "Second Polynomial: " << endl;
    p2.display();

    cout << endl << "Resultant Polynomial: " << endl;
    p3.display();

}
