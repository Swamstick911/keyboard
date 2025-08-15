# Mechatron

## About

Mechatron is a 65% mechanical keyboard. It has some features listed below:
- An OLED Display [SSD1306]
- A Rotary Encoder [EC11]
- RGB Underglow
- Tactile Switches

---

## Firmware

The firmware will be KMK which will be written in micropython, as I am using a Raspberry Pi Pico, it makes this easier. Still working on the firmware of the keyboard, for updates check the JOURNAL.md file!

---

## Bill of Materials (BOM)

| Reference     | Qty | Component                 | Footprint                                               | Datasheet                                                                                      | Buy Link                                                                                     |
|--------------|-----|---------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| A1           | 1   | Raspberry Pi Pico          | Module:RaspberryPi_Pico_Common_Unspecified              | [Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)                      | [Buy](https://www.raspberrypi.com/products/raspberry-pi-pico/)                              |
| D1-D80       | 80  | 1N4148 Diode               | Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal              | [Datasheet](https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf)              | [Buy](https://www.digikey.in/en/products/detail/nexperia-usa-inc/1N4148/458366)             |
| D91-D98      | 8   | WS2812B RGB LED            | LED_SMD:LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm              | [Datasheet](https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf)                            | [Buy](https://www.adafruit.com/product/1655)                                                |
| J1           | 1   | Header 1x4 (I2C OLED)      | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical | [Datasheet](https://www.amphenol.com/products/20021121-00010T4LF)                            | [Buy](https://www.digikey.in/en/products/detail/amphenol-fci/20021121-00010T4LF/10014539)   |
| SW1-SW87     | 80  | MX Switch 3-pin            | MX_SW:SW_MX_Kailh_HS                                    | [Datasheet](https://cdn.sparkfun.com/datasheets/Components/Switches/MX%20Series.pdf)         | [Buy](https://www.tme.eu/en/details/mx1a-11nw/switches/mechanical-keyboard/mx/)             |
| OLED1        | 1   | 0.96 I2C OLED Display      | OLED_Display:SSD1306_I2C                                | [Datasheet](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf)                            | [Buy](https://www.adafruit.com/product/326)                                                 |
| ENC1         | 1   | Rotary Encoder EC11 w/ Push| Encoder:EC11_PushButton                                 | [Datasheet](https://cdn.sparkfun.com/datasheets/Components/Encoders/EC11.pdf)                | [Buy](https://www.adafruit.com/product/377)                                                 |
| U1           | 1   | I2C Expander (PCF8574)     | SOP:SO-16_3.9mm                                         | [Datasheet](https://www.ti.com/lit/ds/symlink/pcf8574.pdf)                                   | [Buy](https://www.digikey.in/en/products/detail/nxp-usa-inc/PCF8574T-3-518/735505)          |

---

## Images:

<img width="947" height="396" alt="image" src="https://github.com/user-attachments/assets/23307d84-532a-4620-87aa-27841d974a06" />

<img width="1042" height="438" alt="image" src="https://github.com/user-attachments/assets/5a20deca-5194-4cf9-9fa9-8ea70c4dfce2" />

<img width="1003" height="394" alt="image" src="https://github.com/user-attachments/assets/db14ce97-7b15-4eb7-8785-4012686d9613" />

<img width="1008" height="405" alt="image" src="https://github.com/user-attachments/assets/71c85244-3d2b-4b65-bc5d-1ea1e2b0d15a" />

<img width="581" height="250" alt="image" src="https://github.com/user-attachments/assets/9db45b0f-c265-4f70-8926-f434161a9aef" />

<img width="989" height="687" alt="image" src="https://github.com/user-attachments/assets/fc909aff-5727-4464-85d4-58fc3c4fbb3d" />

<img width="844" height="359" alt="image" src="https://github.com/user-attachments/assets/7068835a-7081-414e-be55-87a740538b16" />


---
