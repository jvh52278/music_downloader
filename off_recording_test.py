
from yt_dlp import YoutubeDL # to download videos
import ffmpeg # to extract mp3 from videos
import music_tag # to add meta data
# modules imported for testing
import os # for file system operations
import time # to get the unix time

# testing -- to download a video and extract audio

links_to_download = ["http://localhost/vpage_template.php?video_id=U0DvnaPmyvBGGQp1689570294E&x=223&y=125"]

# check if the download directory alread exists
working_directory = os.getcwd() #the current working directory the script is being run from - source: https://flexiple.com/python/python-get-current-directory/
files_in_working_directory = os.listdir(working_directory) # generate a list of all files in the working directory - source: https://www.tutorialspoint.com/How-can-I-list-the-contents-of-a-directory-in-Python
# print all directories in the working directory
download_directory_exists = False
download_directory_name = "test_download_directory"
for directory in files_in_working_directory:
    if os.path.isdir(directory): #if the file is a directory print it to terminal - source: https://www.python-engineer.com/posts/check-if-file-exists/
        # check if the directory has the same name as the download directory\
        if (directory == download_directory_name):
            download_directory_exists = True
            print ("download directory already exists")
if (download_directory_exists == False):
    print ("download directory does not exist")
    print ("creating download directory")
    # create the download directory - source: https://www.geeksforgeeks.org/create-a-directory-in-python/
    os.mkdir(download_directory_name)
download_directory_full_path = os.path.join(working_directory, download_directory_name) #append the download directory to working directory - source: https://stackoverflow.com/questions/8989988/can-os-path-join-or-other-python-method-append-a-automatically-for-the-cas
print (download_directory_full_path)
print ("-------------------")
##### download the video #####
# set the file name
time_downloaded = round(time.time() * 100000) # to get the unix time - source for rounding: https://www.w3schools.com/python/ref_func_round.asp
expected_file_extension = ".mp3"
downloaded_file_name = "download_" + str(time_downloaded) # source for string conversion: https://pythonprinciples.com/blog/converting-integer-to-string-in-python/ 
# Note: there is no need to specify the file extension at the download stage -- is it automatically done
path_to_downloaded_file = os.path.join(download_directory_full_path,downloaded_file_name)
print (path_to_downloaded_file)

download_options = {
    # save to a specific directory - source: https://stackoverflow.com/questions/35643757/how-to-set-directory-in-ydl-opts-in-using-youtube-dl-in-python
    'outtmpl': path_to_downloaded_file,
    # extract audio
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}


with YoutubeDL(download_options) as ydl:
    error_code = ydl.download(links_to_download)

# apply metadata - source: https://pypi.org/project/music-tag/
# Note: specifying the file extension here is required
placeholder_metadata = "pirate" + str(round(time.time() * 100000))
path_to_file_for_metadata = os.path.join(download_directory_name,downloaded_file_name + expected_file_extension)
file_to_edit = music_tag.load_file(path_to_file_for_metadata) # open the file for editing
# set the title
file_to_edit['tracktitle'] = placeholder_metadata
# set the artist
file_to_edit['artist'] = 'artist'
# set the album
file_to_edit['album'] = "album"
file_to_edit.save() # save the meta data


