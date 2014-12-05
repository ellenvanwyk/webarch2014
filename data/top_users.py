from mrjob.job import MRJob
from combine_user_visits import csv_readline

'''python top_users.py user-visits_msweb.data > top_users.out'''

class TopUsers(MRJob):
    def mapper(self, line_no, line):
        cell = csv_readline(line)
        yield [ cell[0], 1]


    def reducer(self, user, visit_counts):
        total = [user, sum(visit_counts)]
        if total[1] > 20:
            yield  total

if __name__ == '__main__':
    TopUsers.run()
