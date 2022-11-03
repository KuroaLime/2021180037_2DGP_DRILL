world=[[],[],[]]

def add_object(o, depth):
    world[depth].append(o)

def add_objects(ol,depth):
    world[depth] += ol

def all_objects():
    for layer in world:
        for o in layer:
            yield o #yield된 함수를 호출한 곳이 for문 같은 것이면 generator

def remove_object(o,depth):
    for layer in world:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')
    # world[depth].remove(o) # 단순히 리스트로부터 삭제하는 것
    # del o #메모리까지 삭제

def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()