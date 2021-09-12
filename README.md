# Election_Analysis

## Project Overview
Using a provided source file that contains election results the purpose of this project is to do the following:

1. Calculate the total number of votes cast.
2. Determine vote count by county and percent of total vote in each county
3. Determine county with largest turn out 
4. Get a complete list of candidates who received votes
5. Calcualte the total votes for each candidate name.
6. Calculate the percent of the total vote each candidate received
7. Determine the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv  
- Software:  Python 3.7.6, Visual Studio Code 1.59.1  

## Election Audit Results
The analysis of the election show that:  
- There were 369,711 votes cast
- Percent of total votes and vote count by county
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- Largest County turn out
  - Denver: 82.8% (306,055)
- The candidates were  
  - Charles Casper Stockham  
  - Diana Degette  
  - Raymon Anthony Doane  
- The cadidate results were  
  - Charles Casper Stockham: 23.0% (85,213)  
  - Diana DeGette: 73.8% (272,892)  
  - Raymon Anthony Doane: 3.1% (11,606)  
- The winner of the election was:  
  - Diana Degette, who received 73.8% of the vote and 272,892 votes

## Eelction Audit Summary
This script would be easy to adapt for use in other elections.  I would recommend adding a section of code that would take user input
to request file names for both the input csv and the output txt files.  We could also add a section that could summarize cannidate results
by county to provide additional information about the election to the user.
