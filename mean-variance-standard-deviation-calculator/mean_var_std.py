import numpy as np

def calculate(list):
    if len(list) < 9 :
      raise ValueError("List must contain nine numbers.")
    else :  
      calculations = {}
      a = np.array(list)
           
      mean= []
      variance = []
      standard_deviation = []
      _max = []
      _min = []
      _sum = []

      for i in range(2) :
        mean.append(a.reshape((3,3)).mean(axis=i).tolist())
        variance.append(a.reshape((3,3)).var(axis=i).tolist())
        standard_deviation.append(a.reshape(3,3).std(axis=i).tolist())
        _max.append(a.reshape((3,3)).max(axis=i).tolist())
        _min.append(a.reshape((3,3)).min(axis=i).tolist())
        _sum.append(a.reshape((3,3)).sum(axis=i).tolist())
              
      standard_deviation.append(a.std().tolist())  
      mean.append(a.mean().tolist())
      variance.append(a.var().tolist())
      _max.append(a.max().tolist())
      _min.append(a.min().tolist())
      _sum.append(a.sum().tolist())

      calculations['mean']=mean
      calculations['variance'] = variance
      calculations['standard deviation'] = standard_deviation
      calculations['max'] = _max
      calculations['min'] = _min
      calculations['max'] = _max
      calculations['sum'] = _sum
      
    
      return calculations