class LFUcache:
    def __init__(self,capacity: int):
        self.capacity=capacity
        self.key_to_val={}
        self.key_to_frq={}
        minfreq=0
        self.frq_to_key=defaultdict(OrderedDict)
        def update(self,key):
            freq=self.key_to_frq[key]
            del self.frq_to_key[freq][key]
            if not self.frq_to_key[freq]:
                del self.frq_to_key[freq]
                if self.minfreq==freq:
                    self.minfreq+=1
            self.key_to_feq[key]=freq+1
            self.frq_to_key[freq+1][key]=None
    def get(self,key: int)->int:
        if key not in self.key_to_val:
            return -1
        self.key_to_val[key]
        self.update(key)
        return self.key_to_val[key]
    def put(self,key: int,value: int)->None:
        if self.capacity==0:
            return
        if key in self.key_to_val:
            self.key_to_val[key]=value
            self.update(key)
            return
        if len(self.key_to_val)>=self.capacity:
            lfu,=self.frq_to_key[self.minfreq].popitem
            del self.key_to_val[lfu]
            del self.key_to_frq[lfu]
        self.key_to_val[key]=value
        self.key_to_frq[key]=1
        self.minfreq=1
        self.frq_to_key[1][key]=None
        return    
                            
