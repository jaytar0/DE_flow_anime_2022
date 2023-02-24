# Dashboarding
Thank you for reading if you have gotten this far! Now that we have everything in place and a view of our data ready for the analysis phase, let's get to it!
In my prorject flow I have described two ways that I have wanted to visualize this data [Looker Studio](https://lookerstudio.google.com/) and [Power BI](https://powerbi.microsoft.com/en-us/).

In this writeup I will only be walking through the looker portion since power BI has a very similar process.

> I will be uploading the Power BI variant later on, since I have the most experience in it (want to make it look extra nice!)


## Google Looker Studio
First step we will be taking is connecting a data source. Here we can fill out details pertaining to your respective ```cloud provider``` if you are using one. It will bring up a list of vendors and the rest is history. Below you can see me entering the details of my connection.


![image](/assets/looker_connection.png)


Once that is all setup you will have the main view of your canvas and your data sources to your right.
![image](/assets/looker_data_source.png)


Let's get creating!



![image](/assets/dash_update.png)


> Once your cloud resource trials end you may not have access to your source data anymore. To display this indefinitely, I have downloaded a csv version of what I had finalized in snowflake and uploaded it to google to use as an "offline" data source.


## Power BI
This tool requires you to be on a windows system and have the desktop app installed. Once you have a physical copy of windows or a virtualized version of it, head over to the ```Microsoft App Store``` and download Power BI. 

> Note: I believe you do need to have a microsoft account for log-in purposes, so create a dummy one if you don't have it already


For connections it will run a similar process as the looker portion of the writeup.


[Back](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/dbt_process.md) | [To Home Page](https://github.com/jaytar0/DE_flow_anime_2022/) 
