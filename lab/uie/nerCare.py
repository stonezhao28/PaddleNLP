from pprint import pprint
from paddlenlp import Taskflow

schema = ['楼层', '房间', '姓名', '时间', '护理级别', '身体注意', '夜间注意','活动安排'] # Define the schema for entity extraction
ie = Taskflow('information_extraction', schema=schema)
pprint(ie("今天看了5楼501床，邹震平老人需要重点护理，二便增加，夜晚加强巡视，右半身行动不便，做早操，推拿按摩，看电视")) # Better print results using pprint
