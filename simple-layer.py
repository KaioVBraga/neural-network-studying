import random

inputs = [1, 2, 3, 4, 5, 6]
# weights = [3.1, 2.1, 8.7]


def neuron(inputs):
  bias = round(random.random()*100)/10
  weighted_list = list(map(lambda x: x*3 , inputs))
  sum_weighted = sum(weighted_list)

  return sum_weighted + bias

outputs = [];

for i in range(0, 2):
  outputs.append(neuron(inputs))

print(outputs)