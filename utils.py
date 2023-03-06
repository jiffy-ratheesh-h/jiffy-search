from .settings import *

def forword_strip(keyword,target,delim):
        split_target = str(target).lower().split(delim)
        for i in range(len(split_target)):
            if(i == 0):
                string_target = ' '.join(split_target)
                if(keyword == string_target):
                    return make_response(True,Algorithms.FORWARD_SEARCH,keyword,string_target)
            else:
                x = i-1
                if(x <= len(split_target)-1):
                    split_target.pop(0)
                    string_target = ' '.join(split_target)
                    if(keyword == string_target):
                        return make_response(True,Algorithms.FORWARD_SEARCH,keyword,string_target)
        return make_response(False,Algorithms.FORWARD_SEARCH,keyword,string_target)


def backword_strp(keyword,target,delim):
        target = str(target).strip()
        split_target = str(target).lower().split(delim)
        keyword = str(keyword).strip()
        for i in range(len(split_target)):
            if(len(split_target)>=1):
                if(i == 0):
                    string_target = ' '.join(split_target)
                    string_target = str(string_target).strip()
                    # print(string_target,keyword)
                    if(keyword == string_target):
                        return make_response(True,Algorithms.BACKWARD_SEARCH,keyword,string_target)
                else:
                    split_target.pop(-1)
                    string_target = ' '.join(split_target)
                    string_target = str(string_target).strip()
                    # print(string_target,keyword)
                    if(keyword == string_target):
                        return make_response(True,Algorithms.BACKWARD_SEARCH,keyword,string_target)
        return make_response(False,Algorithms.BACKWARD_SEARCH,keyword,target)

def split_search(keyword,target,delim):
        word_match = []
        split_target = str(target).lower().split(delim)
        for i in range(0,len(Config.SPECIAL_CHARACTERS)):
            match_count = 0
            delim1=Config.SPECIAL_CHARACTERS[i]
            split_keyword = str(keyword).lower().split(delim1)
            for j in range(0,len(split_target)):
                try:
                    if(len(split_target[j+1]) == 1):
                        word = str(split_target[j])+str(split_target[j+1])
                        if(str(word).strip() in split_keyword):
                            # print(word, split_keyword)
                            word_match.append({
                                'keyword':split_keyword,
                                'target':word
                            })
                            match_count += 1
                    else:
                        if(split_target[j].strip() in split_keyword and len(split_keyword)==1):
                            # print("Single")
                            # print(split_target[j], split_keyword)
                            word_match.append({
                                'keyword':split_keyword,
                                'target':split_target[j].strip()
                            })
                            match_count += 1
                        elif(split_target[j].strip() in split_keyword and len(split_target[j])>=3):
                            # print(split_target[j], split_keyword)
                            word_match.append({
                                'keyword':split_keyword,
                                'target':split_target[j].strip()
                            })
                            match_count += 1
                except Exception as e:
                    if(split_target[j].strip() in split_keyword and len(split_keyword)==1):
                        # print(split_target[j], split_keyword)
                        word_match.append({
                                'keyword':split_keyword,
                                'target':split_target[j].strip()
                            })
                        match_count += 1
                    if(split_target[j].strip() in split_keyword and len(split_target[j])>=3):
                        # print(split_target[j], split_keyword)
                        word_match.append({
                                'keyword':split_keyword,
                                'target':split_target[j].strip()
                            })
                        match_count += 1
            keyword = str(keyword).rstrip(',')
        for item in Config.SPLIT_DELIMITTER:
            if(item in keyword):
                new_keyword = str(keyword).lower().split(item)
                for word in new_keyword:
                    if(word in str(target).lower()):
                        # print(word, target)
                        word_match.append({
                                'keyword':word,
                                'target':target
                            })
                        match_count += 1
        
        if(match_count >= 1):
            return make_response(True,Algorithms.SPLIT_SEARCH,keyword,target,match_count,word_match)
        return make_response(False,Algorithms.SPLIT_SEARCH,keyword,target)