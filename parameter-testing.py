## create model and optimizer
learning_rate = 0.2
momentum = 0.00007
device = "cpu"
model = CNN().to(device) #using cpu here
optimizer = optim.SGD(model.parameters(), lr=learning_rate,
                      momentum=momentum)