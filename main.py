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
     self.keyword = str(keyword)
     self.target = str(target)

    def search_forward(self):
        new_keyword = self.keyword.lower()
        new_target = self.target.lower()
        for delim in Config.SPECIAL_CHARACTERS:
            forword_status = forword_strip(new_keyword,new_target,delim)
            if(forword_status['status'] == True):
                return forword_status
        return forword_status
    
    def search_backward(self):
        new_keyword = self.keyword.lower()
        new_target = self.target.lower()
        for delim in Config.SPECIAL_CHARACTERS:
            backword_status = backword_strp(new_keyword,new_target,delim)
            if(backword_status['status'] == True):
                return backword_status
        return backword_status
            
    def search_split(self):
        new_keyword = self.keyword.lower()
        new_target = self.target.lower()
        for delim in Config.SPECIAL_CHARACTERS:
            split_status = split_search(new_keyword,new_target,delim)
            if(split_status['status'] == True):
                return split_status
        return split_status

    def search_contains(self):
        new_keyword = self.keyword.lower()
        new_target = self.target.lower()
        contains_status = contains_match(new_keyword,new_target)
        return contains_status


