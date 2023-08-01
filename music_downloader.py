from yt_dlp import YoutubeDL # to download videos
import ffmpeg # to extract mp3 from videos
import music_tag # to add meta data
import os # for file system operations
"""
# testing -- to download a video and extract audio

links_to_download = ["http://localhost/vpage_template.php?video_id=U0DvnaPmyvBGGQp1689570294E&x=223&y=125"]

download_options = {
    # See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}


with YoutubeDL(download_options) as ydl:
    error_code = ydl.download(links_to_download)
"""
"""
safeguards to add:
download cannot commence if there are any mp3 files in the working directory
metadata cannot be added if the number of mp3 files in the working directory does not match the number of links
"""
run_status = "running"
# create the download directory if it does not exist
current_working_directory = os.getcwd() #the current working directory the script is being run from
download_directory = "downloaded_files"
file_in_working_directory = os.listdir(current_working_directory) # generate a list of all files in the working directory
download_directory_exists = False # true if the download directory exists
for file in file_in_working_directory:
    if (os.path.isdir(file)):
        if (file == download_directory):
            download_directory_exists = True
if (download_directory_exists == False):
    # create the download directory
    os.mkdir(download_directory)
while (run_status == "running"):
    # set the link information
    links_to_download = [] # links to download
    track_titles = [] # track titles
    track_artist = [] # track artists
    track_albums = [] # track albums
    print ("select from the following options:\nenter 'download' to start the download process\nenter 'exit' to exit the program")
    user_input = input()
    # if the user enters "download"
    link_loop_status = ""
    if (user_input == "download"):
        link_loop_status = "running"
    while (link_loop_status == "running"):
        print("enter a link to download from\nenter 'done' to commence downloading\nenter 'exit' to return to the previous menu")
        user_input_inner_download = input()
        # if the user enters a link
        if (user_input_inner_download != "done" and user_input_inner_download != "exit"):
            # enter track title
            print ("enter a track title:")
            user_input_title = input()
            # enter track artist
            print ("enter a track artist:")
            user_input_artist = input()
            # enter track album
            print ("enter a track album:")
            user_input_album = input()
            # save the links to download
            print ("the following inputs have been entered")
            print ("track link: ",user_input_inner_download, sep="")
            print ("track title: ",user_input_title, sep="")
            print ("track artist: ",user_input_artist, sep="")
            print ("track album: ",user_input_album, sep="")
            print ("is this correct?\nenter 'yes' to confirm'\nenter anything else to discard inputs")
            confirm_input = input()
            if (confirm_input == "yes"):
                # check if the the link to be entered already exists
                link_already_exists = False # if the link already exists, then true
                if (len(links_to_download) > 0):
                    # check if the link already has been entered
                    for link in links_to_download:
                        if(link == user_input_inner_download): # check if this link has already been entered
                            link_already_exists = True
                # save the inputs to the lists if the link does not already exist
                if (link_already_exists == False):
                    links_to_download.append(user_input_inner_download)
                    track_titles.append(user_input_title)
                    track_artist.append(user_input_artist)
                    track_albums.append(user_input_album)
                    print(links_to_download,track_titles,track_artist,track_albums,sep="")
                else:
                    print ("link cannot be added: link already exists")
            if (confirm_input != "yes"):
                # do not save the inputs to the list
                print ("the inputs will be discarded")
        # if the user enters "done"
        ## check if there are any mp3 files in the working directory
        files_in_working_directory = os.listdir(current_working_directory)
        mp3_files_do_not_exist_in_the_working_directory = False # if true, there are no mp3 files in the working directory
        number_of_mp3_files = 0 # this should be 0 for the download to occur
        for file in files_in_working_directory:
            file_path_to_check = file
            # seperate the file name from the file extension
            file_name, file_extension = os.path.splitext(file_path_to_check)
            file_extension_to_check_for = ".mp3" # the file extension to find
            if (file_extension == file_extension_to_check_for):
                number_of_mp3_files = number_of_mp3_files + 1
        # check the count of mp3 files
        if (number_of_mp3_files == 0):
            mp3_files_do_not_exist_in_the_working_directory = True
        if (number_of_mp3_files != 0):
            print ("download cannot commence if there are mp3 files in the working directory")
        # download cannot occur if there are any mp3 files in the working directory
        if (user_input_inner_download == "done" and len(links_to_download) > 0 and mp3_files_do_not_exist_in_the_working_directory == True):
            try:
                print ("the links will now be downloaded")
                    # download the links
                    # loop through the list of links
                for x in range(0, len(links_to_download)):
                    link = links_to_download[x] # the link to download from
                    title = track_titles[x] # the track title
                    artist = track_artist[x] # the artist
                    album = track_albums[x] # the album
                    # download from each link
                    #full_file_path = os.path.join(current_working_directory,download_directory,title)
                    full_file_path = os.path.join(current_working_directory,"%(title)s.%(ext)s")

                    download_options = { # set the download options
                    'updatetime': False,
                    'outtmpl': full_file_path, # save to download directory
                    'postprocessors': [{  # Extract audio using ffmpeg
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    }]
                }
                
                with YoutubeDL(download_options) as ydl:
                    error_code = ydl.download(links_to_download)
                
                # apply metadata
                ## list all mp3 files, with the first file downloaded at the top of list
                ## get list of all files in the current working directory
                all_file_in_current_directory = os.listdir(current_working_directory)
                ## get all the mp3 files into a list
                list_of_mp3_files = [] # a list all mp3 files, matching with file_creation_time
                file_creation_time =[] # the associated file creation time of all mp3 files, matching with list_of_mp3_files
                for file in all_file_in_current_directory:
                    # get the file extention
                    path_to_file = os.path.join(current_working_directory,file)
                    ## split the file name and the file extention
                    file_name, file_extension = os.path.splitext(path_to_file)
                    # if the file extention is ".mp3", add the file path to the list of mp3 files, as well as the file creation time
                    file_extension_to_find = ".mp3" # the file extention to look for
                    if (file_extension == file_extension_to_find):
                        # add the file to the mp3 list
                        list_of_mp3_files.append(path_to_file)
                        # add the file creation time
                        file_creation_time.append(os.path.getctime(path_to_file))
                        pass
                # apply metadata
                ## sort the creation date list from smallest to largest
                sorted_file_creation_times = sorted(file_creation_time)
                ## loop through the file creation times, find the file, then apply metadata, and move the file to download directory
                for x in range(0, len(sorted_file_creation_times)):
                    # find the mp3 file with the specified creation date
                    find_this_creation_date = sorted_file_creation_times[x]
                    for y in range(0,len(list_of_mp3_files)):
                        if (file_creation_time[y] == find_this_creation_date):
                            # apply metadata, using music-tag
                            file_to_open = list_of_mp3_files[y]
                            edit_file = music_tag.load_file(file_to_open) # open the file
                            # the outer loop index should match up with the indexes of the metadata lists
                            # apply track title
                            edit_file["tracktitle"] = track_titles[x]
                            # apply track artist
                            edit_file["artist"] = track_artist[x]
                            # apply track album
                            edit_file["album"] = track_albums[x]
                            # save metadata
                            edit_file.save()
                            # move and rename file to download directory
                            source_file_path = file_to_open
                            new_file_name = track_titles[x] # also the title of the track
                            move_destination = os.path.join(current_working_directory,download_directory,(new_file_name + ".mp3"))
                            os.rename(source_file_path, move_destination)
                        pass
                # clear the links
                links_to_download.clear()
                track_titles.clear()
                track_artist.clear()
                track_albums.clear()
            # if the user enters "exit"
                pass
            except:
                print ("download failed")
        elif (len(links_to_download) <= 0):
            print ("you must enter at least one link")
        if (user_input_inner_download == "exit"):
            link_loop_status = "not running"
    # if the user enters "exit"
    if (user_input == "exit"):
        run_status = "not running"