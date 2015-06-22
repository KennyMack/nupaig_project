/**
 * Created by Jonathan on 18/06/2015.
 */

/* Make request in JSON format using GET*/
appNUPAIG.factory('request', ['$rootScope', '$http', function ($rootScope, $http) {
    return function (continuous) {
        return $http({
            url: $rootScope.url,
            method: "GET",
            headers: {'Content-Type': 'application/json'}
        }).success(function (data, status, headers, config) {
            if (continuous)
                $rootScope.objects = $rootScope.objects.concat(data.objects);
            else
                $rootScope.objects = data.objects;
            $rootScope.count = data.meta.total_count;
            $rootScope.prev = data.meta.previous;
            $rootScope.next = data.meta.next;
            $rootScope.limit = data.meta.limit;
        }).error(function (data, status, headers, config) {
            $rootScope.status = status + ' ' + headers;
        });
    };
}]).factory('next_page', ['$rootScope', 'request', function ($rootScope, request) {
    return function (continuous) {
        $rootScope.url = $rootScope.namespaceurl + $rootScope.next;
        if ($rootScope.next != null) {
            $rootScope.actualpage++;
            return request(continuous);
        }
    };
}]).factory('prev_page', ['$rootScope', 'request', function ($rootScope, request) {
    return function (continuous) {
        $rootScope.url = $rootScope.namespaceurl + $rootScope.prev;
        if ($rootScope.prev != null) {
            $rootScope.actualpage--;
            return request(continuous);
        }
    };
}]).factory('page_count', ['$window', function ($window) {
    return function (count, limit) {
        if (limit > 0)
            return $window.Math.ceil(count / limit);
        else
            return 1;
    };
}]).factory('get_data', ['$rootScope', '$http', function ($rootScope, $http) {
    return function (continuous) {
        return $http({
            url: $rootScope.url,
            method: "GET",
            headers: {'Content-Type': 'application/json'}
        }).success(function (data, status, headers, config) {
            if (continuous)
                $rootScope.data = $rootScope.data.concat(data);
            else
                $rootScope.data = data;
        }).error(function (data, status, headers, config) {
            $rootScope.status = status + ' ' + headers;
        });
    };
}]);

/* Make request using POST */
appNUPAIG.factory('PostRequest', ['$rootScope', '$http', '$cookies',  function ($rootScope, $http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    return function (pUrl, pData) {
        return $http({
            url: pUrl,
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            data: { data: pData }
        }).success(function (data, status, headers, config) {
            return data == 'ok';
        }).error(function (data, status, headers, config) {
            return false;
        });
    };
}]);