from mrjob.job import MRJob
from combine_user_visits import csv_readline

"python top_title_words.py anonymous-msweb.data > top_title_words.out"

class TopUsers(MRJob):
    def mapper(self, line_no, line):
        cell = csv_readline(line)
        #If it is a title line
        if cell[0] == 'A':
            #Split line into words
	        for word in cell[3].split():
                #Map 1 to each word
	        	yield [ word.lower(), 1]

    def reducer(self, word, word_counts):
        #Sum word counts for each word
        total = [word, sum(word_counts)]
        #Yeild total.  Export to excel file and find the top 10 words from there.
        yield total

if __name__ == '__main__':
    TopUsers.run()
