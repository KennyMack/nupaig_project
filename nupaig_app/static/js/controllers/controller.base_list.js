/**
 * Created by Jonathan on 20/06/2015.
 */
appNUPAIG.controller('controller_gridview', [
    '$rootScope',
    '$scope',
    function($rootScope, $scope){
        $scope.edit_button = function(){
            window.location = $rootScope.urledit;
        }
    }
]);