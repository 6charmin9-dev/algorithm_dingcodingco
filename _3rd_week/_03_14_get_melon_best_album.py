'''
Q3. ✍️ 멜론 베스트 앨범 뽑기 - 원 문제 링크
Q. 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.

노래는 인덱스로 구분하며, 노래를 수록하는 기준은 다음과 같다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록한다. (단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)

2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.

3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.


노래의 장르를 나타내는 문자열 배열 genres와
노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,

베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.
# 1
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# 정답 = [4, 1, 3, 0]


# 2
genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays = [2000, 500, 600, 150, 800, 2500, 2000]
# 정답 = [0, 6, 5, 2, 4, 1]
'''
'''
hiphop: 4000 : 0, 6
pop: 3100 : 5, 2
classic: 1450 : 4, 1, 3
'''
def get_melon_best_album_1(genre_array, play_array):
    # 구현해보세요!
    result = []
    genre_to_plays_sum_map = {}
    genre_to_album_plays_map = {}
    for i in range(len(genre_array)):
        genre_to_plays_sum_map[genre_array[i]] = genre_to_plays_sum_map.get(genre_array[i], 0) + play_array[i]
        if genre_array[i] not in genre_to_album_plays_map:
            genre_to_album_plays_map[genre_array[i]] = []
        genre_to_album_plays_map.get(genre_array[i]).append((i, play_array[i]))
    # print(f"genre_to_plays_sum_map: {genre_to_plays_sum_map}")
    sorted_sum_items = sorted(genre_to_plays_sum_map.items(), key=lambda x: x[1], reverse=True)
    # print(f"sorted_genre: {sorted_genre}")
    for genre, _ in sorted_sum_items:
        album_plays = genre_to_album_plays_map.get(genre)
        sorted_album_plays = sorted(album_plays, key=lambda x: (-x[1], x[0]))[:2]
        result.extend([album[0] for album in sorted_album_plays])
    return result

def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    result = []
    genre_to_total_play_dict = {}
    genre_to_play_items_dict = {}
    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        if genre in genre_to_total_play_dict:
            genre_to_total_play_dict[genre] += play
            genre_to_play_items_dict[genre].append((i, play))
        else:
            genre_to_total_play_dict[genre] = play
            genre_to_play_items_dict[genre] = [(i, play)]
    sorted_genre_to_total_play_items = sorted(genre_to_total_play_dict.items(), key=lambda x: x[1], reverse=True)
    for genre, total_play in sorted_genre_to_total_play_items:
        sorted_album_to_play_items = sorted(genre_to_play_items_dict[genre], key=lambda x: (-x[1], x[0]))[:2] # sorted 는 안정정력을 하게 되어 원래 인덱스 순대로 정렬이 됨. 따라서 -x[1] 조건으로도 충분함
        result.extend([item[0] for item in sorted_album_to_play_items])
    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))