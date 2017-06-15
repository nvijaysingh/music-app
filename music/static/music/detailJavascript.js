console.log("asdfghjkqwertyuiop");
function audioPlay(song_id) {
         var song = document.getElementById(song_id);
         document.getElementById('songDetail').innerHTML = "<h3>Now Playing "+song.innerHTML+"</h3>";


}
function giveUrl(song_url) {
    var url = document.getElementById('url');
    console.log(song_url);
    var audio = document.getElementById('audio');
   url.src=song_url;
    audio.load();
    audio.play();

}
var app = angular.module('myApp',[]);
app.directive('bindFile', [function () {
    return {
        require: "ngModel",
        restrict: 'A',
        link: function ($scope, el, attrs, ngModel) {
            el.bind('change', function (event) {
                ngModel.$setViewValue(event.target.files[0]);
                $scope.$apply();
            });

            $scope.$watch(function () {
                return ngModel.$viewValue;
            }, function (value) {
                if (!value) {
                    el.val("");
                }
            });
        }
    };
}]);

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




    // $scope.submit = function () {
    //     console.log("here are you");
    //     var data = new FormData();
    //     var image = $('#imagefile')[0].files[0];
    //     console.log(image);
    //     // var image = $scope.album.logo;
    //     data.append('img',image);
    //     console.log(data);
    //     var params = $scope.album;
    //     // console.log(params);
    //     customHttp.request(data,'/music/addAlbum','POST', function (data) {
    //                 if(data){
    //                   if(data.status = 'success')
    //                   {
    //                     document.getElementById('myModal').style.display = 'none';
    //                     document.getElementById('indexPage').style.opacity = '1';
    //                     $scope.message_update = true;
    //                     $timeout(function () { $scope.message_update =false;},2000);
    //                     }

    //                 }
    //               });
    // };



      $scope.submitsong = function () {
        console.log("here are you");
        $scope.song.url = "/media/"+$scope.song.file.name;
        console.log($scope.song);
        var params = $scope.song;
        customHttp.request(params,'/music/addSong','POST', function (data) {
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

    var time = 0;

    $scope.playall =function () {

        console.log("here");
        var params = "abc";
        customHttp.request(params, '/music/get_ids', 'GET', function (data) {
            if (data) {
                $scope.keys = data.list;

             var items = $scope.keys;
             $scope.pk =items[Math.floor(Math.random() *items.length)];

                var param = "id=" + $scope.pk;
        console.log(param);
        customHttp.request(param, '/music/get_all_songs', 'GET', function (data) {
            if (data) {
                console.log(data);
                $scope.song = data.list[0];
                console.log($scope.song);
                 document.getElementById('songDetail').innerHTML = "<h3>Now Playing "+$scope.song.pk+". "+$scope.song.name+"</h3>";
               var url = document.getElementById('url');
               var audio = document.getElementById('audio');
                url.src=$scope.song.song;
                console.log(url);
                audio.load();
               audio.play();
               time = audio.duration;
            }
        });
        var audio = document.getElementById('audio');
        
               console.log(time);
         setInterval(function(){
                $scope.pk = items[Math.floor(Math.random() *items.length)];
                var params = "id=" + $scope.pk;
                customHttp.request(params, '/music/get_all_songs', 'GET', function (data) {
                    if (data) {
                        console.log(data);
                        $scope.song = data.list[0];
                        console.log($scope.song);
                        document.getElementById('songDetail').innerHTML = "<h3>Now Playing "+$scope.song.pk+". "+$scope.song.name+"</h3>";
                        var url = document.getElementById('url');
                       audio = document.getElementById('audio');
                        url.src = "../../" + $scope.song.song;
                        audio.load();
                        audio.play();
                        time = audio.duration;
                        console.log(time);
                    }
                });
            } , 240000);

            }
        });


    };

       $scope.getalbums2 = function () {
        console.log("here are you");

         var params = "id=" + $scope.pk;
         console.log(params);
        customHttp.request(params, '/music/get_all_album', 'GET', function (data) {
            if (data) {
                console.log(data);
                $scope.albumlist1 = data.list[0];
                console.log($scope.albumlist1);
            }
        });
       };


});

