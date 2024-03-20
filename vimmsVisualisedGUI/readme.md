# ViMMS Visualised Readme

ViMMS Visualised is a graphical user interface that has been created to offer an accessible way to utilise the functionality provided by the existing ViMMS framework. It allows users to perform LC-MS/MS experiments in-silico with the complexity of having to set up the required Python objects instantiated through the ViMMS library hidden from the user. The GUI provided four main aspects of functionality offered by ViMMS: extracting & generating chemicals, simulating controllers, performing experiments and visualising results.

The interface is a PyQt application that makes use of the wide variety of widgets provided by this interface toolkit as well custom widgets to receive input from the user. It has been designed in a "no-frills" way, with a strong focus on giving scientists a tool that is easy to navigate, self-explanatory and works well for the job at hand. 

The ViMMS framework is under active development, so the interface was designed in an abstracted manner to ensure that it was easily extensible to accommodate new additions to the underlying codebase. Each aspect of the code is separated, providing a high level of modularity to make it easier to maintain and develop.

## Installation steps

It is recommended to use an Anaconda virtual environment for the setup and installation of ViMMS Visualised to avoid any potential issues with dynamically linked libraries. 

### Dependencies

The existing ViMMS framework uses external peak-picking algorithms as part of the process when performing experiments. Listed below are the required dependencies that must be installed to use this functionality.

**_R:_** The programming language R is used by the peak-picking algorithms utilised by ViMMS. R can be installed [here](https://www.stats.bris.ac.uk/R/).

**_XCMS:_** Open an R terminal and type the following commands:

```if (!require("BiocManager", quietly = TRUE))```

```install.packages("BiocManager")```

```BiocManager::install("xcms")```


**_MZMine 2.53:_** Go the the [MZMine GitHub Repository](https://github.com/mzmine/mzmine2/releases). Select the zip folder appropriate for your OS and extract it to a preferred memory location.

### Anaconda environment (Recommended)

Install Anaconda for your machine [here](https://www.anaconda.com/download). To create a new virtual environment, run the following command:

```conda create --name \<name-of-env\> python=3.10```

At any point throughout this installation process you are asked to use a command prompt, use an Anaconda prompt and have your newly made environment activated by running the following command:

```conda activate \<name-of-env\>```

### Cloning the repository

Follow the appropriate steps needed for your OS to install git [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Create a clone of this repository on your local machine by navigating to where you want the files to be saved within a command prompt:

```cd PATH\TO\CLONE```

And run the following command:

```git clone https://github.com/Adam-Tem/vimmsVisualised.git```
### ViMMS

Copy the path to the 'vimms' folder of the cloned repository, that should resemble something similar to this:

```C:\PATH\TO\CLONE\vimms```

Open a command prompt and type "pip install " and then right click to paste in the path. Press enter to run the command:

```pip install C:\PATH\TO\CLONE\vimms```

### ViMMS Visualised requirements

The ViMMS Visualised GUI uses Python version 3.10.

The following two installations are required to run the interface.

**_QtRangeSlider:_** Run the command: 
```pip install QtRangeSlider```

**_PyQtWebEngine:_** Install this PyQt extension library by running one of the following commands:

_Anaconda Environment:_ ```
conda install conda-forge::pyqtwebengine```

_Local Installation_: ```
pip install PyQtWebEngine ```

## Testing

To see if the installation has been a success, try running the application. Start by navigating to the vimmsVisualisedGUI folder of your cloned repository:

```
cd C:\PATH\TO\CLONE\vimmsVisualisedGUI
```

And run the following command to launch the interface:

```
python VimmsMain.py
``` 

---
The ViMMS Visualised interface has a test suite that utilises the QtTest module of PyQt. QtTest was used as it allows the developer to simulate clicks and text input with the GUI, meaning interactions with the interface can be tested automatically. Unit tests are used to ensure a wide variety of tasks such as navigation and executing processes work as expected when input is simulated. 

To run the test suite, navigate to the vimmsVisualisedGUI folder of your cloned repository:  

```
cd C:\PATH\TO\CLONE\vimmsVisualisedGUI
```
And run the following command:

```
python testSuite.py
```
---