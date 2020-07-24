# numberstations
Python script that emulates real numbers stations  
Required libraries:  
- playsound

Usage:  
Launch "main.py <textfile.txt>" in the CLI of your choice.  
You can now check your files for errors before running them through the main.py. Just run "validator.py <textfile.txt>" in your cli! (of course without quotes)  

The stations:  
So far, this script supports E11, E07, E07a and S11a (single message formats; I'm working on more!).  
E07's message format can be viewed here: http://priyom.org/number-stations/english/e07 .  
E07a here: http://priyom.org/number-stations/english/e07a  
and E11 here: https://i0.wp.com/www.numbers-stations.com/sites/default/files/E11a.jpg?resize=522%2C153 .  
The first line of the text file has to be the mode you want to use  


Text file layout for E11 or S11a:
1.  E11 (or S11a)
2.  Any 3-digit ID
3.  The Group count
4.  The 5-digit groups  

Text file layout for E07:
1.  E07
2.  Any 3-Digit ID
3.  A 3/4-digit group
4.  The group count
5.  The 5-digit groups


Text file layout for E07a:
1.  E07a
2.  Any 3-Digit ID
3.  The extra 5-digit group
4.  A 3/4-digit group
5.  The group count
6.  The 5-digit groups
