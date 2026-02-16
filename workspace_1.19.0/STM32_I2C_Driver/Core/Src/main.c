#include "stm32l4xx.h"
#include "i2c_driver.h"

void delay_ms(uint32_t d)
{
    for(uint32_t i=0;i<d*4000;i++);
}
float lux;
int main(void)
{
    I2C1_Init();


    while(1)
    {
        lux = OPT3001_ReadLux();
        delay_ms(500);
    }
}
