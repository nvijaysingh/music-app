console.log("asdfghjkqwertyuiop");
function audioPlay(song_id) {
         var song = document.getElementById(song_id);
         document.getElementById('songDetail').innerHTML = "<h3>Now Playing "+song.innerHTML+"</h3>";


}
function giveUrl(song_url) {
    var url = document.getElementById('url');
    var audio = document.getElementById('audio');
   url.src="../../"+song_url;
    audio.load();
    audio.play();

}

var app = angular.module('myApp',[]);

angular.module('myApp')
.service('customHttp', ['$http', function ($http) {

  this.request = function(impParams, requestLink, type, callback){
    if(type == 'GET'){
        requestLink = requestLink+'?'+impParams; //To search using the important parameters by $stateParams
        impParams = '';
      }
      else{
        //As it is
      }
      $http({
        method : type,
        url : requestLink,
        data : impParams,
        headers : {
          "Content-Type": 'application/x-www-form-urlencoded'
        }
      })
      .success(function(data, status, headers, config){
        callback(data);
      })
      .error(function(data, status, headers, config) {
        //console.log('HTTP request failed!');
        // Materialize.toast('Sorry! There occurred some error', 2000);
      });
    }
  }])
app.controller('faqCtrl', function($scope,customHttp,$timeout,$window,$location) {
    console.log("inside faq ctrl");



    $scope.submit = function () {
        console.log("here are you");

        console.log($scope.album);
        var params = JSON.stringify($scope.album);
        customHttp.request(params,'/music/addAlbum','POST', function (data) {
                    if(data){
                      if(data.status = 'success')
                      {
                        document.getElementById('myModal').style.display = 'none';
                        document.getElementById('indexPage').style.opacity = '1';
                        $scope.message_update = true;
                        $timeout(function () { $scope.message_update =false;},2000);
                        }

                    }
                  });
    };



});

