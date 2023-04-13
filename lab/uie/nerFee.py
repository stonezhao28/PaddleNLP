from pprint import pprint
from paddlenlp import Taskflow

schema = ['出发地', '目的地', '费用', '时间'] # Define the schema for entity extraction
ie = Taskflow('information_extraction', schema=schema)
pprint(ie("深大到双龙28块钱4月24号交通费")) # Better print results using pprint
