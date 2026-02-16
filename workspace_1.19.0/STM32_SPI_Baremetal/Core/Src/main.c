#include <stdint.h>

/* Base addresses */
#define PERIPH_BASE        0x40000000UL
#define AHB2PERIPH_BASE    (PERIPH_BASE + 0x08000000UL)
#define APB2PERIPH_BASE    (PERIPH_BASE + 0x00010000UL)

/* RCC */
#define RCC_BASE           (AHB2PERIPH_BASE + 0x1000)
#define RCC_AHB2ENR        (*(volatile uint32_t*)(RCC_BASE + 0x4C))
#define RCC_APB2ENR        (*(volatile uint32_t*)(RCC_BASE + 0x60))

/* GPIOA */
#define GPIOA_BASE         (AHB2PERIPH_BASE + 0x0000)
#define GPIOA_MODER        (*(volatile uint32_t*)(GPIOA_BASE + 0x00))
#define GPIOA_AFRL         (*(volatile uint32_t*)(GPIOA_BASE + 0x20))
#define GPIOA_OSPEEDR      (*(volatile uint32_t*)(GPIOA_BASE + 0x08))

/* SPI1 */
#define SPI1_BASE          (APB2PERIPH_BASE + 0x3000)
#define SPI1_CR1           (*(volatile uint32_t*)(SPI1_BASE + 0x00))
#define SPI1_CR2           (*(volatile uint32_t*)(SPI1_BASE + 0x04))
#define SPI1_SR            (*(volatile uint32_t*)(SPI1_BASE + 0x08))
#define SPI1_DR            (*(volatile uint32_t*)(SPI1_BASE + 0x0C))

/* Function Prototypes */
void SPI1_Init(void);
uint8_t SPI1_Transfer(uint8_t data);

int main(void)
{
    SPI1_Init();

    uint8_t tx = 0x55;
    uint8_t rx;

    while(1)
    {
        rx = SPI1_Transfer(tx);

        if(rx == tx)
        {
            // SUCCESS
        }
        else
        {
            // ERROR
        }

        for(volatile int i=0;i<500000;i++);  // delay
    }
}

/* SPI Initialization */
void SPI1_Init(void)
{
    /* Enable GPIOA clock */
    RCC_AHB2ENR |= (1 << 0);

    /* Enable SPI1 clock */
    RCC_APB2ENR |= (1 << 12);

    /* PA5, PA6, PA7 -> Alternate Function */
    GPIOA_MODER &= ~((3<<(5*2)) | (3<<(6*2)) | (3<<(7*2)));
    GPIOA_MODER |=  ((2<<(5*2)) | (2<<(6*2)) | (2<<(7*2)));

    /* High speed */
    GPIOA_OSPEEDR |= ((3<<(5*2)) | (3<<(6*2)) | (3<<(7*2)));

    /* AF5 for SPI1 */
    GPIOA_AFRL &= ~((0xF<<(5*4)) | (0xF<<(6*4)) | (0xF<<(7*4)));
    GPIOA_AFRL |=  ((5<<(5*4)) | (5<<(6*4)) | (5<<(7*4)));

    /* Reset SPI */
    SPI1_CR1 = 0;

    /* Master mode */
    SPI1_CR1 |= (1 << 2);

    /* Baud rate = fPCLK/16 */
    SPI1_CR1 |= (3 << 3);

    /* slave management */
    SPI1_CR1 |= (1 << 9);
    SPI1_CR1 |= (1 << 8);

    /* 8-bit data */
    SPI1_CR2 = 0;
    SPI1_CR2 |= (7 << 8);
    SPI1_CR2 |= (1 << 12);

    /* Enable SPI */
    SPI1_CR1 |= (1 << 6);
}


uint8_t SPI1_Transfer(uint8_t data)
{
    /* Wait TXE */
    while(!(SPI1_SR & (1 << 1)));

    *((volatile uint8_t*)&SPI1_DR) = data;

    /* Wait RXNE */
    while(!(SPI1_SR & (1 << 0)));

    return *((volatile uint8_t*)&SPI1_DR);
}
