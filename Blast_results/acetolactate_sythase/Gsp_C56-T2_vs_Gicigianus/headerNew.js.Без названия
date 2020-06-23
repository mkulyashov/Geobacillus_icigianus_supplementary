

        // add a back_url to a#myncbi's href
        /*
        var acctLinks = document.querySelectorAll('#account_login, #account_logout');
        for (var i = 0; i < acctLinks.length; i++) {
            acctLinks[i].href = acctLinks[i].href + '?back_url=' + document.location.href;
        }
        */
        var cubby = getCookie('WebCubbyUser');
        cubby = decodeURIComponent(decodeURIComponent(cubby));

        var username = getUser(cubby);

        if (username) {
            jQuery('#uname_short').text(username.trunc(20));
            jQuery('#uname_long').text(username.trunc(40));
            jQuery('#account_login').hide();
            jQuery('#account_info').show();
        }
        else {
            jQuery('#account_login').show();
            jQuery('#account_info').hide();
        }


        function getUser(c) {

            var re_logd = /.*logged-in\=(\w*);.*/;
            var re_user = /.*my-name\=([\w|\-|\.|\ |\@|\+]*);.*/;
            if (c) {
                var l = re_logd.exec(c);
                if (l && l[1] && l[1] === 'true') {
                    var u = re_user.exec(c);
                    if (u && u[1]) {
                        return u[1];
                    }
                }
            }
            return '';
        }


        function getCookie(f) {
            var e;
            if (window.sessionStorage) {
                try {
                    e = sessionStorage.getItem(f) || '';
                } catch (g) {
                    e = '';
                }
                if (e.length > 0) {
                    return e;
                }
            }
            if (document.cookie.length > 0) {
                e = document.cookie.indexOf(f + '=');
                if (e !== -1) {
                    e = e + f.length + 1;
                    f = document.cookie.indexOf(';', e);
                    if (f === -1) {
                        f = document.cookie.length;
                    }
                    return unescape(document.cookie.substring(e, f))
                }
            }
            return '';
        }

        var $popupMenu = jQuery('#account_info').ncbipopup();

    