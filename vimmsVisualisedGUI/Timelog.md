# Timelog

- VIMMS VISUALISED: A GUI FOR THE SIMULATION OF LC-MS/MS EXPERIMENTS
- ADAM TEMPLETON
- 2567437T
- DR. KEVIN BRYSON

## Week 0

### 14 Sep 2023

- _1 hour_ Research into the science of LC-MS/MS.
- _2 hours_ Create initial wireframes of GUI, both single- and multi-page examples.

### 15 Sep 2023

- _2 hours_ Explore potential GUI frameworks to use for the project, identifying mostly Python libararies as the best choice as that is the language used to code the current simulator.

## Week 1

### 21 Sep 2023

- _3 hours_ First meeting and introduction to supervisor. Performed as a group meeting with students who have similar project descriptions. Deep dive into the background of ViMMS and why it is needed. General outline of what the project ahead entails.

### 22 Sep 2023

- _2 hours_ Watch level 4 guidance zoom meeting.
- _1 hour_ Set up forked repository of existing ViMMS repo, adding wireframes made so far and timelog.
- _1.5 hours_ Watched videos by Alan D Moore, author of multiple python GUI textbooks, explain the differences between Tkinter and PyQt5, then another explaining how to work with QtDesigner.

## Week 2

### 25 Sep 2023

- _1.5 hours_ Reviewed 'Guide to ViMMS' and 'Demo' Jupyter Notebooks.
- _1 hour_ Researched and watched videos on how to make multi-page GUIs.
- _3.5 hours_ Install QtDesigner Software, watch videos on initial setup, create starter interface.

### 26 Sep 2023

- _2 hours_ Fixed issue to resolve window scaling, added navigation from home page to extract data page.

### 27 Sep 2023

- _1 hour_ Added file selection to Extract Data Screen.

### 28 Sep 2023

- _1.5 hours_ Implemented data extraction functions to extract data page.
- _1 hour_ Tidy up the monolith file that I had created into nicer, smaller files. Utils and Interfaces now separated from the main python script to run the application.
- _1 hour_ Studied process of Chemical Creator functions and planned how to implement it.

### 29 Sep 2023

- _1 hour_ Built interface of the generate chemical screen, yet to add functionality.
- _1 hour_ Meeting with advisor.

### 30 Sep 2023

- _2 hours_ Implemented most of the functionality for the generate chemical screen, still a few edge cases to sort out but majortiy of work is done.

### 01 Oct 2023

- _1 hour_ Began to watch videos on how to best implement the graphing of results into the app.

## Week 3

### 02 Oct 2023

- _1 hour_ Page navigation now possible from start page to each individual page and back.
- _1.5 hours_ Reading through the different possible controllers and trying to work out what variables have to be identified to run them properly and give a user full control.

### 03 Oct 2023

- _2 hours_ Worked through each and every class in the controllers section of the vimms module to see how I could organise the simulate page. Many, MANY variables and parameters...

### 04 Oct 2023

- _2 hours_ Began to build the simulate interface with all the possible inputs, still to change it so that only the necessary parameters are visible with the correct controller selected.

- _1 hour_ Added a few helper functions and little adjustments to the simulate page.

### 05 Oct 2023

- _1 hour_ It is now possible to run the TopN controller from the simulate page of the app, where a .mzML file is ultimately produced after inputting an appropriate .p file. Still have to add loading screen and clarification, but good to get the basic functionality in place.

- _1 hour_ A struggling hour getting bogged down in the weeds about how to try and display progress loading bar of the simulation.

### 06 Oct 2023

- _1 hour_ Continued to work on adding loading screen, it now displays but then lags the entire system.

- _0.5 hours_ Meeting with adviser, clarifying direction and getting questions answered.

- _1.5 hours_ Now looking into Qthreads for running the simulation while still having the load display work properly. Although, still not working...

### 07 Oct 2023

- _2 hours_ Shifted focus away from trying to get the loading screen to display and actually had some success with code elsewhere! A function is now in place that when you select a particular controller on the simulation page (well, n=1 with the topN controller still currently) only the appropriate paramerters are displayed to the user to avoid unwanted input and paramter overload.

- _2 hours_ Well, I thought to get away from the n=1 scenario of the topN controller I'd add another, so chose to implement TopN Smart ROI. Well what a can of worms that was I opened, as it had more selective paramters on the inside for ROI and smart ROI builders... However it has appropriately been implemented and now there is a nice way of showing the sub headings and displaying the appropriate parameters. The actual goal of adding more functionality was also complete, so another successful bit of coding.

- _1 hour_ Began to look into what visualisation tool would be best, potentially leaning towards matplotlib.

## Week 3

### 10 Oct 2023

- _2 hours_ Managed to get a graph displayed and have begun adding the functions that are already in place in the guide to vimms jupyter notebook, but will try and get this a bit nicer looking.

### 11 Oct 2023

- _1 hour_ adjusted parameters to make graph display only relevant scales on the axes, to get a better look at the data.

### 12 Oct 2023

- _2 hours_ Began thinking about how to create an abstracted function to do the variety of input checks when a user input is needed. Made wireframe sketch of the different edge cases I felt would have to be checked, and then began to implement. I feel the checker function should work, just need to find the best way to pass the parameters.

### 13 Oct 2023

- _0.5 hours_ Adviser meeting discussing best way forward for visualisation and then concept of reflection.

- _1.5 hours_ Researched reflection topic through online videos, trying to explore the best way to implement it.

### 14 Oct 2023

- _1.5 hours_ Began implementing reflection, trying to separate everything up nicely and keep high cohesion.

### 15 Oct 2023

- _1.5 hours_ Managed to implement the refelection when selecting the topN controller, you only have to add a new controller to the identify params file and then any new specific parameters to the ParamWidgets const file.

- _1.5 hours_ It is now possible to run the topN controller from the simualte page, where parameters are all passed using the generated ones and nothing is pulled in a hard coded style. Of course I am now back to an n=1 scenario again, but tbh to get this working is really good.

- _1.5 hours_ Trying to make the simulate page have a scroll bar in preparation for the controllers with too many parameters to display on the one screen.

## Week 4

### 16 Oct 2023

- _1 hour_ Trying to get the page to now reflect on inline constructors, in this case the Roi and smart roi builder params.

- _1 hour_ Managed to now reflect the inline objects, just now finding a way to construct the objects with the appropriate values going to the correct paramter.

### 17 Oct 2023

- _2 hours_ Finally beginning to understand the purpose fo kwargs, just now encountering an error where the findchild function will not identify the custom button widget that I have created...

### 18 Oct 2023

- _2.5 hours_ Fixed issue where the widgets were not being identified, so now have successfully implemented the kwargs selection of parameters. It appears now though that the simulation functions do not like floats and require integers in some cases... May just go and edit the actual controller code to fix this.

### 19 Oct 2023

- _1 hour_ Fixed bug that was stopping the indexing of a particular list because the value was being passed as a float as apposed to an integer, however did have to modify the actual Vimms code to resolve this. Also began reseaching more about the PEP 8 style guide to start making my code more readable and fall in line with the current ViMMs library.

### 20 Oct 2023

- _1 hour_ Attended supervisor meeting, where we discussed the current implementation of the execution of the controllers, showing clearly the abstraction that is now in place, but that potentially more selection should be used to identify what style of action occurs when using the controller. Explaining further the science of the code and trying to understand the project more fully.

## Week 5

### 24 Oct 2023

- _2 hours_ Fought against the visualisation page trying to get a scatter plot of the mzml file to display but with no success.

### 25 Oct 2023

- _1 hour_ Successfully displayed the data of the scatter plot, but encountering an issue where the x label is not showing.

- _1 hour_ Going back to work on the generate/simulate side of things, as the generated p files are not suitable for the simulate side of things. Nothing working as of yet but don't really see how to get this working.

### 26 Oct 2023

- _1.5 hours_ The can of worms has been opened once again... After going back into detail on the generate page, I have come to realise that there is also a plethora of parameters associated with all selectable options on this page as well. I have begun to set it up to try and use the same functions already implemented for the simulate page, trying to extract those further to allow for use elsewhere. I have listed all parameters in the global parameters file as well, under their respective categories.

### 27 Oct 2023

- _1 hour_ Meeting with advisor discussing progress of the week, discussing what sort of explanation would be required of the actual science of the project and deciding to work on fixing current code rather than start anything new.

### 28 Oct 2023

- _2 hours_ Continous refactoring of the display parameter function, trying to make it applicable for every drop down combo box no matter the display. Feel like I am close to solving this issue, just trying to wokr out where to pass the appropriate parameters so that I am not repeating code anywhere while keeping the function definitions concise enough so that it is not just a parameter mess.

## Week 6

### 30 Oct 2023

- _1.5 hours_ A fairly successful coding session. That is the display params function now abstracted in such a way that any combo box and associated group box can be passed to then allow for the appropriate parameters to be displayed. Only issue I am now encountering is that the scroll area on the generate page is not actually changing or creating a scroll bar, it is more that the grid layout is becoming squished, which I am currently unsure the reason of.

- _1 hour_ Fighting against the scroll area with no avail, very annoying bug that I cannot work out...

### 31 Oct 2023

- _2.5 hours_ That took WAY too long to figure out, but I got there in the end! For some reason, the scroll area was creating an extra layer that also had to be changed and updated ot force the scroll bar to work, but I got there in the end! Unfortunately my brain is fairly frazzled and simple mathematics on how to reduce the group boxes and main window back to the approriate size after selecting a lesser amount of parameters is not coming to me, but is hopefully the last bug GUI wise and then I can finally start looking at implementation of the code again to make it work properly.

### 01 Nov 2023

- _2 hours_ That took way too long once again to get rid of such a simple bug, but who new that adjusting both the minimum and fixed height of an object would increase its size but then not decrease it proportionately... Finally figured out this mess, so param boxes now expand and contract to the right size on the generate page. Time to fix up the implementation of the actual code.

- _1.5 hours_ Nearly there with the implementation of the generate stuff, just encountering an issue where it is not iterating over the group boxes and combo boxes in the order I want them to.

- _1.5 hours_ You can now successfully run and generate a chemical mzml simulation! Okay it is with some dodgy parameter selection at the moment but a file can be created and with the options available you can create the file.

### 02 nov 2023

- _1.5 hours_ After a very successful bit coding, it is now possible to go from end to end with the generation/extraction, to simulation to visualisation of a chemical mixture being passed through a simulated LCMS experiment.

- _1.5 hours_ I have now added a variety of custom widgets regarding the uploading of different file types and also for selecting whether files should be replaced or not. Functionality for parsing these new widgets still has to be implemented come to think of it as I type this, but at least the graphical side of things is sorted and there at least is a visible option for all different possible params.

- _1 hour_ Began to construct a high level UML of the vimms repository. Very high level, showing only the basic functionality and inputs so far but gives general consensus of what goes on with the inner functions.

### 03 Nov 2023

- _1 hour_ Added proper parsing for new custom widgets to allow the generation to run on any selection of samplers given appropriate inputs.

- _1 hour_ Meeting with adviser and PhD student showing developments and discussing next steps.

## Week 7

### 06 Nov 2023

- _1.5 hours_ Added very basic 3d graph display to the visualise page, not interactive even though I had it that way before but is capable of swapping between 2d scatter plot and 3d bar plot.

### 08 Nov 2023

- _2 hours_ Added the controller to the displays of the graphs, so the user can interact with the visuals and also swap between visualisations.

- _1 hour_ When selecting a particular sampler or controller from a combo box, the fields that hold defaults now show these when the selection is made.

### 10 Nov 2023

- _1.5 hours_ Designed a wireframe for the experiment page and also added the button to access the page, but no functionality as of yet.

- _1 hour_ Meeting with advisor and PhD student to explore best route forward for implementation of experiment in GUI, using wireframe as discussion point.

### 11 Nov 2023

- _2.5 hours_ Initial development of adding fullscans for experiment case should now be complete, encountered the same silly error with the scroll area once again but managed to resolve the issue.

### 12 Nov 2023

- _2.5 hours_ Selecting a controller and having the option to input variables has now been added to the perform experiment page, reusing much of the code found elsewhere in the project already. With a few extra inputs, the page now also has the capability of creating and storing the experiment cases, so now it is just setting up the "run experiment" function that takes these cases and performs said experiment.

### 16 Nov 2023

- _1 hour_ Encountering a major error that I cannot solve... The program is looking for some variable but I cannot work out for the life of me what is being processed wrong to allow the experiment to run.

### 17 Nov 2023

- _1 hour_ During the weekly meeting we were able to diagnose the problem! Just one little dependency, I hadn't actually installed R, the language used to perform the experiment! A new error has appeared but at least it is some progress!

## Week 8

### 22 Nov 2023

- _1 hour_ Managed to finish of the debugging and altered my vimms install so that experiments can now be run from start to finish! Will now move on to displaying the summary and allowing the user to go on and visualise the result.

* _1.5 hours_ When an experiment is complete, the user can now see the summary of said experiment on the same display and then also has the option to then start a new experiment by going back to the main run experiment page. Object variables are reset but widgets I have not implemented the reset for just yet.

### 23 Nov 2023

- _2 hours_ I thought I was beyond fighting against PyQt Scrollbars but I guess not! Thankfully I have managed to resolve the issue that would occur if selecting a controller with too many parameters visible on the screen to be shown, and a scrollbar is added to resolve it!

* _1 hour_ You know that way you touch something that you thought was working, but then fall down the rabbit hole of one bug that finds another bug? Yeah that was the past hour! Managed to get the topN controller now running on the experiment side of things. Was hoping to add the visualisation but should get that afterwards!

* _1.5 hours_ Alas, no avail with the visualisation on the summary page. I feel like I am close but it's just a pain in the backside with all of these PyQt widgets working ever so slightly differently than you would expect them to.

### 26 Nov 2023

- _1.5 hours_ Managed to at least identify what the problem was with the graph situation. It is now displaying the figures, but in actual fact it is two figures and not one plot, so a bit of restyling or some sort of selection will need to be done on the page so it can work for this.

## Week 9

### 28 Nov 2023

- _1 hour_ Amidst the minefield that is end of semester assignments, I have managed to find the time to add a nice little usability undo button connected to the fullscan and experiment case lists!

### 29 Nov 2023

- _4.5 hours_ Sheesh that was a shift put in today for not very much code, but at least it is some working code! The experiment function has now been moved onto a separate thread when executing, as to stop the GUI from freezing and appearing as if it has crashed. Using the QThreads built in module, I eventually figured out how to structure this so that it can perform the execution in the tidiest way possible, following Qt guidelines.

### 30 Nov 2023

- _2.5 hours_ Wow, how much I now appreciate my old self for doing all the abstraction and parameterisation from before! Managed to get a save/load controller parameter state working in a pretty easy manner. Currently only implemented on the experiment page but will be easy to add to the simulate page!

### 02 Dec 2023

- _2 hours_ Began to add the XCMS parameter choices to the experiment page. Managed to get the tab widget functional and the inputs displaying.

* _1.5 hours_ In a fairly swift manner, I was able to get the xcms paramters parsed and passed to the run experiment function, with only the one set of parameters the selection box does not need to be updated. I have now also added the functionality so that the save and load config buttons know what to do if it is the controller or xcms screen detected. May potentially change this so that it would change the tab given the selection, or maybe show an error if wrong selection is made.

## Week 10

### 05 Dec 2023

- _1 hour_ Nice simple task to start the day, abstracted the load and save config buttons so that they could be added to the simulate experiment page as well.
