
import inspect
"""
insepectを使用したオブジェクトからメソッドだけを取り出す関数
"""
def get_only_method(obj):
    members = inspect.getmembers(obj)
    for obj_li in members:
        for obj_name,obj_contents in zip([obj_li[0]],[obj_li[1]]):
            if inspect.ismethod(obj_contents):
                print(obj_name)