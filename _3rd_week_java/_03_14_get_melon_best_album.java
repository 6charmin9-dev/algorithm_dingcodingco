package _3rd_week_java;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class _03_14_get_melon_best_album {
    public static void main(String[] args) {
        System.out.print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ");
        printList(getMelonBestAlbum(
            new String[]{"classic", "pop", "classic", "classic", "pop"}, 
            new int[]{500, 600, 150, 800, 2500}));
        
        System.out.print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ");
        printList(getMelonBestAlbum(
            new String[]{"hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"}, 
            new int[]{2000, 500, 600, 150, 800, 2500, 2000}));
    }

    public static List<Integer> getMelonBestAlbum(String[] genres, int[] plays) {
        List<Integer> result = new ArrayList<>();
        Map<String, Integer> genreToTotalPlaysMap = new HashMap<>();
        Map<String, List<Song>> genreToSongsMap = new HashMap<>(); 
        for (int i=0; i<genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];
            genreToTotalPlaysMap.put(genre, genreToTotalPlaysMap.getOrDefault(genre, 0) + play);
            genreToSongsMap.putIfAbsent(genre, new ArrayList<>());
            genreToSongsMap.get(genre).add(new Song(genre, i, play));
        }
        List<String> sortedGenres = genreToTotalPlaysMap.entrySet().stream()
            .sorted((e1, e2) -> e2.getValue().compareTo(e1.getValue()))
            .map(Map.Entry::getKey)
            .collect(Collectors.toList());
        for (String genre : sortedGenres) {
            List<Song> songs = genreToSongsMap.get(genre);
            List<Song> sortedSongs = songs.stream()
                .sorted((s1, s2) -> {
                    if (s1.playCount != s2.playCount) {
                        return s2.playCount - s1.playCount;
                    } else {
                        return s1.idx - s2.idx;
                    }
                })
                .limit(2)
                .collect(Collectors.toList());
            result.addAll(sortedSongs.stream().map(s -> s.idx).collect(Collectors.toList()));
        }
        return result;
    }

    public static void printList(List<?> list) {
        System.out.println(list);
    }

    public static class Song {
        String genre;
        int idx;
        int playCount;

        public Song(String genre, int idx, int playCount) {
            this.genre = genre;
            this.idx = idx;
            this.playCount = playCount;
        }
    }
}
