from pprint import pprint
from paddlenlp import Taskflow

schema = ['业务场景','楼层', '房间', '姓名', '时间','血压','心率'] # Define the schema for entity extraction
ie = Taskflow('information_extraction', schema=schema)
pprint(ie("交接班记录，今天看了5楼501床，邹震平老人需要重点护理，二便增加，夜晚加强巡视，右半身行动不便，做早操，推拿按摩，看电视，血压130，血压70，心率60")) # Better print results using pprint
