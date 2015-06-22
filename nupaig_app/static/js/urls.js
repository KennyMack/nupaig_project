/**
 * Created by Jonathan on 21/06/2015.
 */
function get_url_update(p){
    var router = {
        'update_dependence' : '/principal/update-dependence/'
    };
    return (router[p]);
}

function get_url_delete(p){
    var router = {
        'delete_dependence' : '/principal/delete-all-dependence/'
    };
    return (router[p]);
}

function get_url_list(p){
    var router = {
        'list_dependence': '/principal/api/v1/dependence/'
    };
    return (router[p]);
}

function get_url_detail(p){
    var router = {
        'detail_dependence': '/principal/detail-dependence/'
    };
    return (router[p]);
}
