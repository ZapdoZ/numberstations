Python script that emulates real numbers stations
## Required libraries

    playsound
    multiprocess

## Usage
Open interface.py  

## The stations
Supported stations and layouts (single message formats):
- E11: https://i0.wp.com/www.numbers-stations.com/sites/default/files/E11a.jpg?resize=522%2C153
- E07: http://priyom.org/number-stations/english/e07
- E07a: http://priyom.org/number-stations/english/e07a
- S11a: https://i0.wp.com/www.numbers-stations.com/sites/default/files/E11a.jpg?resize=522%2C153 (basically the same as E11)
- G06: https://i2.wp.com/www.numbers-stations.com/sites/default/files/G06.jpg?resize=548%2C117

## Text file layouts
The first line of the text file has to be the mode you want to use  
Example files for all modes are given  
Text file layout for E11 or S11a:

    E11 (or S11a)
    Any 3-digit ID
    The Group count
    The 5-digit groups

Text file layout for E07:

    E07
    Any 3-Digit ID
    A 3/4-digit group
    The group count
    The 5-digit groups

Text file layout for E07a:

    E07a
    Any 3-Digit ID
    The extra 5-digit group
    A 3/4-digit group
    The group count
    The 5-digit groups

Text file layout for G06:

    G06
    Any 3-Digit ID
    A 3-digit group
    The group count
    The 5-digit groups
