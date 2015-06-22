/**
 * Created by Jonathan on 21/06/2015.
 */
function message_Ask(type, text, callback) {
    var n = noty({
        text        : text,
        type        : type,
        dismissQueue: true,
        layout      : 'center',
        closeWith   : ['click'],
        theme       : 'relax',
        maxVisible  : 5,
        modal       : true,
        killer      : true,
        animation   : default_animation(),
        buttons     : [
        {addClass: 'btn btn-primary', text: 'Ok', onClick: function ($noty) {
            callback();
            $noty.close();
        }
        },
        {addClass: 'btn btn-danger', text: 'Cancel', onClick: function ($noty) {
            $noty.close();
        }
        }
        ]
    });
}
function message_Alert(type, text) {
    var n = noty({
        text        : text,
        type        : type,
        dismissQueue: true,
        killer      : true,
        layout      : 'top',
        closeWith   : ['click'],
        theme       : 'relax',
        maxVisible  : 5,
        animation   : default_animation()
    });
}

function default_animation(){
    return {
        open  : 'animated fadeInDown',
        close : 'animated fadeOutDown',
        easing: 'swing',
        speed : 500
    }
}