// main.js for Music RecommeNDer
// Ana Luisa Lamberto

// Transform Words from Database Format to Readable Format
function formatting(word){
    var name = word.split("-");
    for (var i = 0; i < name.length; i++){
        var newLetter = name[i][0].toUpperCase();
        name[i] = name[i].replace(name[i][0], newLetter);
    }
    return name.join(" ");
}

// Transform Words from Readable Format to Database Format
function unformat(word){
    var name = word.split(" ");
    for (var i = 0; i < name.length; i++){
        var newLetter = name[i][0].toLowerCase();
        name[i] = name[i].replace(name[i][0], newLetter);
    }
    return name.join("-");
}

// Clear All Labels on Screen Between Searches
function clear(args){
    args[1].innerHTML = "";
    args[2].innerHTML = "";
    args[3].innerHTML = "";
    args[4].innerHTML = "";
    args[5].innerHTML = "";
    args[6].innerHTML = "";
    args[7].innerHTML = "";
    args[8].innerHTML = "";
    args[9].innerHTML = "";
    args[10].innerHTML = "";
    args[11].innerHTML = "";
    args[12].innerHTML = "";
    document.getElementById("addBarTitle").innerHTML = "";
    document.getElementById("addBarYear").innerHTML = "";
    document.getElementById("addBarArtist").innerHTML = "";
    document.getElementById("addBarGenre").innerHTML = "";
    document.getElementById("addBarLyrics").innerHTML = "";
    document.getElementById("deleteBar").innerHTML = "";    
}

// Perform Get Requests for Title and Recommendations
function findTitle(args){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://student04.cse.nd.edu:52072/songs/"+args[0], true);
    xhr.onload = function(e){
        var songResponse = JSON.parse(xhr.responseText);
        if(songResponse.result == "success"){
            args[1].style.width = "350px";
            args[1].innerHTML += "Title: " + formatting(songResponse.song) + " (" + songResponse.year + ')<br><br>';
            args[1].innerHTML += "Artist: " + formatting(songResponse.artist) + "<br>Search: (" + songResponse.artist + ")<br><br>";
            args[1].innerHTML += "Genre: " + songResponse.genre;
            args[2].innerHTML = songResponse.lyrics;
            
            var xhr2 = new XMLHttpRequest();
            xhr2.open("GET", "http://student04.cse.nd.edu:52072/recommendations/songs/"+args[0], true);
            xhr2.onload = function(e){
                var responseRec = JSON.parse(xhr2.responseText);
                var recs = [];
                for (var i = 0; i < 10; i++){
                    var song = responseRec.song_recommendations[i];
                    recs.push(song);
                }
                
                args[3].innerHTML = formatting(recs[0]) + " (Search: " + recs[0] + ")";
                args[4].innerHTML = formatting(recs[1]) + " (Search: " + recs[1] + ")";
                args[5].innerHTML = formatting(recs[2]) + " (Search: " + recs[2] + ")";
                args[6].innerHTML = formatting(recs[3]) + " (Search: " + recs[3] + ")";
                args[7].innerHTML = formatting(recs[4]) + " (Search: " + recs[4] + ")";
                args[8].innerHTML = formatting(recs[5]) + " (Search: " + recs[5] + ")";
                args[9].innerHTML = formatting(recs[6]) + " (Search: " + recs[6] + ")";
                args[10].innerHTML = formatting(recs[7]) + " (Search: " + recs[7] + ")";
                args[11].innerHTML = formatting(recs[8]) + " (Search: " + recs[8] + ")";
                args[12].innerHTML = formatting(recs[9]) + " (Search: " + recs[9] + ")";
            }
            xhr2.send(null);
            
        }
        else{
            clear(args);
            alert("This Title Was Not Found.");
        }
    }
    xhr.send(null);
}

// Perform GET Requests for Artists and Recommendations
function findArtist(args) {
    args[1].style.width = "700px";
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://student04.cse.nd.edu:52072/artists/"+args[0], true);
    xhr.onload = function(e){
        var songResponse = JSON.parse(xhr.responseText);
        if(songResponse.result == "success"){
            args[1].innerHTML += "Artist: " + formatting(songResponse.artist) + '<br><br>';
            args[1].innerHTML += "Genre: " + songResponse.genre + "<br><br>";
            args[1].innerHTML += "Songs: <br><br>";
            for(var i = 0; i < songResponse.songs.length; i++){
                args[1].innerHTML += formatting(songResponse.songs[i]) + " (Search: " + songResponse.songs[i] + ")<br>";
            }
            args[2].innerHTML = "";
            
            var xhr2 = new XMLHttpRequest();
            xhr2.open("GET", "http://student04.cse.nd.edu:52072/recommendations/artists/"+args[0], true);
            xhr2.onload = function(e){
                var responseRec = JSON.parse(xhr2.responseText);
                var recs = [];
                for (var i = 0; i < 10; i++){
                    var song = responseRec.artist_recommendations[i];
                    recs.push(song);
                }
                
                args[3].innerHTML = formatting(recs[0]) + " (Search: " + recs[0] + ")";
                args[4].innerHTML = formatting(recs[1]) + " (Search: " + recs[1] + ")";
                args[5].innerHTML = formatting(recs[2]) + " (Search: " + recs[2] + ")";
                args[6].innerHTML = formatting(recs[3]) + " (Search: " + recs[3] + ")";
                args[7].innerHTML = formatting(recs[4]) + " (Search: " + recs[4] + ")";
                args[8].innerHTML = "";
                args[9].innerHTML = "";
                args[10].innerHTML = "";
                args[11].innerHTML = "";
                args[12].innerHTML = "";
            }
            xhr2.send(null);
            
        }
        else{
            clear(args);
            alert("This Artist Was Not Found");
        }
    }
    xhr.send(null);

}

// Perform Search When SEARCH Button is Clicked
function performSearch() {
    
    // Search Bar and Dropdown Values
    var searched = document.getElementById("bar").value;
    var chosen = document.getElementById("drop").value;
    
    // All Changeable Labels
    var result = document.getElementById("display");
    var L = document.getElementById("lyrics");
    var song1 = document.getElementById("rec1");
    var song2 = document.getElementById("rec2");
    var song3 = document.getElementById("rec3");
    var song4 = document.getElementById("rec4");
    var song5 = document.getElementById("rec5");
    var song6 = document.getElementById("rec6");
    var song7 = document.getElementById("rec7");
    var song8 = document.getElementById("rec8");
    var song9 = document.getElementById("rec9");
    var song10 = document.getElementById("rec10");
    
    args = [searched, result, L, song1, song2, song3, song4, song5, song6, song7, song8, song9, song10];
    
    result.innerHTML = "";
    
    if (chosen == "title"){
        findTitle(args);
    }
    else if (chosen == "artist"){
        findArtist(args);
    }
}

// Add Song To Database Using a Modal
function addSong(){
    var modal = document.getElementById('addPopUp');
    var span = document.getElementsByClassName("close")[0];
    modal.style.display = "block";
    

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

// Delete Song From Database Using a Modal
function deleteSong(){
    var modal = document.getElementById('deletePopUp');
    var span = document.getElementsByClassName("close")[0];
    modal.style.display = "block";

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

// Close Delete Modal When Enter Clicked
function closePopUpDelete() {
    var toDelete = document.getElementById("deleteBar").value;
    
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", "http://student04.cse.nd.edu:52072/songs/"+toDelete, true);
    xhr.onload = function(e){
        var response = JSON.parse(xhr.responseText);
        alert(xhr.responseText);
        if(response.result == "success"){
            alert("Song Was Successfully Deleted");
        }
        else{
            alert("Error: Song Was Not Deleted");
        }
    }
    xhr.send(null);
    
    var modal = document.getElementById("deletePopUp");
    modal.style.display = "none";
    clear();
}

// Close Add Modal When Enter Clicked
function closePopUpAdd() {
    var title = unformat(document.getElementById("addBarTitle").value);
    var year = document.getElementById("addBarYear").value;
    var genre = document.getElementById("addBarGenre").value;
    var artist = unformat(document.getElementById("addBarArtist").value);
    var lyrics = document.getElementById("addBarLyrics").value;
    var newSong = {"year" : year, "artist": artist, "genre" : genre, "lyrics" : lyrics};
    var json = JSON.stringify(newSong);
    
    var xhr = new XMLHttpRequest();
    xhr.open("PUT", "http://student04.cse.nd.edu:52072/songs/"+title, true);
    xhr.onload = function(e){
        var response = JSON.parse(xhr.responseText);
        if(response.result == "success"){
            alert("Song Was Successfully Added");
        }
        else{
            alert("Error: Song Was Not Added");
        }
    }
    xhr.send(json);

    var modal = document.getElementById("addPopUp");
    modal.style.display = "none";
    clear();
}

// Reset Database when RESET Button Clicked
function reset(){
    var xhr = new XMLHttpRequest();
    xhr.open("PUT", "http://student04.cse.nd.edu:52072/reset/", true);
    xhr.onload = function(e){
        var response = JSON.parse(xhr.responseText);
        if(response.result == "success"){
            alert("Database Reset");
        }
        else{
            alert("Error: Database Not Reset");
        }
    }
    xhr.send(null);
}


