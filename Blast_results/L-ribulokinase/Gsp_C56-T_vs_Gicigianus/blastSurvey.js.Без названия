function get_meta_value(name) 
{
    var meta = document.querySelector("meta[name='" + name + "']"),
        v = '';
    if (meta !== null && meta.getAttribute('content') !== null) {
        v = meta.getAttribute('content');
    }
    return encodeURIComponent(v);
}

jQuery('body').on('click', 'a.smcx-btn-primary', function (e) {    
    var params = [];
    var oldHref = jQuery(this).attr('href');

    var pdid = get_meta_value('ncbi_pdid');
    


    params.push('a=' + get_meta_value('ncbi_app'));
    params.push('from=' + encodeURIComponent(document.location)); // encode the entire URI, see SEQUI-47
    params.push('p=' + pdid);
    params.push('s=' + get_meta_value('ncbi_sessionid'));
    
    params.push('db=' + get_meta_value('ncbi_db'));
    params.push('prog=' + get_meta_value('ncbi_program'));
    params.push('algorithm=' + get_meta_value('ncbi_algorithm'));
    

    if (params.length) {
        jQuery(this).attr('href', oldHref + '?' + params.join('&'))
    }

    window.open(jQuery(this).attr('href'), '_blank');
    return false;
});

function displayResultsPageSurvey(surveyID) 
{    
    eval("(function (t, e, s, o) { var n, a, c; t.SMCX = t.SMCX || [], e.getElementById(o) || (n = e.getElementsByTagName(s), a = n[n.length - 1], c = e.createElement(s), c.type = \"text/javascript\", c.async = !0, c.id = o, c.src = [\"https:\" === location.protocol ? \"https://\" : \"http://\", \"widget.surveymonkey.com/collect/website/js/" + surveyID + ".js\"].join(\"\"), a.parentNode.insertBefore(c, a)) })(window, document, \"script\", \"smcx-sdk\");"); 
}