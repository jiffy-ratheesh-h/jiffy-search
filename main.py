from .settings import *
from .utils import *



class CheckLineName:
    def __init__(self,keyword,target):
     self.keyword = str(keyword).lower()
     self.target = str(target).lower()
    def find_match(self):
        obj = SearchAlgorithms(self.keyword,self.target)
        forward_status = obj.search_forward()
        if(forward_status['status'] == False):
            backward_status = obj.search_backward()
            if(backward_status['status'] == False):
                split_status = obj.search_split()
                return split_status
            else:
                return backward_status
        else:
            return forward_status
    

class SearchAlgorithms:
    def __init__(self,keyword,target):
     self.keyword = str(keyword).lower()
     self.target = str(target).lower()

    def search_forward(self):
        for delim in Config.SPECIAL_CHARACTERS:
            forword_status = forword_strip(self.keyword,self.target,delim)
            if(forword_status['status'] == True):
                return forword_status
        return forword_status
    
    def search_backward(self):
        for delim in Config.SPECIAL_CHARACTERS:
            backword_status = backword_strp(self.keyword,self.target,delim)
            if(backword_status['status'] == True):
                return backword_status
        return backword_status
            
    def search_split(self):
        for delim in Config.SPECIAL_CHARACTERS:
            split_status = split_search(self.keyword,self.target,delim)
            if(split_status['status'] == True):
                return split_status
        return split_status
