# pin definitions for the different boards used at SSIS
# in Advanced Automation with the Sphero RVR

import board

class pin:
    id = board.board_id
    if id == "stm32f411ce_blackpill_with_flash":
        TX      = board.A2
        RX      = board.A3
        TRIGGER = board.B1
        ECHO    = board.B0

    elif id == "raspberry_pi_pico":
        TX      = board.GP4
        RX      = board.GP5
        TRIGGER = board.GP10
        ECHO    = board.GP11

    elif id == "metro_m4_express":
        TX      = board.D1
        RX      = board.D0
        TRIGGER = board.D11
        ECHO    = board.D10

    elif id == "lilygo_ttgo_t8_s2_st7789":
        TX      = board.IO1
        RX      = board.IO2
        TRIGGER = board.IO5
        ECHO    = board.IO4

    else:
        print("No definition for UART and Ultrasonic pins found")
