# Periodic Project

##### The goal of this repo is to give you enough understanding of how the electronics and the code works
>This project is about creting an interactive periodic table as a teching aid for teachers to demonstrate different properties of elements and how different elements relate to each other to students.
> Electronics Used
* 118 white 4mm LEDs
* Arduino uno
* Hc-06 bluetooth module
* 2 MAX7219 IC drivers
* 2 24 leg IC bases
* 2 10 micro farad electrolyte capacitors
* 2 100 nano farad ceramic capacitors
* 2 3.3 killo ohm resitors
* 2 10 killo ohm resistors
* 1 and 2 killo ohm resistors
* 5x7cm PCB board
* And lots of jumper wires

#### Main concept

The main concept behinde this project is controling each LEDs individually and for this I used **MAX7219** IC Driver which is great tool which allows you to control upto 64 leds individually by multiplexing *you can see the datasheet here([max7219 datasheet](https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf))* and since there are 118 elements which means I have to light up 118 LEDs therefore I used 2 MAX7219 IC drivers. 
The display is controled by mobile app using Bluetooth connectivity and for that I used **HC-06 Bluetooth module** which you can use it to connect your microcontroler with any other divice and as a microcontroler I used **Arduino uno**

#### Circuit Schematic

###### LED arrangement
I arragnge the LEDs as two group of matrix to arrange them for the **MAX7219** controler where the first matrix of LED have 64 LEDs and the other matrix contains 54 LEDs. The main reason I confiugre the LEDs this way is to make coding of the **MAX7219** easier and clear. Then I arrange the LED matrix as the shape of periodic table (I put the LEDs in the postion of each elements) then I did soldering of the anodes and cathodes as the following schematic.

I connected the LEDs and the **MAX7219 IC drive** as the following diagram.

![max7219 and led connection](https://electronoobs.com/images/Arduino/tut_14/max_logo.png)

And I connect the two **MAX7219 drivers** as the following diagram.

![max7219 and led connection](https://foto.askix.com/upload/2/29/229a8791cd375f9c0ee27f4816106142.jpg)

As you can see it from the above diagram I connect CLK pins of both drivers together to pin 10 of arduino and also the LOAD pins of both drivers connect together to pin 11 of arduino. And the dataout of the first **MAX7219** to the datain of the second one. And the datain of the first one is connected to arduino pin 12. Therefore this way I can control the full LED matrix using only 5 pin from the arduino.

Then I used prototype board to solder the IC bases (for the MAX7219) capacitors and resistors.

###### Bluetooth connection

I connect the VCC and GND pins of the bluetooth pins to the 5V and GND of the arduino pins. Then the TX pin of the bluetooth pin to RX pin of arduino and RX pin to TX pin of the arduino by parallelly connecting 1k and 2k ohm resistors as the following diagram.

![Arduino and bluetooth connection](https://aws1.discourse-cdn.com/arduino/original/4X/8/f/c/8fc1fae064ae0a2a1bc7dcc515babf1a86923929.jpeg)