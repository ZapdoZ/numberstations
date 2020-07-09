# numberstations
Python script that emulates real numbers stations  
Required libraries:  
- playsound

Usage:  
Launch main.py <textfile.txt> in the CLI of your choice.  

The stations:  
So far, this script supports E11 and E07 (single message formats; I'm working on more!).  
E07's message format can be viewed here: http://priyom.org/number-stations/english/e07 .  
E11's message format can be viewed here: https://i0.wp.com/www.numbers-stations.com/sites/default/files/E11a.jpg?resize=522%2C153 .  
The first line of the text file has to be the mode you want to use  

Text file layout for E11:
1.  E11
2.  Any 3-digit ID
3.  The Group count
4.  The 5-digit groups
Example:  
E11  
635  
3  
45612 58697 19853  

Text file layout for E07:
1.  E07
2.  Any 3-Digit ID
3.  A 3/4-digit group
4.  The group count
5.  The 5-digit groups

Example:  
E07  
945  
728  
5  
45612 58676 19854 98745 63210  
