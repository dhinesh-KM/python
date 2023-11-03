class result(Exception):
    pass
class l_mark(result):
    def __init__(self):
        super().__init__("you are fail")
    
class h_mark(result):
    def __init__(self):
        super().__init__("you are pass")

class check(result):
    def __init__(self,mark):
        try:
            if mark<40:
                raise l_mark
            else:
                raise h_mark
        except Exception as e:
            print(e)
        
check(45)
        

    