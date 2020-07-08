# Combos2RanksLeaders

## Problem

For each and every pair of WCA events, who is the "best"?

## Solution

I determined the best person/people to be the one(s) with the lowest sum of world ranks of each pair of events. I combined RanksAverage.tsv file with 333mbf data from the RanksSingle.tsv file. Each list of ranks is crossed with another list of ranks, and the lowest sum of both ranks is calculated. The row(s) corresponding to this is added to a master table containing the final results.

After this, I converted the raw "bests" into standard format by creating and using a result converter function.

Finally, the final dataframe is output into a csv file
