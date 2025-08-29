#include "grains.h"
#include "math.h"

uint64_t square(uint8_t index){
    if (index > 64) {
        return 0;
    }
    else {
        return pow(2,index-1);
    }
}

uint64_t total(void){
    int total_graos = 0; 
    int contador; 
    for (contador = 1; contador <= 64; contador++) {
        total_graos = total_graos + square(contador); 
    }
    return total_graos; 
}
