from youtube_transcript_api import YouTubeTranscriptApi

video_id = "GPnwuPEUNlo"
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# print(transcript)
for words in transcript:
    print(words["text"])
