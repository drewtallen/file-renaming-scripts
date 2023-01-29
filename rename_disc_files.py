"""
A script created to rename video files to match Plex's naming conventions so that Plex--
can correctly scrape metadata for the Plex UI.

Due to the nature of ripping physical media to a local machine, it is easier to--
create subfolders within the root TV Show folder for each individual discs of a--
show's DVD season set. I.e., "C:\Plex\Castle\Season 02\disc2".

This particular script is meant for renaming files within a single subfolder of the TV show.
The following folder structure is required: "TVShow\Season\disc\video files".

While the intent was to solve a practical issue for myself, any kind of file can be--
renamed with this script, assuming it follows the folder structure above.
"""


import os, sys

def rename_disc_files():

    path = ""

    while os.path.exists(path) == False:
        try:
            path = str(input("""Input disc subfolder file path for TV Show to rename its files.
                                \nExample file path: \"C:\YourName\Shows\Knight Rider\Season 02\disc2"
                                \n\nInput disc path: """))
            raw_path = r'{}'.format(path)
            directoryList = os.listdir(raw_path)
        except (FileNotFoundError, KeyboardInterrupt):
            print("Double check your file path to make sure it is correct and spelled correctly.\n")


    tvshowName = str(input("What is the name of the TV show you wish to add to your renamed files?\n"))

    seasonNumber = ""

    while (not isinstance(seasonNumber, int)) or (seasonNumber <0):
        try:
            seasonNumber = int(input("Enter the season number you are renaming files for:\n"))
            if seasonNumber <0:
                print("Number must not be less than 0.\n")
        except ValueError:
            print("You must enter a number greater than zero. No letters are allowed.\n")

    if seasonNumber <10 and (seasonNumber >=0):
        seasonName = "s0" + str(seasonNumber)
    elif seasonNumber >=10:
        seasonName = "s" + str(seasonNumber)


    episodeNumber = ""

    while (not isinstance(episodeNumber, int)) or (episodeNumber <0):
        try:
            episodeNumber = int(input("Enter the episode number you wish to start with:\n"))
            if episodeNumber <0:
                print("Number must not be less than 0.\n")
        except ValueError:
            print("You must enter a number greater than zero. No letters are allowed.\n")


    i = episodeNumber
    k = 0
    for item in directoryList:
        if item in directoryList:
            root, ext = os.path.splitext(directoryList[k])
            oldName = str(raw_path+"\\"+item)
            if i < 10 and (i >0):
                episodeName = "e0" + str(i)
            elif i >=10:
                episodeName = "e" + str(i)
            newName = raw_path + "\\" + tvshowName + " - " + seasonName + episodeName + ext
            os.rename(oldName,newName)
            i+=1
            k+=1
            

rename_disc_files()


