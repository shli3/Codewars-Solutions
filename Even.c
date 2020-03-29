#include <stdbool.h>
#include <math.h>

bool is_even(double n)
{  
    if(fmod(n, 2) == 0) return true;
    else return false;
}
