# BeatBot
This project is an AI-powered music generation system that uses ML and DL to generate music when a tune ( seed notes) are given as input. 
The model uses its input sequence as a starting point and uses its knowledge of music patterns to generate the next notes.
The system is built using Python and uses the following libraries:
* Keras
* Tensorflow
* Music21
* Numpy
* Matplotlib
* Pickle
* Flask
* Gunicorn
* Replicated the model from the paper [Generating Music with Recurrent Neural Networks](https://arxiv.org/abs/1308.0850) by [Boulanger-Lewandowski et al.](https://www.cs.toronto.edu/~lcharlin/papers/ismir2012.pdf)
* The model is trained on the [MuseData](https://www.kaggle.com/imsparsh/musicnet-dataset) dataset and the [Maestro](https://magenta.tensorflow.org/datasets/maestro) dataset.
* The model is trained on a GPU instance on Google Cloud Platform.
* The main code is in the [notebook]