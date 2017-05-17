/**
 * Created by vijju on 14-05-2017.
 */
function audioPlay(song_id) {
         var song = document.getElementById(song_id)
         document.getElementById('songDetail').innerHTML = "<h3>Now Playing "+song.innerHTML+"</h3>"


}
function giveUrl(song_url) {
    var url = document.getElementById('url')
    var audio = document.getElementById('audio')
   url.src="../../"+song_url
    audio.load()
    audio.play()
}