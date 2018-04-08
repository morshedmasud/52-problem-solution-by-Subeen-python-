# Taking value of 't' for test case
t = int(input())
x = 0
while x < t:
    # Taking values of 'r1' for oppsite team run, 'r2' your team run , 'b' current less ball.
    r1, r2, b = map(int, input().split())
    # Finding less ball
    ball_played = 300 - b
    # Find current_run_rate
    current_run_rate = (r2 / ball_played) * 6
    # Find ask_run_rate
    ask_run_rate = ((r1 - r2 + 1) / b) * 6
    print("%.2f %.2f \n" %(current_run_rate, ask_run_rate))
    x += 1
