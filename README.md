Python script that emulates real numbers stations
## Required libraries

    playsound

## Usage
Launch "main.py <textfile.txt>" in the CLI of your choice.  

## The stations
So far, this script supports E11, E07, E07a and S11a (single message formats; I'm working on more!).
E07's message format can be viewed here: http://priyom.org/number-stations/english/e07 .
E07a here: http://priyom.org/number-stations/english/e07a
and E11 (which is basically the same as S11a) here: https://i0.wp.com/www.numbers-stations.com/sites/default/files/E11a.jpg?resize=522%2C153 .

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
