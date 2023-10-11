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