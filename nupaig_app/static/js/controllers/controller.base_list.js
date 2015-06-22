/**
 * Created by Jonathan on 20/06/2015.
 */
'use strict';
appNUPAIG.controller('controller_base_list', [
    '$rootScope',
    '$scope',
    '$filter',
    'PostRequest',
    'request',
    'prev_page',
    'next_page',
    'page_count',
    function($rootScope, $scope,  $filter, PostRequest, request, prev_page, next_page, page_count){
        $scope.gridview ={
            checkall : false
        };
        $scope.listsel = [];
        $scope.edit_button = function(){
            $scope.listsel =($filter('filter')($rootScope.objects, {'check': true}));
            if ($rootScope.urledit != '')
                window.location = $rootScope.urledit + $scope.listsel[$scope.listsel.length-1].id;
            else
                message_Alert('alert', 'Selecione um registro');
        };

        $scope.delete_button = function(){
            if($rootScope.objects.length > 0) {
                message_Ask('alert', ($filter('filter')($rootScope.objects, {'check': true}))+ 'Deseja excluir ?', function () {
                    angular.forEach($rootScope.objects, function (value, key) {
                        if (value.check) {
                            if (PostRequest(get_url_delete('delete_dependence') + value.id.toString(), '')) {
                                //$scope.remove_Row(value);
                                $rootScope.objects.splice($rootScope.objects.indexOf(value), 1);
                            }
                        }
                    });
                });
            }
            else
                message_Alert('alert', 'Selecione um registro');
        };

        $scope.check_all = function() {
            angular.forEach($rootScope.objects, function (value) {
                value.check = $scope.gridview.checkall;
            });
        };

        $scope.get_nextpage = function () {
            $scope.gridview.checkall = false;
            next_page();
        };

        $scope.get_prevpage = function () {
            $scope.gridview.checkall = false;
            prev_page();
        };

        $scope.get_pagecount = function () {
            return page_count($rootScope.count, $rootScope.limit);
        };
    }
]);