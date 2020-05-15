#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int k=-n;k<= n;++k)
    {
        int num=n-abs(k);
        for(int i=0;i<abs(k);++i)
        {
            cout<<"  ";
        }
        for(int i=0;i<num;++i)
        {
            cout<<i<<" ";
        }
        for(int i=num;i>0;--i)
        {
            cout<<i<<" ";
        }
        cout<<0<<endl;
    }
    return 0;
}
