def generator(model, sequences, idx_to_char, n_chars):
    # Set the model in evalulation mode
    model.eval()

    # Define the softmax function
    softmax = nn.Softmax(dim=1)

    # Randomly is selected the index from the set of sequences
    start = np.random.randint(0, len(sequences) - 1)

    # The pattern is defined given the random idx
    pattern = sequences[start]

    # By making use of the dictionaries, it is printed the pattern
    print("\nPattern: \n")
    print(''.join([idx_to_char[value] for value in pattern]), "\"")

    # In full_prediction we will save the complete prediction
    full_prediction = pattern.copy()

    # The prediction starts, it is going to be predicted a given
    # number of characters
    for i in range(n_chars):
        # The numpy patterns is transformed into a tesor-type and reshaped
        pattern = torch.from_numpy(pattern).type(torch.LongTensor)
        pattern = pattern.view(1, -1)

        # Make a prediction given the pattern
        prediction = model(pattern)
        # It is applied the softmax function to the predicted tensor
        prediction = softmax(prediction)

        # The prediction tensor is transformed into a numpy array
        prediction = prediction.squeeze().detach().numpy()
        # It is taken the idx with the highest probability
        arg_max = np.argmax(prediction)

        # The current pattern tensor is transformed into numpy array
        pattern = pattern.squeeze().detach().numpy()
        # The window is sliced 1 character to the right
        pattern = pattern[1:]
        # The new pattern is composed by the "old" pattern + the predicted character
        pattern = np.append(pattern, arg_max)

        # The full prediction is saved
        full_prediction = np.append(full_prediction, arg_max)

    print("Prediction: \n")
    print(''.join([idx_to_char[value] for value in full_prediction]), "\"")