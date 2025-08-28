def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_case_names = combined_names.lower()

    t = lower_case_names.count("t")
    r = lower_case_names.count("r")
    u = lower_case_names.count("u")
    e = lower_case_names.count("e")

    l = lower_case_names.count("l")
    o = lower_case_names.count("o")
    v = lower_case_names.count("v")
    e = lower_case_names.count("e")

    true_score = t + r + u + e
    love_score = l + o + v + e

    love_score_combined = int(str(true_score) + str(love_score))

    if (love_score_combined < 10) or (love_score_combined > 90):
        print (love_score_combined)
    elif (love_score_combined >= 40) and (love_score_combined <= 50):
        print (love_score_combined)
    else:
        print (love_score_combined)

calculate_love_score("Kanye West", "Kim Kardashian")
