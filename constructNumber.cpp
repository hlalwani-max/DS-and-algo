#include <iostream>
using namespace std;

int main(){
int array[3] = {3,2,1};
int sum = 0;
for (int i<=2; i>0; --i){
sum += array[i] * 10^i;
}
cout << sum;
}