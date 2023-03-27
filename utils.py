from .settings import *
from ._helper import *
import re


def search_list(keyword,target):
     respnse  = check_exact_match(keyword,target)
     return respnse

def forword_strip(keyword,target,delim):
        split_target = str(target).lower().split(delim)
        word_match = []
        for i in range(len(split_target)):
            if(i == 0):
                string_target = ' '.join(split_target)
                if(keyword == string_target):
                    word_match.append({
                        'Keyword':keyword,
                        'Target':string_target
                    })
            else:
                x = i-1
                if(x <= len(split_target)-1):
                    split_target.pop(0)
                    string_target = ' '.join(split_target)
                    if(keyword == string_target):
                        word_match.append({
                            'Keyword':keyword,
                            'Target':string_target
                        })
        if(len(word_match) >= 1):
            return make_response(True,Algorithms.FORWARD_SEARCH,keyword,string_target,len(word_match),word_match)
        else:
            return make_response(False,Algorithms.FORWARD_SEARCH,keyword,string_target)


def backword_strp(keyword,target,delim):
        target = str(target).strip()
        split_target = str(target).lower().split(delim)
        keyword = str(keyword).strip()
        word_match = []
        for i in range(len(split_target)):
            if(len(split_target)>=1):
                if(i == 0):
                    string_target = ' '.join(split_target)
                    string_target = str(string_target).strip()
                    # print(string_target,keyword)
                    if(keyword == string_target):
                        word_match.append({
                            'Keyword':keyword,
                            'Target':string_target
                        })
                else:
                    split_target.pop(-1)
                    string_target = ' '.join(split_target)
                    string_target = str(string_target).strip()
                    # print(string_target,keyword)
                    if(keyword == string_target):
                        word_match.append({
                            'Keyword':keyword,
                            'Target':string_target
                        })
        if(len(word_match) >= 1):
            return make_response(True,Algorithms.BACKWARD_SEARCH,keyword,string_target,len(word_match),word_match)
        else:
            return make_response(False,Algorithms.BACKWARD_SEARCH,keyword,target)


def split_search(keyword,target,delim):
    keyword_clubbing = club_line_name(keyword)
    # print("keyword_clubbing",keyword_clubbing)
    target_clubbing = club_line_name(target)
    # print("target_clubbing",target_clubbing)
    keyword = str(keyword).split(delim)
    target = str(target).split(delim)
    respnse = {'status':False}
    if(len(keyword) == 1):
        # print("Keyword Length = 1")
        respnse = check_exact_match(keyword,target)
    elif(len(keyword) == 2):
        # print("Keyword Length = 2")
        if(len(keyword[1]) ==1):
            keyword = ["".join(keyword)]
            respnse  = check_exact_match(keyword,target)
            # print(respnse)
            # print("\n\n=\n")
    elif(len(keyword) >= 3):
        # print("Keyword Length >= 3")
        if(len(keyword[2]) >=3):
            new_keyword = ["".join(keyword)]
            # print(new_keyword)
            respnse  = check_exact_match(new_keyword,target)
            if(respnse['status'] == False):
                respnse  = check_exact_match(keyword,target)
                if(respnse['status'] != False):
                    if(respnse['match_count'] == 1):
                        return make_response(True,Algorithms.SPLIT_SEARCH," ".join(keyword)," ".join(target),respnse['match_count'],respnse['word_match'])
    match_count = 0
    if(respnse['status'] == False):
        word_match = []
        if(keyword_clubbing != False):
            # print("Keyword Clubbing")
            for item in keyword_clubbing:
                new_keyword = [item.strip()]
                # print("Target = ",item)
                # print("Keyword = ",keyword)
                respnse = check_exact_match(new_keyword,target)
                if(respnse['status'] == False and " " in item):
                    new_keyword = [item.replace(" ","").strip()]
                    respnse = check_exact_match(new_keyword,target)
                if(respnse['status'] != False):
                    word_match.append({
                        'Keyword':item,
                        'Target':target
                    })
                    match_count += 1
        # print("match_count",match_count)
        if(match_count == 0 and target_clubbing != False):
            # print("Target Clubbing")
            for item in target_clubbing:
                new_target = [item.strip()]
                # print("Target = ",item)
                # print("Keyword = ",keyword)
                respnse = check_exact_match(keyword,new_target)
                if(respnse['status'] == False):
                    new_target = [item.replace(" ","").strip()]
                    respnse = check_exact_match(keyword,new_target)
                if(respnse['status'] != False):
                    word_match.append({
                        'Keyword':keyword,
                        'Target':new_target
                    })
                    match_count += 1
        if(match_count >= 1):
            # print(match_count)
            return make_response(True,Algorithms.SPLIT_SEARCH," ".join(keyword)," ".join(target),match_count,word_match)
        else:
            # print("Entered")
            return check_exact_match(keyword,target)
    else:
        return respnse
    

def contains_match(keyword,target):
    if(keyword in target):
        word_match = [{
            'Keyword':target,
            'Target':keyword
        }]
        return make_response(True,Algorithms.CONTAINS_MATCH,keyword,target,1,word_match)
    else:
        return make_response(False,Algorithms.CONTAINS_MATCH,keyword,target)