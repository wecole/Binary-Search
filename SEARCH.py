
class BinarySearch(list):
    

    def __init__(self, a, b):
        super(BinarySearch, self).__init__()
        self.a=a
        self.b=b
        for i in range(self.a):
            list.append(self, self.b)
            self.b +=b
            i +=1
        self.length=i

    def search(self, hit):
        begin_search = 0
        end_search = self.length - 1
        found=False
        count=0
        is_in_list=False
        try:
            index = self.index(hit)
            is_in_list = True
        except ValueError:
            index = -1
            is_in_list = False

   
        while begin_search <= end_search and not found and is_in_list and hit != self[end_search]:
            centre = (begin_search + end_search)//2
            if centre == hit:
                found = True
                count+=1
                index=centre
            else:
                if hit < centre:
                    end_search = centre - 1
                    count +=1
                else:
                    begin_search = centre + 1
                    count +=1
        return {"count": count, "index": index}