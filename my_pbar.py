import sys

def my_pbar(value, endvalue, bar_length = 20):
    if value % int(endvalue/100) == 0:
        percent = float(value) / endvalue
        complete = '<' + '▮' * int(round(percent * bar_length)-1)
        remain = '▯' * (bar_length - len(complete)) + '>'
        if percent <= 0.33:
            color = 91
            sys.stdout.write(f"\r\033[{color}m Percent: [{complete+remain}] {round(percent*100,2)}%\033[0m")
        elif percent <= 0.66:
            color = 93
            sys.stdout.write(f"\r\033[{color}m Percent: [{complete+remain}] {round(percent*100,2)}%\033[0m")
        elif percent == 1:
            color = 92
            sys.stdout.write(f"\r\033[{color}m Percent: [{complete+remain}] {round(percent*100,2)}%\033[0m")
        else:
            color = 96
            sys.stdout.write(f"\r\033[{color}m Percent: [{complete+remain}] {round(percent*100,2)}%\033[0m")
        sys.stdout.flush()
