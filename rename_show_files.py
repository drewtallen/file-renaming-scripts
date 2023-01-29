"""
A script created to rename video files to match Plex's naming conventions so that Plex--
can correctly scrape metadata for the Plex UI.

Due to the nature of ripping physical media to a local machine, it is easier to--
create subfolders within the root TV Show folder for each individual discs of a--
show's DVD season set. I.e., "C:\Plex\Castle\Season 02\disc2". Therefore, for a--
complete series, you might have multiple season subfolders and multiple disc--
subfolders within each season.

This renaming script requires this folder structure in order to execute correctly:

TVShow\Season\disc\video files.

While the intent was to solve a practical issue for myself, any kind of file can be--
renamed with this script, assuming it follows the folder structure above.
"""


import os, sys

def rename_show_files():


    path = ""

    while os.path.exists(path) == False:
        try:
            path = str(input("""Input root file path for TV Show to rename all of its files.
                                \nExample file path: \"C:\YourName\Shows\Knight Rider\"
                                \n\nInput root path: """))
            raw_path = r'{}'.format(path)
            base_show_directory = os.listdir(raw_path)
        except (FileNotFoundError, KeyboardInterrupt):
            print("Double check your file path to make sure it is correct and spelled correctly.\n")


    tvshowName = str(input("What is the name of the TV show you wish to add to your renamed files?\n"))

    seasonNumber = ""

    while (not isinstance(seasonNumber, int)) or (seasonNumber <0):
        try:
            seasonNumber = int(input("Enter the starting season number:\n"))
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



    k = 0
    j = 0
    s = 1
    n = episodeNumber
    

    for i in range(len(base_show_directory)):
        k=0
        n = episodeNumber
        season_path = os.path.join(raw_path+"\\"+base_show_directory[j]) #raw path + Season 01
        season_directory = os.listdir(season_path) # episode folders within Season 01
        for i in range(len(season_directory)):
            season_folder_path = os.path.join(season_path+"\\"+season_directory[k])
            try:
                season_folder_episodes = os.listdir(season_folder_path)
            except NotADirectoryError:
                print("""Make sure the base file path for the TV show was selected
                         and that all files are within subfolders within the base show folder.""")
                sys.exit(1)
            for file in season_folder_episodes:
                root,ext=os.path.splitext(season_folder_episodes[0])
                old_name = season_folder_path+"\\"+file
                if (n<10) and (n>0):
                    episode_name = "e0" + str(n)
                elif n>=10:
                    episode_name = "e" + str(n)
                if seasonNumber <10 and (seasonNumber >=0):
                    seasonName = "s0" + str(seasonNumber)
                elif seasonNumber >=10:
                    seasonName = "s" + str(seasonNumber)
                new_name = season_folder_path+"\\"+tvshowName+" - "+seasonName+episode_name
                os.rename(old_name,new_name+ext)
                n+=1
            k+=1
        j+=1
        seasonNumber +=1

    print("Files successfully renamed!")

rename_show_files()
