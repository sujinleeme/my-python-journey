s = """Sun 10:00-20:00
Fri 05:00-10:00
Fri 16:30-23:50
Sat 10:00-00:00
Sun 01:00-04:00
Sat 02:00-06:00
Tue 03:30-18:15
Tue 19:00-20:00
Wed 04:25-15:14
Wed 15:14-22:40
Thu 00:00-23:59
Mon 05:00-13:00
Mon 15:00-21:00"""

def convert_date_string(str):
    time_str = [(int(x.split(":")[0]), int(x.split(":")[1])) for x in str.split('-')]
    return time_str

def main():
    result = 1330
    seg = [[x.split()[0],
        convert_date_string(x.split()[1])
    ] for x in s.splitlines()]

    day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # sorting array by day and starting time
    seg = sorted(seg, key=lambda x: (day.index(x[0]), x[1][0][0]))

    for i, meeting_time in enumerate(seg):
        
        start = meeting_time[1][0]
        end = meeting_time[1][1]
        
        start_h = start[0]
        start_m = start[1]
        end_h = end[0]
        end_m = end[1]

        if end_h == 0:
            end_h = 24
            
        if start_m > end_m:
            end_m += 60
            end_h -= 1

        diff_h = end_h - start_h
        minutes_diff = (diff_h * 60) + (end_m - start_m)
        
        if minutes_diff <= result:
            print("{} meeting takes {} minutes.".format(meeting_time[0], minutes_diff))

main()