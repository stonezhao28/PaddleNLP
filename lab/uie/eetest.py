from pprint import pprint
from paddlenlp import Taskflow

schema = {'地震触发词': ['地震强度', '时间', '震中位置', '震源深度']} # Define the schema for event extraction
ie = Taskflow('information_extraction', schema=schema)
ie.set_schema(schema)  # Reset schema
pprint(
    ie('中国地震台网正式测定：5月16日06时08分在云南临沧市凤庆县(北纬24.34度，东经99.98度)发生3.5级地震，震源深度10千米。'))


