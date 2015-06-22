/**
 * Created by Jonathan on 18/06/2015.
 */
appNUPAIG.controller('controller_dependence', [
    '$rootScope',
    '$scope',
    '$window',
    'request',
    function ($rootScope, $scope, $window, request) {
        $scope.model_dependence = {
            id_dependence: 0,
            dependence: ''
        };
        $rootScope.urledit = get_url_update('update_dependence');
        $rootScope.namespaceurl = get_url_list('list_dependence');// '/principal/api/v1/dependence/';
        $rootScope.url = $rootScope.namespaceurl + '?format=json';

        request();

        $scope.urldetail = get_url_detail('detail_dependence');



        /*
        $scope.value_checked = function (pobj) {
            for (var i = 0, _len = $rootScope.selectedlist.length; i < _len; i++) {
                if ($scope.selectedlist[i].id === pobj.id)
                    return true;
            }
            return false;
        };

        $scope.toggleCheck = function (pobj) {
            if ($rootScope.selectedlist.indexOf(pobj) === -1) {
                $rootScope.selectedlist.push(pobj);
            } else {
                $rootScope.selectedlist.splice($rootScope.selectedlist.indexOf(pobj), 1);
            }
            var count = $rootScope.selectedlist.length;
            if (count > 0){
                $rootScope.urledit = get_url_update('update_dependence') + $rootScope.selectedlist[count-1].id;
            }
            else
                $rootScope.urledit = '';
        };*/

    }]);