# Multi-sized Font for Raspberry Pi Pico LCD/OLED Displays
# Existing framebuf library only supports 8*8 font size
# lcd_write method has been implemented in the LCD_1inch3
# class inside the lcd_lib.py file

from lcd_lib import LCD_1inch3

LCD = LCD_1inch3()
LCD.fill(LCD.black)

LCD.write_text('Size 1',x=0,y=0,size=1,color=LCD.white)
LCD.write_text('Size 2',x=0,y=50,size=2,color=LCD.white)
LCD.write_text('Size 3',x=0,y=100,size=3,color=LCD.white)
LCD.write_text('Size 4',x=0,y=150,size=4,color=LCD.white)
LCD.write_text('Size 5',x=0,y=200,size=5,color=LCD.white)

LCD.show()
        
