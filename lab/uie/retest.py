from pprint import pprint
from paddlenlp import Taskflow

schema = {'竞赛名称': ['主办方', '承办方', '已举办次数']}  # Define the schema for relation extraction
ie = Taskflow('information_extraction', schema=schema)
ie.set_schema(schema)  # Reset schema
pprint(
    ie('2022语言与智能技术竞赛由中国中文信息学会和中国计算机学会联合主办，百度公司、中国中文信息学会评测工作委员会和中国计算机学会自然语言处理专委会承办，已连续举办4届，成为全球最热门的中文NLP赛事之一。'))


