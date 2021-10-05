from numpy import zeros

class cell:
    def __init__(self, arr, n1, n2):
        self.num    = [arr[i*n1:(i+1)*n1] for i in range(n2)]
