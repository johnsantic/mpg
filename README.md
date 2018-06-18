# mpg.py


mpy.py is a python program that reads gas purchase records from a file, then computes average gas
mileage and other statistics.


## Usage

How to run mpg:

    python mpg.py <optional command-line parameter>

Command-line parameter:

    python mpg.py -h

Display a help message, which is the mpg.py module docstring.

## Input file

There is one required input file, which must be in the current working directory. The default file
name is *gas_purchases.txt*, but this can be changed by modifying a program constant. This file can
contain comment lines and gas purchase lines. Comment lines start with a `#` character (can have
leading spaces) and are completely ignored by the program. Gas purchase lines each contain the
information for one gas purchase per line, in a comma-delimited format. There can be spaces after
the commas. Strings must not be quoted, and can not contain commas. The format is as follows:

    date, location, gallons, price per gallon, cost of purchase, odometer mileage<, optional comments>

Where:

* `date` must be formatted MM/DD/YYYY, purchase lines in file should be in order of increasing date
* `location` is an unquoted string without embedded commas (max 23 chars, see constant in code)
* `gallons` is a floating point number with up to three decimal places (max = 40.0, can be changed)
* `price per gallon` is a floating point number with up to three decimal places (max = 5.00)
* `cost of purchase` is a floating point number with two decimal places
* `odometer mileage` is an integer
* `optional comments` is an unquoted string without embedded commas, and is optional (max 25 chars)

Example input file:

    # Transit Connect gas purchases, for MPG calculation
    #
    08/06/2016, Costco Cville, 8.788, 1.669, 14.67, 246
    08/16/2016, Costco Cville, 9.904, 1.699, 16.83, 506
    08/22/2016, Costco Cville, 12.853, 1.729, 22.22, 858
    08/28/2016, Wawa Fburg, 10.050, 1.959, 19.69, 1135, traveling to DC
    09/06/2016, Costco Cville, 7.142, 1.849, 13.21, 1335
    09/11/2016, Costco Cville, 11.178, 1.789, 20.00, 1645
    09/17/2016, Wawa Fburg, 9.820, 1.999, 19.63, 1899, returning from DC
    09/30/2016, Costco Cville, 9.076, 1.909, 17.33, 2140
    10/10/2016, Costco Cville, 11.128, 1.939, 21.58, 2469
    10/19/2016, Costco Cville, 10.993, 1.889, 20.77, 2789
    11/04/2016, Costco Cville, 10.798, 1.839, 19.86, 3084
    11/19/2016, Costco Cville, 12.229, 1.769, 21.63, 3431, almost out of gas
    11/27/2016, Wawa Gainsville, 6.094, 1.969, 12.00, 3588

## Output file

The program produces one output file in the current working directory, and displays the identical
information on the console. The default file name is *mpg_results.txt*, but this can be changed by
modifying a program constant. The file is overwritten if it already exists.

The program displays one line per gas purchase, listing the information from the input file as well 
as a computed MPG per line. At the end, the program displays the overall MPG/gallons/miles, then the
ten best and worst MPGs. For best/worse, the program ignores unreasonable MPG values, which can happen
if you don't fill the tank when making a purchase. The program then displays min/max/avg information
for gallons, price per gallon, cost of purchase, etc. Note that the total miles and gallons for MPG 
computation is different than the total miles and gallons for the entire file (the program displays 
both). This is because the gallons/miles for the first gas purchase in the file are NOT included in 
the overall MPG calculation, but are included in the totals for the file.

Example output file:

    Gas Mileage Statistics as of 06/14/2018
    
    Input file:   C:\Users\John\Projects\mpg\gas_purchases.txt
    Output file:  C:\Users\John\Projects\mpg\mpg_results.txt
    
     Nbr    Date      Location                 Gals. Price/Gal.  Cost  Mileage  MPG   Comments
    ----  ----------  ----------------------- ------   -----    ------ ------  -----  --------------------
       1  08/06/2016  Costco Cville            8.788   1.669     14.67    246   0.00
       2  08/16/2016  Costco Cville            9.904   1.699     16.83    506  26.25
       3  08/22/2016  Costco Cville           12.853   1.729     22.22    858  27.39
       4  08/28/2016  Wawa Fburg              10.050   1.959     19.69   1135  27.56  traveling to DC
       5  09/06/2016  Costco Cville            7.142   1.849     13.21   1335  28.00
       6  09/11/2016  Costco Cville           11.178   1.789     20.00   1645  27.73
       7  09/17/2016  Wawa Fburg               9.820   1.999     19.63   1899  25.87  returning from DC
       8  09/30/2016  Costco Cville            9.076   1.909     17.33   2140  26.55
       9  10/10/2016  Costco Cville           11.128   1.939     21.58   2469  29.57
      10  10/19/2016  Costco Cville           10.993   1.889     20.77   2789  29.11
      11  11/04/2016  Costco Cville           10.798   1.839     19.86   3084  27.32
      12  11/19/2016  Costco Cville           12.229   1.769     21.63   3431  28.38  almost out of gas
      13  11/27/2016  Wawa Gainsville          6.094   1.969     12.00   3588  25.76
    
    Overall MPG = 3342 miles / 121.265 gallons = 27.56 MPG
    
    Ten best MPGs:  29.57  29.11  28.38  28.00  27.73  27.56  27.39  27.32  26.55  26.25
    
    Ten worst MPGs: 25.76  25.87  26.25  26.55  27.32  27.39  27.56  27.73  28.00  28.38
    
    Gallons per purchase:  Min = 6.094 (Nbr 13),  Max = 12.853 (Nbr 3),  Avg = 10.004
    
    Price per gallon:  Min = 1.669 (Nbr 1),  Max = 1.999 (Nbr 7),  Avg = 1.841
    
    Cost per purchase:  Min = $12.00 (Nbr 13),  Max = $22.22 (Nbr 3),  Avg = $18.42
    
    Total gallons = 130.053, total cost = $239.42, gas cost per mile = $0.067
    
    Press Enter key to exit


## Development toolset

* Anaconda3 Python version 3.4.3, standard library, no other packages.
* Edited with notepad++.
* All running on Windows 7. 

## Installation

The entire program consists of a single file, *mpg.py*. There is no formal installation
procedure, merely copy the file from the repository to your local hard drive.

## License

The MIT License (MIT) - Copyright (c) 2018 John Santic

Permission is hereby granted, free of
charge, to any person obtaining a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so, subject to the
following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

The Software is provided "as is", without warranty of any kind, express or implied, including
but not limited to the warranties of merchantability, fitness for a particular purpose and
noninfringement. In no event shall the authors or copyright holders be liable for any claim,
damages or other liability, whether in an action of contract, tort or otherwise, arising from,
out of or in connection with the Software or the use or other dealings in the Software.

## Author

John Santic, email johnsantic  <at\>  g m a i l  <dot\>  c o m

## Revision history

03-Jun-2018 - create original
