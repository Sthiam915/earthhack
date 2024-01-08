#main script that gets all of the journal information.

import csvreader
import scrapejournals
import getkeywords

#gets all of the solutions from the csv
solutions = csvreader.add_data_to_model()

#converts the solution description into a search argument to find articles about the subject
search = getkeywords.getsearch(solutions[11])

#gathers text from several articles =that support or contradict the validity of the subgject
scrapejournals.scrapesites(search, "file7")

#use an llm in order to decipher the studies' information to see whether current studies support or discredit the idea we have


