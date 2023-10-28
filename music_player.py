import youtube_dl
import asyncio
import os


class MusicPlayer:
    def __init__(self):
        self.voice_client = None

    def download_video(self, url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict.get("url", None)
            ydl.download([url])
        return video_url

    async def join_channel(self, ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            self.voice_client = await channel.connect()
        else:
            await ctx.send("You need to be in a voice channel to use this command.")

    async def play_music(self, ctx, url, discord):
        await self.join_channel(ctx)
        if self.voice_client.is_playing():
            self.voice_client.stop()
        video_url = self.download_video(url)
        self.voice_client.play(discord.FFmpegPCMAudio(video_url))

    def stop_music(self):
        if self.voice_client and self.voice_client.is_playing():
            self.voice_client.stop()
            os.remove("song.mp3")