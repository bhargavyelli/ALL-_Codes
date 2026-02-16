#include<stm32l4xx_hal.h>
#include<stm32l476xx.h>
void uart_init();
void Error_Handler(void);
// USART2 Connectd to APB1 Bus
UART_HandleTypeDef huart2;

char message[20] = "Hello\r\n";

int main()
{
	HAL_Init();
	uart_init();


	while(1)
	{
		HAL_UART_Transmit(&huart2,(uint8_t *)message,20,100);
		//HAL_Delay(10);
	}
}

void Error_Handler(void)
{
    // Optional: add some error indication here, like blinking an LED or infinite loop
    while(1)
    {
    }
}

void uart_init()
{


	GPIO_InitTypeDef   GPIO_InitStruct = {0};

	//enable clock for uart pins
	__HAL_RCC_GPIOA_CLK_ENABLE();

	//enable clock for uart module
	__HAL_RCC_USART2_CLK_ENABLE();

	//Configure Pins fo r
	GPIO_InitStruct.Pin = GPIO_PIN_2 | GPIO_PIN_3;
	GPIO_InitStruct.Mode =  GPIO_MODE_AF_PP;
	GPIO_InitStruct.Alternate = GPIO_AF7_USART2;
	GPIO_InitStruct.Pull = GPIO_NOPULL;
	GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_VERY_HIGH;

	HAL_GPIO_Init(GPIOA,&GPIO_InitStruct);

	//Configure UART Module
	huart2.Instance	= USART2;

	huart2.Init.BaudRate = 9600;
	huart2.Init.WordLength = UART_WORDLENGTH_8B;
	huart2.Init.StopBits = UART_STOPBITS_1;
	huart2.Init.Parity = UART_PARITY_NONE;
	huart2.Init.Mode = UART_MODE_TX;
	huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
	huart2.Init.OverSampling = UART_OVERSAMPLING_16;

	HAL_UART_Init(&huart2);
}
