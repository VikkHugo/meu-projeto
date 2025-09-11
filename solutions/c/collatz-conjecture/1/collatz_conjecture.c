#include "collatz_conjecture.h"

int steps(int start){
    int contador = 0; 
    int numero = start; 

    if (numero <= 0) {
        return -1; 
    }
    
    while (numero > 1){ 
        if (numero % 2 == 0) {
            numero = numero / 2; 
            contador++; 
        }
        else {
            numero = 3 * numero + 1; 
            contador++; 
        }
    }
    return contador; 
}