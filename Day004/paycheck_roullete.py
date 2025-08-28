import random
import secrets

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#result = random.choice(friends)
#result_index = random.randint(0, len(friends) -1)
result = secrets.choice(friends)
print(result)

