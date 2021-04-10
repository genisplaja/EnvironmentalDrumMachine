# EnvironmentalDrumMachine
### A Python-based drum machine to create and play JSON-based drum patterns with environmental sounds.
Developed within the framework of the Computational Music Creativity Course (Music Technology Group, Barcelona).

---

## Included files

### Source code

The ```EnvironmentalDrumMachine.py``` Python file contains the source code of the framwework. The code is commented,
so the user can know what is done at each step. The main class and all the functions have a formatted docstring
where you can find the information of what is the main use of the functions, what are the expected parameters and
outputs.

### Example notebooks

The ```experiment.ipynb``` is basically hosting the interaction between the user and the application. Along the notebook,
you can find useful explanations of the project and how to play with it. Some examples are already provided.

The ```classification.ipynb``` provides an example code walkthrough to automatically build your environmental drum kit with
a Machine Learning model. The training and evaluation dataset is the
[Freesound One-Shot Percussive Sounds Dataset](https://zenodo.org/record/3665275#.YHGJe2gp5-V).

### Provided kits and patterns

The folder ```./kit``` contains the Environmental Sounds Drum Kit generated using the Drum Part Classification Model.
This modeel was generated using sklearn, and the features were extracted using Essentia's Music Extractor. Please
note that the samples are automatically segmented using an energy threshold, aiming at removing the silent or
unvoiced regions from them. You can review the implementation of this approach in the

The ```./patterns``` folder contains example patterns written in JSON format. Further detail and instruction to create
your own patterns is given in the notebook.

### IMPORTANT DISCLAIMER

This project is not installable yet. It is also not robust to errors. In other words, it
assumes that the drum patterns are written correctly, and that the folder structures and files are organized
in the right way. While we increasr the robustness of the application, please make sure you write the patterns well
and organize the sounds as they are organized now.

## External tools used
- [Essentia](https://essentia.upf.edu/) by MTG
- [pyo](http://ajaxsoundstudio.com/pyodoc/) by Ajax Sound Studio
- [pydub](https://github.com/jiaaro/pydub) by @jiaaro

If you have doubts or problems reproducing the experiment, please contact me at genis.plaja01@estudiant.upf.edu.

Thanks:)
