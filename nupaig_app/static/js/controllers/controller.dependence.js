/**
 * Created by Jonathan on 18/06/2015.
 */
appNUPAIG.controller('controller_dependence', [
    '$rootScope',
    '$scope',
    '$window',
    'request',
    'prev_page',
    'next_page',
    'page_count',
    function($rootScope, $scope, $window, request, prev_page, next_page, page_count) {
        $scope.model_dependence = {
            id_dependence: 0,
            dependence: ''
        };
        $scope.checked_dependence = [];

        $rootScope.namespaceurl ='/principal/api/v1/dependence/';
        $rootScope.url = $rootScope.namespaceurl + '?format=json';

        request();
        console.log('controller_dependence');

        $scope.get_nextpage = function(){
            next_page();
            console.log($rootScope.url);
        };

        $scope.get_prevpage = function(){
            prev_page();console.log($rootScope.url);
        };

        $scope.get_pagecount = function(){
            return page_count($rootScope.count, $rootScope.limit);
        };
        
        $scope.value_checked = function (pobj) {
            for (var i = 0, _len = $scope.checked_dependence.length; i < _len; i++) {
                if ($scope.checked_dependence[i].id === pobj.id)
                    return true;
            }
            return false;
        };

        $scope.toggleCheck = function(pobj){
            $rootScope.urledit= '/principal/update-dependence/' + pobj.id;
            if ($scope.checked_dependence.indexOf(pobj) === -1) {
                $scope.checked_dependence.push(pobj);
            } else {
                $scope.checked_dependence.splice($scope.checked_dependence.indexOf(pobj), 1);
            }
        };

}]);