from pytube import YouTube

def download_youtube_video(url, resolution="480p"):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Get the stream with the specified resolution
        stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
        
        # If no stream found with the specified resolution
        if not stream:
            print(f"No stream found with resolution {resolution}. Downloading the highest resolution available.")
            stream = yt.streams.get_highest_resolution()
        
        # Download the video
        stream.download()
        
        print(f"Video downloaded successfully: {yt.title}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = "https://www.youtube.com/watch?v=A28zps9Q-gE"
download_youtube_video(url)

