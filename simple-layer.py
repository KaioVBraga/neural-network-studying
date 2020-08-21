import random

inputs = [1, 2, 3, 4, 5, 6]
# weights = [i for i, x in enumerate(inputs)]
weights = [1,2,3,4,5,6]

def neuron(inputs, weights):
  bias = round(random.random()*100)/10
  weigthed_list = list(inputs[i] * weights[i] for i, x in enumerate(inputs))
  return sum(weigthed_list) + bias


outputs = []
for i in range(0, 2):
  outputs.append(neuron(inputs, weights))

print(outputs)