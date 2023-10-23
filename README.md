# raspberry-sem01-m08

## Manual de referência

Link para o manual de referência: <https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf> .

## Interfaces de comunicação com componentes externos

### GPIO (General Purpose Input/Output):
Os pinos GPIO permitem que você se comunique com outros dispositivos e periféricos digitais. Eles podem ser configurados como entradas (para leitura de dados) ou saídas (para envio de dados). O Raspberry Pi Pico W possui um total de 30 pinos GPIO.

### UART (Universal Asynchronous Receiver/Transmitter):

O Raspberry Pi Pico W suporta comunicação UART, que é uma interface serial assíncrona usada para a comunicação com dispositivos externos, como sensores, módulos GPS, e outros microcontroladores.

### SPI (Serial Peripheral Interface):

A interface SPI é usada para comunicação serial síncrona de alta velocidade com dispositivos como displays TFT, sensores de pressão e memórias flash. O Raspberry Pi Pico W oferece suporte a 2 barramentos SPI.

### I2C (Inter-Integrated Circuit):

A interface I2C é um barramento serial de comunicação de dois fios que é amplamente usado para conectar sensores e dispositivos periféricos, como acelerômetros, giroscópios e displays OLED.

### PWM (Pulse Width Modulation):

Os pinos PWM permitem a geração de sinais PWM para controlar dispositivos como servomotores e LEDs. Essa é uma técnica usada para controlar a intensidade luminosa, a velocidade do motor, entre outros.

### ADC (Analog-to-Digital Converter):

O Raspberry Pi Pico W possui pinos ADC que podem ser usados para converter sinais analógicos em valores digitais. Isso é útil para leitura de sensores analógicos, como sensores de temperatura e umidade.

### Onboard Temperature Sensor:

O Pico W possui um sensor de temperatura integrado que pode ser acessado por meio do Raspberry Pi Pico SDK para leitura da temperatura do microcontrolador.

### Wi-Fi:

O Raspberry Pi Pico W suporta conectividade Wi-Fi. Isso permite que o Pico W se conecte a redes sem fio e comunique-se com servidores ou outros dispositivos na rede.