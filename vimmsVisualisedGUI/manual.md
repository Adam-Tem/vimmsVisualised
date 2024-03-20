# ViMMS Visualised User Manual

Listed below are ways in which you as a user can interact with the ViMMS VIsualised GUI, providing the details about how to start the software and perform a variety of tasks provided through the interface.

## Starting the application

To start the ViMMS Visualised interface, navigate to the 'vimmsVisualisedGUI' folder of your cloned repository:

```
cd C:\PATH\TO\CLONE\vimmsVisualisedGUI
```

And run the following command to launch the interface:

```
python VimmsMain.py
``` 

The interface should load in after a few seconds, presenting you with the ViMMS Visualised start page.

## Starter Tasks

The functionality provided by the interface can be rather overwhelming to those new to LC-MS/MS experiments and the ViMMS framework.

Below are a range of tasks to get you started with the interface, showing what it is capable of and how to utilise its features.

### Task 1: Generating a Synthetic Chemical Mixture

The ViMMS framework allows you to generate synthetic chemical mixtures that are representative of real-world examples. These synthetic chemical mixtures are created by fine-tuning a list of parameters associated with different samplers.

**Your Task:**

- Navigate the "Extract/Generate" Page and select the "Generate" tab.
- Select and adjust the parameters to those shown below.

| Type of Parameter | Specific Parameter | Suggested Value      |
|-------------------|--------------------|----------------------|
| Formula Sampler   | Uniform Sampler    | 70 - 1000            |
| RTI Sampler       | Uniform RTI        | Default settings     |
| Chromatogram Sampler | Gaussian        | Default settings     |
| MS2 Sampler       | Uniform            | Default settings     |
| Chems to sample   | -                  | 1000 to 2000         |

- Make sure the MS level is set to 2, and name the mixture "starter_task_generate".
- Press the generate button.

Once this process completes, you should be notified by a pop-up window proclaiming this success. All newly made files are stored in their respective sub-directories in the "results" folder, which resides in the VimmsVisualisedGUI folder.

## Task 2: .mzML Creation

From the newly created synthetic chemical mixture, we want to sample from this using one of our controllers to generate an .mzML file. This .mzML file will be used for injection purposes when we simulate our experiment.

- Navigate to the "Simulate" Page.
- Select the generated .p file* we have just created as input, stored in "results/generated_data"
- Choose the TopN Controller and adjust the parameters by keeping most as the default values but setting the following:

| Parameter           | Value        |
|---------------------|--------------|
| N                   | 3            |
| Isolation Width     | 1            |
| MZ Tolerance        | 10           |
| RT Tolerance        | 15           |
| Min MS1 Intensity   | 500          |

- Name this file "starter_task_simulate".
- Press the simulate button.

Once again, this should notify you upon completion with a suitable pop-up window, with the new file being stored in "results/simulations".

*\*These pickle files that we have generated from the first task store information of chemical objects that have been serialized into a binary format. The chemical objects in our file are UnknownChemical objects, with information such as the m/z, maximum intensity, and starting retention time for the chemical.*  


## Task 3: Perform an experiment with the synthetic chemicals

It is all fine and well having generated these chemical mixtures, but the main use case for the ViMMS framework is it allows you to replace most of your lab experiments to test fragmentation strategies, only having to conduct final validations on a real system. In our case, this is the controllers. Performing LC-MS/MS experiments is time-consuming and costly. ViMMS resolves these issues by letting users perform simulations in a much more time-efficient manner through well-designed programming scripts. This allows for more consistent repeatability and also for the comparison of different controllers.

**Your Task:**

- Navigate to the Experiment page.
- Choose your newly generated .mzML from Task 2, stored in "results/simulations", to be injected 3 times.
- Select and adjust the parameters for a the TopN Controller*.
- Name this case "starter_task_case1" and add it to the experiment case list.
- To allow comparison of controllers, repeat this process with the TopNEX Controller. Name this case "starter_task_case2" and add it to the experiment list.
- Navigate to the "Peak Picking Params" tab and select "XCMS". The default values will be fine here.
- Name the experiment "starter_task_exp", and then click "Run Experiment".
- Upon completion, view the summary page.

## Task 4: Different Visualisations

The ViMMS framework offers a variety of different ways to visualize results produced from the simulation of chemical mixtures. Different visualizations can potentially offer new insights, improve understanding, and identify different characteristics of said chemical mixtures.

**Your Task:**
- Navigate to the "Visualise Results" Page.
- From the "mzmL viewer" tab, select the mzML file produced from Task 2.
- Test the visualization of the scatter plot.
- Swap to the "experiment Viewer" tab, and select the experiment folder as input, stored in "results/experiment_results". Once selected, press the "Visualise" button to update the display.
- Run through the different visualizations to see the results of your experiment.

**Congratulations!** You have successfully completed the ViMMS Visualised starter tasks. Please feel free to explore the interface more.
