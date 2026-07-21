import yt_dlp

ydl_opts = {
    'js_runtimes': {'node': {}},
    'extractor_args': {'youtube': ['player-client=web,default']},
    'quiet': True,
    'extract_flat': True,
}
# There is an undocumented way to pass args via 'compat_opts' or just set them? Let's just try without remote_components. 
# wait, yt_dlp command line parser maps --remote-components ejs:github to a specific option, I'll just check if without it we get error.

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info("https://www.youtube.com/watch?v=Bhcpcnwxl0Y", download=False)
        print("SUCCESS:", info.get('id'))
except Exception as e:
    print("ERROR:", str(e))
