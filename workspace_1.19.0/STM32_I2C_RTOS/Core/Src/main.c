#include "stm32l4xx.h"
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include <math.h>

#define OPT3001_ADDR 0x44

SemaphoreHandle_t i2cMutex;
volatile float g_luxValue = 0;


void I2C1_Init(void)
{
    RCC->AHB2ENR |= RCC_AHB2ENR_GPIOBEN;
    RCC->APB1ENR1 |= RCC_APB1ENR1_I2C1EN;

    /* PB8=SCL, PB9=SDA */
    GPIOB->MODER &= ~((3<<(8*2)) | (3<<(9*2)));
    GPIOB->MODER |=  (2<<(8*2)) | (2<<(9*2));

    GPIOB->OTYPER |= (1<<8) | (1<<9);
    GPIOB->OSPEEDR |= (3<<(8*2)) | (3<<(9*2));

    GPIOB->PUPDR &= ~((3<<(8*2)) | (3<<(9*2)));
    GPIOB->PUPDR |=  (1<<(8*2)) | (1<<(9*2));

    GPIOB->AFR[1] |= (4<<0) | (4<<4);

    I2C1->CR1 &= ~I2C_CR1_PE;
    I2C1->TIMINGR = 0x0010061A;
    I2C1->CR1 |= I2C_CR1_PE;
}



void I2C1_ReadMulti(uint8_t devAddr, uint8_t reg, uint8_t *buf, uint8_t len)
{
    while(I2C1->ISR & I2C_ISR_BUSY);


    I2C1->CR2 = (devAddr << 1) | (1 << 16);
    I2C1->CR2 |= I2C_CR2_START;

    while(!(I2C1->ISR & I2C_ISR_TXIS));
    I2C1->TXDR = reg;

    while(!(I2C1->ISR & I2C_ISR_TC));


    I2C1->CR2 = (devAddr << 1) |
                (len << 16) |
                I2C_CR2_RD_WRN |
                I2C_CR2_AUTOEND;

    I2C1->CR2 |= I2C_CR2_START;

    for(int i=0; i<len; i++)
    {
        while(!(I2C1->ISR & I2C_ISR_RXNE));
        buf[i] = I2C1->RXDR;
    }

    while(!(I2C1->ISR & I2C_ISR_STOPF));
    I2C1->ICR |= I2C_ICR_STOPCF;
}



float OPT3001_ReadLux(void)
{
    uint8_t raw[2];
    uint16_t value;
    uint16_t mantissa;
    uint8_t exponent;

    I2C1_ReadMulti(OPT3001_ADDR, 0x00, raw, 2);

    value = (raw[0] << 8) | raw[1];
    exponent = (value >> 12) & 0x0F;
    mantissa = value & 0x0FFF;

    return (0.01f * powf(2, exponent)) * mantissa;
}



void vLuxTask(void *pvParameters)
{
    while(1)
    {
        if(xSemaphoreTake(i2cMutex, portMAX_DELAY) == pdTRUE)
        {
            g_luxValue = OPT3001_ReadLux();
            xSemaphoreGive(i2cMutex);
        }

        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}


int main(void)
{
    I2C1_Init();

    i2cMutex = xSemaphoreCreateMutex();

    xTaskCreate(vLuxTask,
                "LuxTask",
                512,
                NULL,
                2,
                NULL);

    vTaskStartScheduler();

    while(1);
}
