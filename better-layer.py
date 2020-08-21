import random


def neuron(inputs, weights, bias):
  weigthed_list = list(inputs[i] * weights[i] for i, x in enumerate(inputs))
  return sum(weigthed_list) + bias


def create_outputs(inputs, weights, biases):
  middle_outputs = []
  for i in range(0, len(biases)):
    middle_outputs.append(neuron(inputs, weights[i], biases[i]))
  return middle_outputs


def create_layers(inputs, weights_list, biases_list):
  layers = list()
  layers.append(create_outputs(inputs, weights_list[0], biases_list[0]))

  if(len(weights_list) > 2):
    for i in range(1, len(weights_list)-1):
      layers.append(create_outputs(layers[i-1], weights_list[i], biases_list[i]))

  layers.append(create_outputs(layers[-1], weights_list[-1], biases_list[-1]))

  return layers


def main():
  inputs = [1,2,3,4,5,6]

  weights_list = [
    [[1,2,3,4,5,10], [1,2,3,4,25,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6]],
    [[1,45,1,2,3], [1,2,1,2,3], [1,2,1,2,3], [1,2,1,2,3], [1,2,1,2,3]],
    [[1,2,1,2,3], [1,2,1,2,3], [1,2,1,2,3], [1,2,1,2,3], [1,2,1,2,3]],
    [[1,2,1,2,3], [1,2,1,2,3], [1,2,1,2,3], [1,2,1,2,3], [1,2,1,2,3]]
  ]

  biases_list = [
    [1,2,3,4,5],
    [1.33,2.5,1.96,2,3],
    [1,2,4,2,3],
    [1,2]
  ]

  layers = create_layers(inputs, weights_list, biases_list)

  print("0 : ", inputs)
  for i, layer in enumerate(layers):
    print(i+1,": ",layer)


main()