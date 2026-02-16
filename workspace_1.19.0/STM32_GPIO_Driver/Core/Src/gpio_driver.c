#include "gpio_driver.h"

uint8_t mode = 0;
uint8_t ledState = 0;
uint32_t lastToggle = 0;
volatile uint32_t msTicks = 0;

void GPIO_Init(GPIO_RegDef_t *GPIOx, uint8_t pin, uint8_t mode,
               uint8_t otype, uint8_t speed, uint8_t pupd)
{
    /* Mode */
    GPIOx->MODER &= ~(3 << (pin * 2));
    GPIOx->MODER |= (mode << (pin * 2));

    /* Output Type */
    GPIOx->OTYPER &= ~(1 << pin);
    GPIOx->OTYPER |= (otype << pin);

    /* Speed */
    GPIOx->OSPEEDR &= ~(3 << (pin * 2));
    GPIOx->OSPEEDR |= (speed << (pin * 2));

    /* Pull-up/Pull-down */
    GPIOx->PUPDR &= ~(3 << (pin * 2));
    GPIOx->PUPDR |= (pupd << (pin * 2));
}

void GPIO_WritePin(GPIO_RegDef_t *GPIOx, uint8_t pin, uint8_t value)
{
    if(value)
        GPIOx->BSRR = (1 << pin);        // Set
    else
        GPIOx->BSRR = (1 << (pin + 16)); // Reset
}

void GPIO_TogglePin(GPIO_RegDef_t *GPIOx, uint8_t pin)
{
    GPIOx->ODR ^= (1 << pin);
}

uint8_t GPIO_ReadPin(GPIO_RegDef_t *GPIOx, uint8_t pin)
{
    return (GPIOx->IDR & (1 << pin)) ? 1 : 0;
}

void led_task(void)
{
    uint32_t interval;

    if(mode == 0) interval = 600;
    else if(mode == 1) interval = 300;
    else interval = 100;

    if(msTicks - lastToggle >= interval)
    {
        lastToggle = msTicks;
        ledState ^= 1;
        GPIO_WritePin(GPIOA, 5, ledState);
    }
//    ledState ^= 1;
//    GPIO_WritePin(GPIOA, 5, ledState);
//    for(int i=0;i<interval;i++);

}

void check_button(void)
{
    static uint8_t lastState = 1;
    uint8_t currentState = GPIO_ReadPin(GPIOC, 13);

    if(lastState == 1 && currentState == 0)
    {
        mode = (mode + 1) % 3;
    }
    lastState = currentState;
}
