import numpy as np

def calculate(list):
 if len(list) != 9:
  raise ValueError("List must contain nine numbers.")
 else:
  array=np.asarray(list).reshape(3,3)
  mean_axis1=[np.mean(array[:,0]),np.mean(array[:,1]),np.mean(array[:,2])]
  mean_axis2=[np.mean(array[0,:]),np.mean(array[1,:]),np.mean(array[2,:])]
  mean_flattened=np.mean(array)

  var_axis1=[np.var(array[:,0]),np.var(array[:,1]),np.var(array[:,2])]
  var_axis2=[np.var(array[0,:]),np.var(array[1,:]),np.var(array[2,:])]
  var_flattened=np.var(array)

  std_axis1=[np.std(array[:,0]),np.std(array[:,1]),np.std(array[:,2])]
  std_axis2=[np.std(array[0,:]),np.std(array[1,:]),np.std(array[2,:])]
  std_flattened=np.std(array)

  max_axis1=[np.max(array[:,0]),np.max(array[:,1]),np.max(array[:,2])]
  max_axis2=[np.max(array[0,:]),np.max(array[1,:]),np.max(array[2,:])]
  max_flattened=np.max(array)

  min_axis1=[np.min(array[:,0]),np.min(array[:,1]),np.min(array[:,2])]
  min_axis2=[np.min(array[0,:]),np.min(array[1,:]),np.min(array[2,:])]
  min_flattened=np.min(array)

  sum_axis1=[np.sum(array[:,0]),np.sum(array[:,1]),np.sum(array[:,2])]
  sum_axis2=[np.sum(array[0,:]),np.sum(array[1,:]),np.sum(array[2,:])]
  sum_flattened=np.sum(array)

 dicc={
  'mean': [mean_axis1,mean_axis2, mean_flattened],
  'variance': [var_axis1, var_axis2, var_flattened],
  'standard deviation': [std_axis1, std_axis2, std_flattened],
  'max': [max_axis1, max_axis2, max_flattened],
  'min': [min_axis1, min_axis2, min_flattened],
  'sum': [sum_axis1, sum_axis2, sum_flattened]
}



 return dicc