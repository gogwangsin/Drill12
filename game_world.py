objects = [[] for _ in range(4)]
# 시각적인 관점에서의 월드


# 충돌관점의 월드 정의 dictionary
collision_pairs = {}  # { 'Boy:Ball' : [[boy],[ball1,ball2...]] }


# fill here

def add_object(o, depth=0):
    objects[depth].append(o)


def add_objects(ol, depth=0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


# fill here
def collide(a, b):  # a물체 b물체
    # left bottom right top
    La, Ba, Ra, Ta = a.get_bb()
    Lb, Bb, Rb, Tb = b.get_bb()

    # b가 중앙 a가 4방면에서 확인
    if La > Rb: return False
    if Ra < Lb: return False
    if Ta < Bb: return False
    if Ba > Tb: return False

    return True


# { 'Boy:Ball' : [ [a],[b] ] }
# 소년이 한번 들어오면 다시 추가할 필요 없는디
def add_collision_pair(group, a, b):
    if group not in collision_pairs:  # 아무것도없으면 빈리스트 생성
        print(f'New Group {group} added.')
        collision_pairs[group] = [[], []]

    if a:  # a가 있을 때, 즉 a가 None이 아니면 추가해주고
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)  # 시각적 월드에서만 삭제한거 objects , collision_pairs은 아직 안없어짐
            remove_collision_object(o) # 충돌 그룹에서 삭제 완료
            del o # 객체 자체를 완전히 메모리에서 제거.
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()


def handle_collisions():
    # 등록된 모든 충돌 상황에 대해서 충돌 검사 및 충돌 처리 수행
    for group, pairs in collision_pairs.items():  # key='str', value [[],[]]
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    # 어떤 그룹과 충돌했는지
                    # 충돌 상대방은 누구인지
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
