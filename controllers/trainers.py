''' Shoes controller '''
from werkzeug.exceptions import BadRequest


def index(req):
    return [t for t in trainers], 200

def show(req, uid):
    return find_by_uid(uid), 200

# def create(req):
#     new_cat = req.get_json()
#     new_cat['id'] = sorted([c['id'] for c in cats])[-1] + 1
#     cats.append(new_cat)
#     return new_cat, 201

# def update(req, uid):
#     cat = find_by_uid(uid)
#     data = req.get_json()
#     print(data)
#     for key, val in data.items():
#         cat[key] = val
#     return cat, 200

# def destroy(req, uid):
#     cat = find_by_uid(uid)
#     cats.remove(cat)
#     return cat, 204

def find_by_uid(uid):
    try:
        return next(shoe for shoe in trainers if shoe['id'] == uid)
    except:
        raise BadRequest(f"We don't have that brand with id {uid}!")