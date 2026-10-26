def average(numbers):
    return sum(numbers) / len(numbers)

def get_user(users, id):
    for u in users:
        if u["id"] == id:
            return u
