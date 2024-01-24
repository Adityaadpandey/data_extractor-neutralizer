from youtubesearchpython import VideosSearch
from langdetect import detect

def get_video_links(search_query, max_results=50):
    video_links = []

    while len(video_links) < max_results:
        videos_search = VideosSearch(search_query, limit=min(20, max_results - len(video_links)))
        results = videos_search.result()

        for video in results['result']:
            try:
                title = video['title']
                # Detect language based on the title
                if detect(title) == 'en':
                    video_links.append(video['link'])

                    if len(video_links) >= max_results:
                        break
            except KeyError:
                pass

        if 'nextPageToken' not in results:
            break

        videos_search = VideosSearch(search_query, limit=min(20, max_results - len(video_links)), pageToken=results['nextPageToken'])

    return video_links

def save_links_to_file(video_links, file_path='video_links.txt'):
    with open(file_path, 'w') as file:
        for link in video_links:
            file.write(link + '\n')

if __name__ == "__main__":
    search_query = input("Enter your YouTube search query: ")

    video_links = get_video_links(search_query)

    save_links_to_file(video_links)

    print(f"\nList of Video Links saved to 'video_links.txt'")
