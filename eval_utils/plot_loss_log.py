import sys
from csv import reader
from matplotlib import pyplot

file_path = sys.argv[1]

with open(file_path, 'r') as f:
    data = list(reader(f))[1:]
    epochs = [int(i[0]) for i in data]
    losses = [float(i[1]) for i in data]
    val_losses = [float(i[2]) for i in data]

pyplot.title('Training steps')
pyplot.xlabel('Epoch')
pyplot.ylabel('Loss')
train_line = pyplot.plot(epochs, losses, color='blue', label='training loss')[0]
validation_line = pyplot.plot(epochs, val_losses, color='orange', label='validation loss')[0]
pyplot.legend(handles=[train_line, validation_line])
pyplot.show()
