#Example of role base authorization
users = [
    {"name": "Roger", "role": "admin"},
    {"name": "David", "role": "customer"},
    {"name": "Sarah", "role": "staff"}
]


alllowed_roles = ["admin" , "staff"]

def can_delete_product(user):
    return user["role"]  in alllowed_roles

for user in users:
    if can_delete_product(user):
        print(f"{user['name']} can delete products.")
    else:
        print(f"{user['name']} cannot delete products")

#Example of ownership base authorization

orders = [
    {"id": 101 , "user_id": 1, "total": 500},
    {"id": 102, "user_id": 2, "total":300}
]

def can_view_orders(user, order):
    return user["id"] == order["user_id"]

roger = {"id": 1, "role": "customer"}
david = {"id": 2, "role": "customer"}

order = {"id": 101, "user_id": 1, "total": 500}

print(can_view_orders(roger , order))
print(can_view_orders(david , order))
        
        