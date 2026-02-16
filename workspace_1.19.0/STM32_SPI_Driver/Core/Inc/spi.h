#ifndef SPI_H_
#define SPI_H_

#include "stm32l476xx.h"

void SPI1_Init(void);
uint8_t SPI1_Transfer(uint8_t data);

#endif
