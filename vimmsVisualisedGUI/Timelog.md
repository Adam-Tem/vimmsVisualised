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

* _1 hour_ Designed some mock wireframes for the potential load screen to show on the experiment page, or throughout the software tool when the user is having to wait on the execution of a process. Unsure whether the user should just be notified upon completion or have to wait on the specific page.

* _2.5 hours_ It is now possible to select any of the controllers currently identified in the Experiment.py file other than the agentBased controller as I have a few questions around that one. I also realised when coding away that the experiment was not actually taking into consideration changes made to the smart_roi parameters present in the controller, as I had not done appropriate parsing of these fields. This has now been resolved and will mean that the correct values input by the user as apposed to the defaults will be used.

### 06 Dec 2023

- _2 hours_ Back again looking at how to get the graph to cooperate on the experiment summary page. It just appears that the controls for moving and altering the graph image are not working, but the nav bar and graph are linked as the save function works properly. I have managed to get it to display one graph now, but will try and get it so there is an option to choose between what graph the user wants to see related to the summary.

### 10 Dec 2023

- _1 hour_ Another quickhour fighting against the bloody summary graph but I feel I will know how to sort it now. Manana.

## Week 11

### 11 Dec 2023

- _2 hours_ Finally resolved the issue with the uninteractive summary graph. I have now also added the option to select between what results graph you wish to have displayed.

* _1.5 hours_ Wow that was actually reasonably simple! Absolutely brilliant that PyQt has a built in tool tip function, so all I had to do was write a simple script to parse the docstring of the constructor of the selected controller, then assign these descriptions to the appropriate label! It has been set up just now with the assumption that all parameters will have a description associated with it, so I'll need to test that to be sure. But yeah, basically got the tool tip working already!

### 12 Dec 2023

- _2 hours_ Initially started by doing some debugging of the new tool tip description implementation, now seems fully functional across entire GUI. I have now also started adding the implementation of the advanced parameters selection screen. At first I thought I would have to make it an optional seleciton, but it is part of all the controllers so I can just add it as a default. Just a tedious process going through and adding all the different parameters, but will get there eventually!

### 13 Dec 2023

- _2 hours_ Managed to finish off adding in the advanced params screen to the experiment page. Still have to set up the parsing of the values, but have added in the appropriate tool tip descriptions.

* _1.5 hours_ Parsing of advanced parameters now also added to the experiment page. Was initially just going to be lazy and hard code everything, but it is set up now with not 100% abstraction, but still makes use of kwargs to construct the object.

* _1 hour_ Now added load/save param state to the advanced params also.

* _1 hour_ And that should be the advanced parameters variables being properly parsed and used in the simulate page also! Will still need to stress test this and I am bound to find bugs, but after an n=1 case with the basic TopN controller, all seems to be working well.

### 14 Dec 2023

- _1.5 hours_ Managed to get the first test script up and running. Had to modify the main script so that an instance of the page was created using a class so I could construct one for the testing, but got that resolved and I have added the first navigation test.

* _2 hours_ Status report has been written for project, identifying that the GUI is essentially complete with regards to core functionality and it is now just about tidying it up and adding in some nicer details.

* _1 hour_ Proper test that checks navigation of the GUI now successfully implemented.

### 15 Dec 2023

- _1.5 hours_ Added a pop up that is now displayed upon the completion of an experiment. To keep it consistent across the GUI, threading now occurs on the simulate page and the pop up is abstracted so that the same functionality is used to display a similar thing when a simulation completes.

### 16 Dec 2023

- _1.5 hours_ Threading now successfully added to the extract generate page also, displaying a pop that the user must interact with upon completion. This pop up is abstracted to be the same functionality across all thread completion. When a thread is running, I have also set it up so that the execution button of that particular action is disabled, meaning only one form of a particular action can occur at any one time. Even though the extract and generate functions typically execute in a swift manenr, it is good for completeness to have them run on worker threads also.

* _2 hours_ Finally tidied up where all the newly generated files are set to be stored when created. This applies for extracted data, generated data, simulated data, experiment results and also saved parameter states.

## Week 12

### 18 Dec 2023

- _1.5 hours_ Got to love a good bit of extraction! Modified the simulate page so that there is only one function that runs the simulation and adjusts itself on the fly to what controller has been picked. Still have to add in how some newer parameters such as the grid parameter should be parsed and constructed. But basic controllers work and it shouldn't be too much hassle to add in a new custom widget for the grid options.

* _1 hour_ Have created a solution at the moment that just constructs a default box manager grid, will be something that I'll need to ask about -- time to add some MORE parameters?!

### 22 Dec 2023

- _1.5 hours_ After doing very minimal work this week, I finally actually started to bother going through every aspect of the GUI to see what and what isn't working. So far I have identified a couple of issues with roi_params but should be an easy fix, and then some float to int parsing errors, but again shouldn't be too challenging to resolve.

### 23 Dec 2023

- _1.5 hours_ Finished off testing and started to remove some of the bugs. Fixed roi param issue and altered new experiment page so that it didn't store old parameters.

* _1.5 hours_ Resolved all currently identified issues in the generate section of the code. I have identified some parameters that appear to only have one option, so they are currently displayed as labels and not adjustable. Also, the exact match ms2 sampler is not actually complete, so I have removed it as an option from the code. All simulate bugs should be gone as well, other than the DsDA docstring issue, but I probably will create a separate unique function for this to make it an option.

### 24 Dec 2023

- _1.5 hours_ Another little bug squashed! Actually quite a nice solution for this one, as I had to create a new custom widget to allow the editing/parsing of the scoring params found in the intensity non overlap controller. For some reason the Non overlap controller had the same params but did not encounter the same issue? But it has now been sorted and again other than the DsDA controller, that should be all the experiment controllers now fully functional. Nice to get that one solved in the one sitting, feel like I am starting to know what I am doing.

* _1.5 hours_ Resolved an issue where it was possible to still click to add a fullscan file even when there was none selected. Completed this in slightly a hacky way, but it's just starting to get to the point where a lot of stuff is nested and I don't want to be passing too much about. Got it working though which is nice.

## Week 13

### 26 Dec 2023

- _0.5 hours_ A nice little quick fix removing the horrible code that I had written last time when trying to send a signal about for the mzml upload. Tidied it now so the signal is actually coming from the upload button and not in a hierarchical mess.

* _0.5 hours_ Added the same sort of case checking for the "Add experiment case" button, so that it is only enabled both when a valid controller is selected and the text edit area for naming the case has an appropriate text value as apposed to being empty or just spaces.

### 27 Dec 2023

- _1 hour_ Not much focus, but I have tidied up the visualise interface to now use the custom mzml upload widget and also the graph constructor method. I still don't really know how to fix the really laggy 3d plot, and will also have to move the generation of the plot to a thread as it takes a while so will be best to not make the GUI look as if it is crashing again.

### 31 Dec 2023

- _1 hour_ Yeah, progress has not been great on the project over the past few days. Time hasn't been wasted though as I have been reviewing and analysing the "Hall of Fame" dissertations in good detail, understanding the general structure and layout of them. I should have officially recorded how long I had spent doing this as it was a good few hours. Alas, I have finally added some new code to the project itself, with an error message now being shown to the user if there is invalid input when trying to execute n action. It is very much a general error message at the moment, but at least identifies the issue rather than leaving the user unaware.

## Week 14

### 01 Jan 2024

- _1 hour_ Just out here trying to catch as many edge cases as possible, with the extract interface now only allowing you to actually execute an extract action when there is a (hopefully) valid file selected and a name for the output file, not just an empty string.

* _0.5 hours_ Also now added the same to ensure that there is a valid sampler selected for all options and that the file name, number of chems to sample and adduct proportion cut off are not empty strings.

* _0.5 hours_ Rinse and repeat once again, this time with the simulate page. A couple of adjustments to the custom widgets to add a file upload for .p files and moved about the pyqt signals to the superclass to limit repeated code. Unsure whether all this input checking I should be moving to a different file, but it is not clogging up the interface files too much.

### 02 Jan 2024

- _1.5 hours_ Feels very strange writing the year as "2024"! Like I always seem to do, I have gone back and abstracted the code I wrote yesterday. This ensures an executable button was only clickable given valid inputs, now in a nicer more concise manner, parameterised and passed around rather than written multiple times. This is now found throughout the GUI.

### 03 Jan 2024

- _2 hours_ Spent a solid bit of time looking at the graphing section of the GUI there. I have now moved the updating of the graph to a thread, again just to stop the GUI looking like it is frozen. I have added in the retention time parameters for the 2d scatter plot, but for the 3d plot I am now also looking at the parameters for the "scan range". I don't 100% know how this works in with the rest of the variables, but this will be the focus to keep working on it and develop it further.

* _2 hours_ Again, looking to modify the visualise page but an aspect that appears in multiple locations throughout the GUI, I have been trying to build a slider for the range values as well as text input. I did have the two handles on the slider for a while, but somehow have managed to break it... I guess I probably shouldn't use this python library but I feel like I am close to solving it so will stick with it.

* _1 hour_ Another bit of progress made, I now have the text box updating to match the slider, just need to get it working the other way round and tidy it up a bit more.

### 04 Jan 2024

- _5 hours_ Holy moly that was an all day kind of task to eventually get that working! Slider bar now used to set the retention time values on the visualise page, I will add it to the other pages but just not today because that was way too long working on the one thing. Happy to get it done, and it is parameterised in such a way that I will probably add it for the scan window scaling as well for the visualisation page. An absolute nightmare to get working but at least it is done.

### 05 Jan 2024

- _1.5 hours_ Okay, after constructing the range slider in a parameterised, abstracted manner, I have now been able to easily implement a slider that controls the scan range for the 3d bar plot. It is not necessary to use it for the 2d plot as it is nowhere near as computationally expensive to display all values. Again, this ensures only suitable values are passed to the display functions and also tidies up the interface. I will still have to add it to the other areas of the GUI for RT, but progress made!

* _1 hour_ Quick bit of work and a new script for parsing the RT from a .p file, but that is now the RT slider found on the simulate page.

## Week 15

### 08 Jan 2024

- _2.5 hours_ A good stopping point and some good progress made. When trying to add the customisation of the box geompetry variables, I have actually identified that the create widgets function was rather verbose, and could be condensed considerably. I am now also in the process of considering removing one of the parameters from the method signature as well, as I think it is no longer needed... However my brain is slightly frazzled working on this one section and it is getting late so will go back to it tomorrow and get it (hopefully) finished!

### 09 Jan 2024

- _2 hours_ The extra "potential constructor" parameter has now been removed and the create_widgets function now works even if there is multi-level nesting of constructors given a controller, its parameters and the parameters' parameters. Still have to create a parsing function for the construction of the box grid but should not be a challenge at all.

* _1.5 hours_ Parsing and construction of inline parameter objects now complete, including the box parameter with the nested objects. I have encountered an error going back to check the workings of it that the scroll on the simulate page is not expanding, but will fix this next.

### 10 Jan 2024

- _0.5 hours_ Fixed issue with scroll bar not activating on the simulate page.

* _4 hours_ A solid shift put in towards modifying the visualise page to add all the placeholders for getting the plotly graph to display for previously run experiments. So far so good, will just still have to get the experiment save path changed and then get the graph actually displayed but near enough everything is good to go for it and there is a specific widget that can work with plotly graphs so should be easy enough to implement.

### 11 Jan 2024

- _3 hours_ So much time fighting against a widget to not actually get anywhere... Still not managing to get the plotly graphs to load into the GUI, and I am really struggling to understand why... Hopefully tomorrow brings better luck.

### 13 Jan 2024

- _1.5 hours_ It is starting to become less promising in terms of implementing the plotly graphs into the GUI. I have searched the web for hours now trying to find a solution, and I've even tried using PyQt6 to see if that makes a difference but unfortunately not... Really unsure how to get my this issue.

## Week 16

### 15 Jan 2024

- _3.5 hours_ I have no idea how to fix this problem. The view attempts to load the html and then crashes instantly, and just gives me random error messages... So much time spent getting nowhere.
