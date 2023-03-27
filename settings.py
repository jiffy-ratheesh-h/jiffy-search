import os


class Config:
    SPECIAL_CHARACTERS = [" "]
    SPLIT_DELIMITTER = [","]
    SPLIT_CHARACTERS = ["`",'~','|','@','#','$','%','&','^','*','(',')','_','-',',','-'," "]

class Algorithms:
    SPLIT_SEARCH = "Split Search"
    FORWARD_SEARCH = "Forward Search"
    BACKWARD_SEARCH = "Backward Search"
    ABORTED = "Aborted Search"
    CONTAINS_MATCH = "Contains Match"
    EXACT_MATCH = "Exact Match"

def make_response(status,algorithm,keyword,target,match_count=0,word_match=None):
    return {
        'status':status,
        'algorithm':algorithm,
        'keyword':keyword,
        'target':target,
        'match_count':match_count,
        'word_match':word_match
    }