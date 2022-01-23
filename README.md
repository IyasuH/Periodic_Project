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
I arragnge the LEDs as two group of matrix to arrange them for the **MAX7219** controler where the first matrix of LED have 64 LEDs and the other matrix contains 54 LEDs. The main reason I confiugre the LEDs this way is to make coding of the MAX7219 easier and clear.

I connected the LEDs and the **MAX7219 IC drive** as the following diagram.
![max7219 and led connection](https://electronoobs.com/images/Arduino/tut_14/max_logo.png)
And I connect the two **MAX7219 drivers** as the followinf diagram
![max7219 and led connection](https://foto.askix.com/upload/2/29/229a8791cd375f9c0ee27f4816106142.jpg)
As you can see it from the above diagram I parralely conect the 5v and GND pins.And I connect CLK pins of both drivers together and also the LOAD pins and the dataout of the first **MAX7219** to the datain of the second one.