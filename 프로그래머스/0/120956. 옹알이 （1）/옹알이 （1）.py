def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        for sound in sounds:
            word = word.replace(sound, " ")

        if word.strip() == "":
            answer += 1

    return answer