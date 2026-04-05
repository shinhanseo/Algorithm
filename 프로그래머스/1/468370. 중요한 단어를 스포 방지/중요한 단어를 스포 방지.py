def solution(message, spoiler_ranges):
    words = []   # (word, start, end)
    temp = ""

    # 1. 단어와 각 단어의 시작/끝 인덱스 구하기
    for idx, ch in enumerate(message + " "):
        temp += ch

        if ch == " ":
            word = temp.strip()
            if word:
                start = idx - len(temp) + 1
                end = idx - 1
                words.append((word, start, end))
            temp = ""

    # 2. 스포가 아닌 단어 집합 구하기
    not_spoiler_message = set()

    # 3. 각 클릭 시점에 완전히 공개되는 스포 단어들을 저장
    reveal_at = [[] for _ in range(len(spoiler_ranges))]

    for word, start, end in words:
        overlap_ranges = []

        for i, (s, e) in enumerate(spoiler_ranges):
            # 단어 [start, end] 와 스포구간 [s, e] 가 겹치면
            if not (end < s or e < start):
                overlap_ranges.append(i)

        if not overlap_ranges:
            # 스포가 아닌 단어
            not_spoiler_message.add(word)
        else:
            # 이 단어는 마지막으로 겹치는 스포 구간을 클릭해야 완전히 공개됨
            last_idx = overlap_ranges[-1]
            reveal_at[last_idx].append(word)

    # 4. 클릭 순서대로 중요한 단어 세기
    important_count = 0
    revealed_spoiler_words = set()

    for group in reveal_at:
        for word in group:
            if word in not_spoiler_message:
                continue
            if word in revealed_spoiler_words:
                continue

            important_count += 1
            revealed_spoiler_words.add(word)

    return important_count