from pytube import YouTube
import os

# 要下載的 YouTube 影片 URL
url = 'https://youtu.be/LQYeAl6GEQA' # 你需要替換為你想下載的影片URL
video = YouTube(url)

# 顯示影片名稱與開始下載的訊息
print(f'開始下載: {video.title}')

# 檢查儲存路徑是否存在，如果不存在，則建立資料夾
save_path = "D:/Youtube/MV"
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 下載影片，選擇最高品質
video.streams.get_highest_resolution().download(output_path=save_path)

# 下載完成後的訊息
print(f'{video.title} - 影片已下載完成')
