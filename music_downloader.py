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
a link cannot be entered more than once
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
                # save the inputs to the lists
                links_to_download.append(user_input_inner_download)
                track_titles.append(user_input_title)
                track_artist.append(user_input_artist)
                track_albums.append(user_input_album)
                print(links_to_download,track_titles,track_artist,track_albums,sep="")
            if (confirm_input != "yes"):
                # do not save the inputs to the list
                print ("the inputs will be discarded")
        # if the user enters "done"
        if (user_input_inner_download == "done"):
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

            """
            to do next
            get list of all mp3 files in the current working directory
            sort from first created to last created
            loop through file list and apply metadata, also rename -> the file list should be in the same order as the metadata list
            move all mp3 files into the download directory
            """

            # clear the links
            links_to_download.clear()
            track_titles.clear()
            track_artist.clear()
            track_albums.clear()
        # if the user enters "exit"
        if (user_input_inner_download == "exit"):
            link_loop_status = "not running"
    # if the user enters "exit"
    if (user_input == "exit"):
        run_status = "not running"