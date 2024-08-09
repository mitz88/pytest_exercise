


# lists exercise t create list from star notation


marks = [4,5] * 4

print(marks)


# creating list from the range function

balls = list(range(1,8))
print(balls)

odd_balls1 = balls[::]
odd_balls2 = balls[0::]
odd_balls2_1 = balls[2::]
odd_balls3 = balls[:4:]
odd_balls4 = balls[::1]
odd_balls5 = balls[::-1]
print(f"\nodd_balls1 = {odd_balls1}\
        \nodd_balls2 = {odd_balls2}\
        \nodd_balls2_1 = {odd_balls2_1}\
        \nodd_balls3 = {odd_balls3} \
        \nodd_balls4 = {odd_balls4}\
        \nodd_balls5 = {odd_balls5}")