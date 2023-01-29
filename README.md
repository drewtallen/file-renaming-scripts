# file-renaming-scripts

## A couple of Python scripts that rename files within subfolders of a root file path. I wrote these during my first semester in the fall of 2021.

### Motivation
I maintain a personal media server called Plex that requires structuring large amounts of folders containing video files. When the files are first added, they need to be renamed in order to adhere to Plex's naming conventions so that the correct metadata can be scraped for the Plex Streaming UI. Needless to say, manually renaming dozens or hundreds of files is tedious. These scripts provide an instant renaming process.

### What the scripts do
The folder structure for a TV show on a Plex media server typically looks like the following: "C:\User\Knight Rider\Season 02", with subfolders representing individual discs within the season folders when files are first added. The rename_show_files script takes a TV Shows root file path, iterates through each season and its subfolders, renaming each video file as an episode of the selected show in numerical order. The rename_disc_files takes the file paht of an individual disc subfolder as an input and renames just those files. A renamed file would look like: "Knight Rider - s02e03".

### Notes
I created these during my first semester without much coding experience. They do contain some exception handling, but an understanding of how files are structured for media servers is needed for these scripts to make sense. As mentioned, a very particular folder structure is required for the scripts to work correctly. However, I am pleased with these as they solve a practical problem of mine and I still use them to this day.
