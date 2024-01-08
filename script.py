import csvreader
import scrapejournals
import getkeywords

solutions = csvreader.add_data_to_model()

search = getkeywords.getsearch(solutions[11])
scrapejournals.scrapesites(search, "file7")


