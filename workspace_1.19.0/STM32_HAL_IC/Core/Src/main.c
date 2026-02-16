#include "stm32l4xx_hal.h"
#include "stm32l476xx.h"
#include <stdio.h>
#include <math.h>

void i2c_init();
void opt3001_init();
float opt3001_read_lux();
void Error_Handler(void);

#define device_addr (0x47 << 1)
volatile float lux;

I2C_HandleTypeDef h_I2C1;

int main()
{
    HAL_Init();
    i2c_init();
    opt3001_init();
    HAL_Delay(100);

    while(1)
    {
        lux = opt3001_read_lux();
        //HAL_Delay(1000);
    }
}



void Error_Handler(void)
{
    // Optional: add some error indication here, like blinking an LED or infinite loop
    while(1)
    {
    }
}

void i2c_init()
{
    GPIO_InitTypeDef GPIO_InitStruct = {0};

    __HAL_RCC_GPIOB_CLK_ENABLE();
    __HAL_RCC_I2C1_CLK_ENABLE();

    // PB6 = SCL, PB7 = SDA
    GPIO_InitStruct.Pin = GPIO_PIN_6 | GPIO_PIN_7;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_OD;
    GPIO_InitStruct.Pull = GPIO_PULLUP;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
    GPIO_InitStruct.Alternate = GPIO_AF4_I2C1;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

    h_I2C1.Instance = I2C1;
    h_I2C1.Init.Timing = 0x00707CBB;
    h_I2C1.Init.OwnAddress1 = 0;
    h_I2C1.Init.AddressingMode = I2C_ADDRESSINGMODE_7BIT;
    h_I2C1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLE;
    h_I2C1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
    h_I2C1.Init.NoStretchMode = I2C_NOSTRETCH_DISABLE;

    HAL_I2C_Init(&h_I2C1);
}


void opt3001_init()
{
    uint8_t data[3];
    uint16_t config = 0xC410;

    data[0] = 0x01;
    data[1] = config >> 8;
    data[2] = config & 0xFF;

    HAL_I2C_Master_Transmit(&h_I2C1, device_addr, data, 3, HAL_MAX_DELAY);
}

float opt3001_read_lux()
{
    uint8_t reg = 0x00;
    uint8_t rx[2];
    uint16_t raw;
    uint16_t exponent, mantissa;

    HAL_I2C_Master_Transmit(&h_I2C1, device_addr, &reg, 1, HAL_MAX_DELAY);
    HAL_I2C_Master_Receive(&h_I2C1, device_addr, rx, 2, HAL_MAX_DELAY);

    raw = (rx[0] << 8) | rx[1];

    exponent = (raw >> 12) & 0x0F;
    mantissa = raw & 0x0FFF;

    return (0.01 * pow(2, exponent)) * mantissa;
}
