function goToBlastAlign(e, dipsGi, winname) {
    url = $("blastCgiUrl").value;
    url += "#" + dipsGi;

    $("giForAlign").value = dipsGi;
    blastAlignWin = window.open(url, winname);
    blastAlignWin.postMessage(dipsGi, location.origin);

    blastAlignWin.focus();  // give focus 
    utils.preventDefault(e);
}

function goToOrgReport(e, taxid) 
{
    jQuery("#showOrg").ncbitoggler("open");    
    location.href = "#" + taxid;        
    utils.preventDefault(e);
}

function ViewSeqsInEntrez(e, taxidList,elem) 
{
    var taxIdArray = taxidList.split(",");
    if (taxIdArray.length == 1) {
        if ($("txForSeq_" + taxidList)) {
            $("selSeqs").value = $("txForSeq_" + taxidList).value;
        }
    }
    else {
        jQuery("#txToSeqsMap").find(".txForSeq").each(function (index) {
            var taxid = jQuery(this).attr("id").replace("txForSeq_", "");
            if (taxIdArray.indexOf(taxid) != -1) {
                if ($("selSeqs").value != "") $("selSeqs").value += ",";
                $("selSeqs").value += this.value;
            }
        });
    }
    if ($("selSeqs").value != "") {
        var submitForm = $("submitterTop");
        submitForm.target = elem.target;
        submitForm.submit();
        $("selSeqs").value = "";
    }
    utils.preventDefault(e);
}

function GetTaxResultsForQuery()
{
    form = $("multiQuery");    
    $("qIndex").value = $("queryList")[$("queryList").selectedIndex].value;
    form.submit();
}

function toggleTaxRow(e) 
{
    var chClass = this.id.replace("txr", "partx");
    var hide;    
    if (jQuery(this).hasClass("showing")) {
        hide = true;
        jQuery(this).removeClass("showing");
    }
    else {
        hide = false;
        jQuery(this).addClass("showing");
    }
    var showOrHide = (hide) ? "Show" : "Hide";
    jQuery(this).attr("title",showOrHide + jQuery(this).attr("title").slice(4));
    jQuery("#taxTable").find("." + chClass).each(function (index) {
        if (hide) {
            jQuery(this).hide();
        }
        else {
            var parTaxid = jQuery(this).attr("parTaxid");
            if(jQuery(parTaxid).hasClass("showing") && !jQuery(parTaxid).is(":hidden")) {
                jQuery(this).show();
            }
        }
    });
    utils.preventDefault(e);
}


function LoadPage()
{    
    if($("queryList")) {
       jQuery("#queryList").bind("change",GetTaxResultsForQuery);  
    }
    jQuery("#taxTable").find(".jtg").each(function (index) {
        jQuery(this).bind("click", toggleTaxRow);
            
    });
}

//If not ADV_VIEW - there is no button #btnTaxn:
if(!$("btnTaxn")) utils.addEvent(window,"load", LoadPage, false);

