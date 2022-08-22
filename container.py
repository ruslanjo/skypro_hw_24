from utils import FileHandler, LogQuery
from config import DATA_DIR

file_handler = FileHandler(DATA_DIR)
log_query = LogQuery()


print(type(log_query.regex))
# data = file_handler.read_file('apache_logs.txt')
#
# data = log_query.regex(data, "POST")
# data = log_query.map(data, 0)
# data = log_query.unique(data)
# data = log_query.sort(data, "desc")
# print(data)

# data = filter(lambda log: "POST" in log, data)
# print(data)
