#include "stm32l4xx.h"
#include "gpio_driver.h"


int main()
{
	SystemCoreClockUpdate();
	SysTick_Config(SystemCoreClock / 1000);

    GPIOA_CLK_EN();
    GPIOC_CLK_EN();

    // LED PA5
    GPIO_Init(GPIOA, 5, GPIO_MODE_OUTPUT,
              GPIO_OTYPE_PP, GPIO_SPEED_LOW, GPIO_NO_PUPD);

    // Button PC13
    GPIO_Init(GPIOC, 13, GPIO_MODE_INPUT,
              GPIO_OTYPE_PP, GPIO_SPEED_LOW, GPIO_NO_PUPD);

    GPIO_WritePin(GPIOA, 5, 0);


    while(1)
    {
        check_button();
        led_task();
    }
}





