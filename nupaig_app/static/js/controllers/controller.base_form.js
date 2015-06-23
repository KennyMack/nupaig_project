/**
 * Created by Jonathan on 22/06/2015.
 */
appNUPAIG.controller('controller_base_form', [
    '$rootScope',
    '$scope',
    function($rootScope, $scope){
        $scope.url_location = function(purl){
             window.location = purl;
         };

         /*$scope.url_delete = function(purldelete, purllist){
             message_Ask('alert', 'Deseja excluir ?', function () {
                 if (PostRequest(purldelete, '')) {
                     window.location = purllist;
                 }
             });
         };*/
    }
]);