from yt_dlp import YoutubeDL # to download videos
import ffmpeg # to extract mp3 from videos

# testing -- to download a video and extract audio

links_to_download = ["http://localhost/vpage_template.php?video_id=U0DvnaPmyvBGGQp1689570294E&x=223&y=125"]

download_options = {
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}


with YoutubeDL(download_options) as ydl:
    error_code = ydl.download(links_to_download)
