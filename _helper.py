from .settings import *




def check_exact_match(keyword,target):
    match_count = 0
    word_match = []
    # print(keyword)
    # print(target)
    for word in keyword:
        for placement in target:
            if(len(word)>=2 and len(placement) >=2):
                if(word == placement):
                    # print("Word = ",word)
                    # print("Placement = ",placement)
                    word_match.append({
                        'Keyword':keyword,
                        'Target':placement
                    })
                    match_count +=1
    if(match_count >= 1):
        # print(match_count)
        return make_response(True,Algorithms.SPLIT_SEARCH," ".join(keyword)," ".join(target),match_count,word_match)
    else:
        return make_response(False,Algorithms.SPLIT_SEARCH," ".join(keyword)," ".join(target),match_count,word_match)

def club_line_name(line_name):
    line_name_split = str(line_name).split(" ")
    new_line_split = []
    for i in range(len(line_name_split)-1):
        if(len(line_name_split[i]) == 1):
            try:
                word = line_name_split[i-1] +line_name_split[i] + line_name_split[i+1]
                new_line_split.append(word)
            except:
                pass
        if(len(line_name_split[i]) >= 3 and len(line_name_split[i+1])>=1):
            word = line_name_split[i] +line_name_split[i+1]
            new_line_split.append(word)
        else:
            word = line_name_split[i]+" " +line_name_split[i+1]
            new_line_split.append(word)
    if(len(new_line_split)>=1):
        return new_line_split
    else:
        return False
    
def check_line_name(keyword):
    for i in range(len(keyword)-1):
        if(len(keyword[i]) >= 3 and len(keyword[i+1]) == 1):
            return [keyword[i] + keyword[i:]]
    return keyword