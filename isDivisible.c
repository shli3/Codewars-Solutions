#include <stdbool.h>
#include <stdio.h>

bool isDivisible(int n, int x, int y) {

    if(n%x == 0 && n%y == 0) return true;
    else return false;
   
}
