#!/usr/bin/env python
""" mpg.py - Read gas purchase records from a file, then compute average gas mileage and other statistics.

Usage: python mpg.py <optional command line parameter>

Command line parameter:

  -h             Print help message (this docstring), exit.

There is one required input file, which must be in the current working directory. The default file
name is gas_purchases.txt, but this can be changed by modifying a program constant. This file can
contain comment lines and gas purchase lines. Comment lines start with a # character (can have
leading spaces) and are completely ignored by the program. Gas purchase lines each contain the
information for one gas purchase per line, in a comma-delimited format. There can be spaces after
the commas. Strings must not be quoted, and can not contain commas. The format is as follows:

date, location, gallons, price per gallon, cost of purchase, odometer mileage<, optional comments>

Where:

date must be formatted MM/DD/YYYY, purchase lines in file should be in order of increasing date
location is an unquoted string without embedded commas (max 23 chars, see constant in code)
gallons is a floating point number with up to three decimal places (max = 40, can be changed)
price per gallon is a floating point number with up to three decimal places (max = 5.00)
cost of purchase is a floating point number with two decimal places
odometer mileage is an integer
optional comments is an unquoted string without embedded commas, and is optional (max 25 chars)

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

The program produces one output file in the current working directory, and displays the identical
information on the console. The default file name is mpg_results.txt, but this can be changed by
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

Input file:   C:\\Users\\John\\Projects\\mpg\\gas_purchases.txt
Output file:  C:\\Users\\John\\Projects\\mpg\\mpg_results.txt

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

License:

The MIT License (MIT) - Copyright (c) 2018 John Santic
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: John Santic, email johnsantic  <at>  g m a i l  <dot>  c o m

Toolset: Anaconda3 python version 3.4.3, standard library, no other packages, running on Windows 7.

Revision history:
    03-Jun-2018 - create original
"""

import sys
from datetime import date, datetime
from os.path import isfile, abspath

# Define some default file names for Windows, change them if it suits you.
DEFAULT_INPUT_FILE = "gas_purchases.txt"
DEFAULT_OUTPUT_FILE = "mpg_results.txt"

# Define some limits for sanity checking gas purchases.
MIN_GALLONS = 0.1
MAX_GALLONS = 40.0
MIN_PRICE = 0.75
MAX_PRICE = 5.00
MAX_COST_ERROR = 0.05  # when we check cost = gallons x price arithmetic

# Max. characters printed in output information, input file chars can be more.
MAX_NAME_LEN = 23     # max chars in name/location field
MAX_COMMENT_LEN = 25  # max chars in optional comment field

# If you don't fill the tank completely, a particular computed MPG can seem unreasonable (but so be 
# it, display it anyway). Use these min/max to ignore those MPGs when printing best/worst MPGs.
MIN_MPG = 15
MAX_MPG = 40

# Lists to save the various parameters from each gas purchase record.
dates = []     # date of purchase (stored here as datetime object)
names = []     # gas station name/location (string)
gallons = []   # total gallons (float)
prices = []    # price per gallon (float)
costs = []     # total cost of purchase (float)
mileages = []  # odometer reading at time of purchase (integer)
comments = []  # optional comments (string)
mpg = []       # this is computed, it's not from the input file (float)

# Start of main program processing.

# If -h command-line option entered, display help message (the module documentation string at top of
# this file) and exit. If anything else on command line, bail out due to error.
if (len(sys.argv) == 2) and (sys.argv[1] == "-h"):
    print(__doc__)
    sys.exit(0)
if len(sys.argv) != 1:
    sys.exit("Error, invalid command line parameters, for help, enter mpg -h")

# Make sure input file exists in current directory; if not, exit in error.
if not isfile(DEFAULT_INPUT_FILE):
    sys.exit("Error, input file not found: " + DEFAULT_INPUT_FILE)

# Read all gas purchase records of input file and do basic error checking, then save the purchase
# parameters in the set of lists for later processing.
try:
    with open(DEFAULT_INPUT_FILE, 'rt') as input_file:
        list_idx = 0
        for line_nbr, line in enumerate(input_file, 1):  # start counting lines with 1
        
            # Any line that starts with # is a comment line, skip it.
            if line.lstrip()[0] == "#":
                continue
                
            # Extract all fields of comma-delimited record, new_comment is variable length because
            # it is optional and might not be present.
            new_date, new_name, new_gallon, new_price, new_cost, new_mileage, *new_comment =  \
                line.split(',')
            
            # Date field must be valid MM/DD/YYYY and in chronological order within file.
            dates.append(datetime.strptime(new_date.strip(), '%m/%d/%Y'))  # save as datetime object
            if list_idx > 0:
                if dates[list_idx] < dates[list_idx-1]:
                    sys.exit("Error, dates out of sequence: Line " + str(line_nbr))

            # Gas station name/location, anything goes, save the string (truncate if too long).
            names.append(new_name.strip()[:MAX_NAME_LEN])
            
            # Gallons purchased, sanity check the value.
            gallons.append(float(new_gallon))
            if not (MIN_GALLONS <= gallons[list_idx] <= MAX_GALLONS):
                sys.exit("Error, gallons out of range: Line " + str(line_nbr))
            
            # Price per gallon, sanity check the value.
            prices.append(float(new_price))
            if not (MIN_PRICE <= prices[list_idx] <= MAX_PRICE):
                sys.exit("Error, price per gallon out of range: Line " + str(line_nbr))
            
            # Cost of purchase, check the receipt arithmetic to catch typos in input file.
            costs.append(float(new_cost))
            if abs((gallons[list_idx] * prices[list_idx]) - costs[list_idx]) > MAX_COST_ERROR:
                sys.exit("Error, cost doesn't equal gallons x price: Line " + str(line_nbr))

            # Mileage (odometer reading), must be integer in numerically increasing order in file.
            mileages.append(int(new_mileage))
            if list_idx > 0:
                if mileages[list_idx] < mileages[list_idx-1]:
                    sys.exit("Error, mileages out of sequence: Line " + str(line_nbr))
             
            # Comments (if any) are ignored by the program. Note that new_comments is extracted as
            # a variable length list, which could be empty if no comment on this record.
            if not (new_comment):
                my_comment = ' '                    # if MT, make it a space, easier later on
            else:                                   # else, extract actual comment string from list
                my_comment = new_comment[0].strip()[:MAX_COMMENT_LEN]  # truncate string if too long
            comments.append(my_comment)
            
            # Count how many gas purchases, as opposed to using line numbers, which can be greater
            # due to comment lines in file.
            list_idx += 1
            
        # End of enumerate loop, loops once per gas purchase line in input file.
        
    # End of "with" block, input file now automatically closed.

# Execution skips the "except" clause if there were no errors in the above "try" code.
# All errors are fatal, bail out with program and system error messages.
except Exception as err_msg:
    print(err_msg)
    sys.exit("Error processing input file: Line " + str(line_nbr))

# There must be at least two gas purchase records to compute MPG. If not, bail out in error.
if list_idx < 2:
    sys.exit("Error, must be at least two gas purchases to compute MPG.")
    
# So far, so good, input file looks good, we have extracted and saved all the parameters.

# First gas purchase record is special - since there is no previous purchase, you can't
# compute MPG for this purchase, but initialize a bunch of statistics variables.
prev_mileage = mileages[0]  # used to compute miles per tankful
min_gallons   = gallons[0]  # used to track min/max
max_gallons   = gallons[0]
min_gal_idx   = 0           # what purchase number was min/max
max_gal_idx   = 0
total_gallons = gallons[0]  # total gallons purchased in entire file, including first purchase
min_price     = prices[0]
max_price     = prices[0]
min_price_idx = 0
max_price_idx = 0
min_cost      = costs[0]
max_cost      = costs[0]
min_cost_idx  = 0
max_cost_idx  = 0
total_cost    = costs[0]  # used to compute average cost/gal for entire file, including first purchase
mpg.append(0)      # no computed MPG for the first record
mpg_gallons   = 0  # running total of gallons for MPG computation, omits first gallon value
mpg_mileage   = 0  # running total of mileage for MPG computation, omits first mileage value

# Loop through remaining gas purchase records, accumulating all statistics as we go.
idx = 1  # skip first record, already processed above
while idx < list_idx:

    if gallons[idx] > max_gallons: max_gallons = gallons[idx]; max_gal_idx = idx
    if gallons[idx] < min_gallons: min_gallons = gallons[idx]; min_gal_idx = idx
    total_gallons += gallons[idx]
    
    if prices[idx] > max_price: max_price = prices[idx]; max_price_idx = idx
    if prices[idx] < min_price: min_price = prices[idx]; min_price_idx = idx
    
    if costs[idx] > max_cost: max_cost = costs[idx]; max_cost_idx = idx
    if costs[idx] < min_cost: min_cost = costs[idx]; min_cost_idx = idx
    total_cost += costs[idx]
    
    miles_this_tankful = mileages[idx] -  prev_mileage
    mpg.append(miles_this_tankful / gallons[idx])
    mpg_gallons += gallons[idx]
    mpg_mileage += miles_this_tankful
    prev_mileage = mileages[idx]
    
    idx += 1
# End of while loop.

# After computing the detailed statistics, create the output file, overwriting any old data.
try:
    with open(DEFAULT_OUTPUT_FILE, 'wt') as output_file:

        # Print a program header with today's date plus the file paths that were used.
        print("\nGas Mileage Statistics as of {0}\n".format(datetime.strftime(date.today(), '%m/%d/%Y')),
            file=output_file)
        print("Input file:  ", abspath(DEFAULT_INPUT_FILE), file=output_file)
        print("Output file: ", abspath(DEFAULT_OUTPUT_FILE), "\n", file=output_file)
        
        # Print a header to identify the various columns of information.
        print(" Nbr    Date      Location                 Gals. Price/Gal.  Cost  Mileage  MPG   Comments",
            file=output_file)
        print("----  ----------  ----------------------- ------   -----    ------ ------  -----  --------------------",
            file=output_file)
        
        # Loop through the gas purchase records, printing each record's information to output file.
        idx = 0
        while idx < list_idx:
            print("{0:>4d}".format(idx+1), datetime.strftime(dates[idx], ' %m/%d/%Y '),
                ("{0:<"+str(MAX_NAME_LEN)+"}").format(names[idx]), "{0:>6.3f}".format(gallons[idx]),
                "  {0:>5.3f}".format(prices[idx]), "   {0:>6.2f}".format(costs[idx]),
                "{0:>6d}".format(mileages[idx]), " {0:>5.2f}".format(mpg[idx]),
                (" {0:<"+str(MAX_COMMENT_LEN)+"}").format(comments[idx]), file=output_file)
            idx += 1
        # End of while loop.
        
        # Print a bunch of interesting overall statistics to the output file.
        print("\nOverall MPG = {0} miles / {1:.3f} gallons = {2:.2f} MPG".format(
            mpg_mileage, mpg_gallons, mpg_mileage/mpg_gallons), file=output_file)

        # Print the ten best and worst MPG values, skip values that appear unreasonable (which can
        # happen if you didn't fill the tank when making a purchase).
        mpg.sort(reverse=True)
        print("\nTen best MPGs:  ", end='', file=output_file)
        count = 0
        for value in mpg:
            if value > MAX_MPG: continue
            print("{0:.2f}".format(value), " ", end='', file=output_file)
            count += 1
            if count >= 10: break
        mpg.reverse()
        print("\n\nTen worst MPGs: ", end='', file=output_file)
        count = 0
        for value in mpg:
            if value < MIN_MPG: continue
            print("{0:.2f}".format(value), " ", end='', file=output_file)
            count += 1
            if count >= 10: break
        
        # Print more interesting statistics.
        print("\n\nGallons per purchase:  Min = {0:.3f} (Nbr {1}),  Max = {2:.3f} (Nbr {3}),  Avg = {4:.3f}".format(
            min_gallons, min_gal_idx+1, max_gallons, max_gal_idx+1, total_gallons/list_idx),
            file=output_file)
        print("\nPrice per gallon:  Min = {0:.3f} (Nbr {1}),  Max = {2:.3f} (Nbr {3}),  Avg = {4:.3f}".format(
            min_price, min_price_idx+1, max_price, max_price_idx+1, total_cost/total_gallons),
            file=output_file)
        print("\nCost per purchase:  Min = ${0:.2f} (Nbr {1}),  Max = ${2:.2f} (Nbr {3}),  Avg = ${4:.2f}".format(
            min_cost, min_cost_idx+1, max_cost, max_cost_idx+1, total_cost/list_idx),
            file=output_file)
        print("\nTotal gallons = {0:.3f}, total cost = ${1:.2f}, gas cost per mile = ${2:.3f}".format(   
            total_gallons, total_cost, (total_cost - costs[0]) / mpg_mileage), file=output_file)
            
    # End of "with" block, output file now automatically closed.
    
# Execution skips the "except" clause if there were no errors in the above "try" code.
# All errors are fatal, bail out with program and system error messages.
except Exception as err_msg:
    print(err_msg)
    sys.exit("Error producing output file: Index " + str(idx+1))
    
# Now reopen the output file for read access and display all of it on the console.
with open(DEFAULT_OUTPUT_FILE, 'rt') as f:
    for line in f:
        print(line, end='')  # avoid double line-feeds
        
# Wait for user to hit Enter key before exiting (and closing command prompt window in Windows).
input("\nPress Enter key to exit")

# If we get here, everything was successfully completed, exit error-free.
sys.exit(0)
