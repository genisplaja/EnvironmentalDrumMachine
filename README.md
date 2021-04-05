# EnvironmentalDrumMachine
ENVIRONMENTAL DRUM MACHINE by Genís Plaja i Roglans
Developed under the framework of the Computational Music Creativity Course, SMC Master, 2020-2021.

### "A Python-based drum machine to play JSON-based drum patterns with every day and environmental sounds."

This repository contains all the material to run the Environmental Drum Machine experiment.

The EnvironmentalDrumMachine.py Python file contains the source code of the framwework. The code is commented
so the user can know what is done at each step. The main class and all the functions have a formatted docstring
where you can find the information of what is the main use of the functions, what are the expected parameters and
outputs.

The experiment.ipynb is basically hosting the interaction between the user and the application. Along the notebook,
you can find useful explanations of the project and how to play with it. Some examples are already provided.

The folder ./cmc_kit contains the Environmental Sounds Drum Kit generated using the Drum Part Classification Model.
This modeel was generated using sklearn, and the features were extracted using Essentia's Music Extractor. Please
note that the samples are automatically segmented using an energy threshold, aiming at removing the silent or
unvoiced regions from them. You can review the implementation of this approach in the

The ./patterns folder contains example patterns written in JSON format. Further detail and instruction to create
your own patterns is given in the notebook.

If you have doubts or problems reproducing the experiment, please contact me at genis.plaja01@estudiant.upf.edu.

THANKS!
