# Timelog

* VIMMS VISUALISED: A GUI FOR THE SIMULATION OF LC-MS/MS EXPERIMENTS
* ADAM TEMPLETON
* 2567437T
* DR. KEVIN BRYSON


## Week 0

### 14 Sep 2023

* *1 hour* Research into the science of LC-MS/MS.
* *2 hours* Create initial wireframes of GUI, both single- and multi-page examples.   

### 15 Sep 2023

* *2 hours* Explore potential GUI frameworks to use for the project, identifying mostly Python libararies as the best choice as that is the language used to code the current simulator.

## Week 1

### 21 Sep 2023

* *3 hours* First meeting and introduction to supervisor. Performed as a group meeting with students who have similar project descriptions. Deep dive into the background of ViMMS and why it is needed. General outline of what the project ahead entails.

### 22 Sep 2023

* *2 hours* Watch level 4 guidance zoom meeting.
* *1 hour* Set up forked repository of existing ViMMS repo, adding wireframes made so far and timelog.
* *1.5 hours* Watched videos by Alan D Moore, author of multiple python GUI textbooks, explain the differences between Tkinter and PyQt5, then another explaining how to work with QtDesigner.

## Week 2

### 25 Sep 2023

* *1.5 hours* Reviewed 'Guide to ViMMS' and 'Demo' Jupyter Notebooks.
* *1 hour* Researched and watched videos on how to make multi-page GUIs.
* *3.5 hours* Install QtDesigner Software, watch videos on initial setup, create starter interface.

### 26 Sep 2023

* *2 hours* Fixed issue to resolve window scaling, added navigation from home page to extract data page.

### 27 Sep 2023

* *1 hour* Added file selection to Extract Data Screen.

### 28 Sep 2023

* *1.5 hours* Implemented data extraction functions to extract data page.
* *1 hour* Tidy up the monolith file that I had created into nicer, smaller files. Utils and Interfaces now separated from the main python script to run the application.
* *1 hour* Studied process of Chemical Creator functions and planned how to implement it.

### 29 Sep 2023

* *1 hour* Built interface of the generate chemical screen, yet to add functionality.
* *1 hour* Meeting with advisor.

### 30 Sep 2023

* *2 hours* Implemented most of the functionality for the generate chemical screen, still a few edge cases to sort out but majortiy of work is done.

### 01 Oct 2023

* *1 hour* Began to watch videos on how to best implement the graphing of results into the app.

## Week 3

### 02 Oct 2023

* *1 hour* Page navigation now possible from start page to each individual page and back.
* *1.5 hours* Reading through the different possible controllers and trying to work out what variables have to be identified to run them properly and give a user full control. 

### 03 Oct 2023

* *2 hours* Worked through each and every class in the controllers section of the vimms module to see how I could organise the simulate page. Many, MANY variables and parameters...

### 04 Oct 2023

* *2 hours* Began to build the simulate interface with all the possible inputs, still to change it so that only the necessary parameters are visible with the correct controller selected.

* *1 hour* Added a few helper functions and little adjustments to the simulate page.

### 05 Oct 2023

* *1 hour* It is now possible to run the TopN controller from the simulate page of the app, where a .mzML file is ultimately produced after inputting an appropriate .p file. Still have to add loading screen and clarification, but good to get the basic functionality in place.

* *1 hour* A struggling hour getting bogged down in the weeds  about how to try and display progress loading bar of the simulation.

### 06 Oct 2023

* *1 hour* Continued to work on adding loading screen, it now displays but then lags the entire system.

* *0.5 hours* Meeting with adviser, clarifying direction and getting questions answered.

* *1.5 hours* Now looking into Qthreads for running the simulation while still having the load display work properly. Although, still not working...

### 07 Oct 2023

* *2 hours* Shifted focus away from trying to get the loading screen to display and actually had some success with code elsewhere! A function is now in place that when you select a particular controller on the simulation page (well, n=1 with the topN controller still currently) only the appropriate paramerters are displayed to the user to avoid unwanted input and paramter overload.

* *2 hours* Well, I thought to get away from the n=1 scenario of the topN controller I'd add another, so chose to implement TopN Smart ROI. Well what a can of worms that was I opened, as it had more selective paramters on the inside for ROI and smart ROI builders... However it has appropriately been implemented and now there is a nice way of showing the sub headings and displaying the appropriate parameters. The actual goal of adding more functionality was also complete, so another successful bit of coding.

* *1 hour* Began to look into what visualisation tool would be best, potentially leaning towards matplotlib.

## Week 3

### 10 Oct 2023

* *2 hours* Managed to get a graph displayed and have begun adding the functions that are already in place in the guide to vimms jupyter notebook, but will try and get this a bit nicer looking.

### 11 Oct 2023

* *1 hour* adjusted parameters to make graph display only relevant scales on the axes, to get a better look at the data.

### 12 Oct 2023

* *2 hours* Began thinking about how to create an abstracted function to do the variety of input checks when a user input is needed. Made wireframe sketch of the different edge cases I felt would have to be checked, and then began to implement. I feel the checker function should work, just need to find the best way to pass the parameters.

### 13 Oct 2023

* *0.5 hours* Adviser meeting discussing best way forward for visualisation and then concept of reflection.

* *1.5 hours* Researched reflection topic through online videos, trying to explore the best way to implement it.

### 14 Oct 2023

* *1.5 hours* Began implementing reflection, trying to separate everything up nicely and keep high cohesion.

### 15 Oct 2023

* *1.5 hours* Managed to implement the refelection when selecting the topN controller, you only have to add a new controller to the identify params file and then any new specific parameters to the ParamWidgets const file.

* *1.5 hours* It is now possible to run the topN controller from the simualte page, where parameters are all passed using the generated ones and nothing is pulled in a hard coded style. Of course I am now back to an n=1 scenario again, but tbh to get this working is really good.

* *1.5 hours* Trying to make the simulate page have a scroll bar in preparation for the controllers with too many parameters to display on the one screen.

## Week 4

### 16 Oct 2023

* *1 hour* Trying to get the page to now reflect on inline constructors, in this case the Roi and smart roi builder params.

* *1 hour* Managed to now reflect the inline objects, just now finding a way to construct the objects with the appropriate values going to the correct paramter.

### 17 Oct 2023

* *2 hours* Finally beginning to understand the purpose fo kwargs, just now encountering an error where the findchild function will not identify the custom button widget that I have created...

### 18 Oct 2023

* *2.5 hours* Fixed issue where the widgets were not being identified, so now have successfully implemented the kwargs selection of parameters. It appears now though that the simulation functions do not like floats and require integers in some cases... May just go and edit the actual controller code to fix this.

### 19 Oct 2023

* *1 hour* Fixed bug that was stopping the indexing of a particular list because the value was being passed as a float as apposed to an integer, however did have to modify the actual Vimms code to resolve this. Also began reseaching more about the PEP 8 style guide to start making my code more readable and fall in line with the current ViMMs library.

### 20 Oct 2023

* *1 hour* Attended supervisor meeting, where we discussed the current implementation of the execution of the controllers, showing clearly the abstraction that is now in place, but that potentially more selection should be used to identify what style of action occurs when using the controller. Explaining further the science of the code and trying to understand the project more fully.

## Week 5

### 24 Oct 2023

* *2 hours* Fought against the visualisation page trying to get a scatter plot of the mzml file to display but with no success.

### 25 Oct 2023

* *1 hour* Successfully displayed the data of the scatter plot, but encountering an issue where the x label is not showing.

* *1 hour* Going back to work on the generate/simulate side of things, as the generated p files are not suitable for the simulate side of things. Nothing working as of yet but don't really see how to get this working.

### 26 Oct 2023

* *1.5 hours* The can of worms has been opened once again... After going back into detail on the generate page, I have come to realise that there is also a plethora of parameters associated with all selectable options on this page as well. I have begun to set it up to try and use the same functions already implemented for the simulate page, trying to extract those further to allow for use elsewhere. I have listed all parameters in the global parameters file as well, under their respective categories.

### 27 Oct 2023

* *1 hour* Meeting with advisor discussing progress of the week, discussing what sort of explanation would be required of the actual science of the project and deciding to work on fixing current code rather than start anything new.

### 28 Oct 2023

* *2 hours* Continous refactoring of the display parameter function, trying to make it applicable for every drop down combo box no matter the display. Feel like I am close to solving this issue, just trying to wokr out where to pass the appropriate parameters so that I am not repeating code anywhere while keeping the function definitions concise enough so that it is not just a parameter mess.

## Week 6

### 30 Oct 2023

* *1.5 hours* A fairly successful coding session. That is the display params function now abstracted in such a way that any combo box and associated group box can be passed to then allow for the appropriate parameters to be displayed. Only issue I am now encountering is that the scroll area on the generate page is not actually changing or creating a scroll bar, it is more that the grid layout is becoming squished, which I am currently unsure the reason of.

* *1 hour* Fighting against the scroll area with no avail, very annoying bug that I cannot work out...

### 31 Oct 2023

* *2.5 hours* That took WAY too long to figure out, but I got there in the end! For some reason, the scroll area was creating an extra layer that also had to be changed and updated ot force the scroll bar to work, but I got there in the end! Unfortunately my brain is fairly frazzled and simple mathematics on how to reduce the group boxes and main window back to the approriate size after selecting a lesser amount of parameters is not coming to me, but is hopefully the last bug GUI wise and then I can finally start looking at implementation of the code again to make it work properly.

### 01 Nov 2023

* *2 hours* That took way too long once again to get rid of such a simple bug, but who new that adjusting both the minimum and fixed height of an object would increase its size but then not decrease it proportionately... Finally figured out this mess, so param boxes now expand and contract to the right size on the generate page. Time to fix up the implementation of the actual code.

* *1.5 hours* Nearly there with the implementation of the generate stuff, just encountering an issue where it is not iterating over the group boxes and combo boxes in the order I want them to.

* *1.5 hours* You can now successfully run and generate a chemical mzml simulation! Okay it is with some dodgy parameter selection at the moment but a file can be created and with the options available you can create the file.

### 02 nov 2023

* *1.5 hours* After a very successful bit coding, it is now possible to go from end to end with the generation/extraction, to simulation to visualisation of a chemical mixture being passed through a simulated LCMS experiment.

* *1.5 hours* I have now added a variety of custom widgets regarding the uploading of different file types and also for selecting whether files should be replaced or not. Functionality for parsing these new widgets still has to be implemented come to think of it as I type this, but at least the graphical side of things is sorted and there at least is a visible option for all different possible params.

* *1 hour* Began to construct a high level UML of the vimms repository. Very high level, showing only the basic functionality and inputs so far but gives general consensus of what goes on with the inner functions.

### 03 Nov 2023

* *1 hour* Added proper parsing for new custom widgets to allow the generation to run on any selection of samplers given appropriate inputs.

* *1 hour* Meeting with adviser and PhD student showing developments and discussing next steps.

## Week 7

### 06 Nov 2023

* *1.5 hours* Added very basic 3d graph display to the visualise page, not interactive even though I had it that way before but is capable of swapping between 2d scatter plot and 3d bar plot.

### 08 Nov 2023

* *2 hours* Added the controller to the displays of the graphs, so the user can interact with the visuals and also swap between visualisations.

* *1 hour* When selecting a particular sampler or controller from a combo box, the fields that hold defaults now show these when the selection is made. 