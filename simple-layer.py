import random

inputs = [1, 2, 3, 4, 5, 6]
# weights = [i for i, x in enumerate(inputs)]
weights = [1,2,3,4,5,6]
weights1 = [1,2,1,2,3]

def neuron(inputs, weights):
  bias = round(random.random()*100)/10
  weigthed_list = list(inputs[i] * weights[i] for i, x in enumerate(inputs))
  return sum(weigthed_list) + bias

def create_middle_outputs(inputs, weights, size):
  middle_outputs = []
  for i in range(0, size):
    middle_outputs.append(neuron(inputs, weights))
  return middle_outputs


middle_outputs = create_middle_outputs(inputs, weights, len(weights1))


final_outputs = []
for i in range(0, 2):
  final_outputs.append(neuron(middle_outputs, weights1))


print(inputs)
print(middle_outputs)
print(final_outputs)