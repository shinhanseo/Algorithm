def solution(video_len, pos, op_start, op_end, commands):
    def time_to_sec(t):
        m, s = map(int, t.split(':'))
        return m * 60 + s

    def sec_to_time(total):
        m = total // 60
        s = total % 60
        return f"{m:02}:{s:02}"

    pos_sec = time_to_sec(pos)
    max_sec = time_to_sec(video_len)
    op_start_sec = time_to_sec(op_start)
    op_end_sec = time_to_sec(op_end)

    for cmd in commands:
        # 오프닝 스킵
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

        if cmd == "next":
            pos_sec += 10
            if pos_sec > max_sec:
                pos_sec = max_sec
        else:
            pos_sec -= 10
            if pos_sec < 0:
                pos_sec = 0

        # 다시 오프닝 스킵 검사
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return sec_to_time(pos_sec)
