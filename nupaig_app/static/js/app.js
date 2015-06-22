/**
 * Created by Jonathan on 18/06/2015.
 */
var appNUPAIG = angular.module('appNUPAIG',['ngCookies'], function($interpolateProvider){
        // Conturns the problem with django interpolation
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });