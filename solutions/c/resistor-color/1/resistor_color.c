#include "resistor_color.h"
const resistor_band_t cores[] = {
    BLACK,
    BROWN, 
    RED, 
    ORANGE, 
    YELLOW, 
    GREEN, 
    BLUE, 
    VIOLET, 
    GREY, 
    WHITE
};

unsigned int color_code(resistor_band_t color) {
    return color; 
}

const resistor_band_t* colors() {
    return (resistor_band_t * )&cores; 
}
