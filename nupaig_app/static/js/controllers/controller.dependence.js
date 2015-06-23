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

        $scope.urldetail = get_url_detail('detail_dependence');
        $rootScope.urledit = get_url_update('update_dependence');
        $rootScope.namespaceurl = get_url_list('list_dependence');
        $rootScope.url = $rootScope.namespaceurl + '?format=json';

        request();



    }]);