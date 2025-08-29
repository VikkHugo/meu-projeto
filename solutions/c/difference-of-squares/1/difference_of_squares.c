#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number){
    unsigned int soma_quadrados = 0; 
    unsigned int contador; 
    for (contador = 1; contador <= number; contador++) {
        soma_quadrados = soma_quadrados + (contador*contador); 
    }
    return soma_quadrados; 
}



unsigned int square_of_sum(unsigned int number){
    unsigned int contador; 
    unsigned int quadrado_soma = 0; 
    for (contador = 1; contador <= number; contador++){
        quadrado_soma = quadrado_soma + contador; 
    }
    quadrado_soma = quadrado_soma*quadrado_soma; 
    return quadrado_soma; 
}



unsigned int difference_of_squares(unsigned int number){
    return square_of_sum(number) - sum_of_squares(number);
}


