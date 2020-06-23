// JScript source code

//Display Reformat page button only after the whole page is loaded    

function ReformatPageEvent()
{
	var refPageLink = document.getElementById("refPage");    	
	
	//alert(refPageLink);
	//alert(refPageLink.getAttribute("submitForm"));
	var submitForm = refPageLink.getAttribute("submitForm");
	alert(submitForm);
	if(refPageLink && submitForm) {
		utils.addEvent(refPageLink, 
					   "click", 
					   function() {
							document.getElementById(submitForm).submit();					
						}, 
						false);    
	}	
}


function SubmitEvent(linkID)
{
	
	var link = document.getElementById(linkID);    	
	//alert(link.getAttribute("submitForm"));
	var submitForm = link.getAttribute("submitForm");
	if(link && submitForm) {
		utils.addEvent(link, 
					   "click", 
					   function() {							
							document.getElementById(submitForm).submit();					
						}, 
						false);    
	}	
}


function SubmitEventSave(linkID)
{
	
	var link = document.getElementById(linkID);    	
	//alert(link.getAttribute("submitForm"));
	var submitForm = link.getAttribute("submitForm");
	if(link && submitForm) {
		utils.addEvent(link, 
					   "click", 
					   function() {
							//$(submitForm).CMD.value = "GetSaved";							
							document.getElementById(submitForm).submit();					
						}, 
						false);    
	}	
}

//This function creates submit form event on click
//form submitted is defined in submitForm attribute
//It also copies params from forms[0] (search paramateres) created by formatter
function SubmitEventNew(linkID)
{
	
	var link = document.getElementById(linkID);    	
	//alert(link.getAttribute("submitForm"));
	if(!link) return;
	var submitForm = link.getAttribute("submitForm");
	if(link && submitForm) {
	    utils.addEvent(link,
					   "click",
					   function () {

					       if ($(submitForm).CMD) {
					           document.forms[0].CMD.value = $(submitForm).CMD.value;
					       }
					       if (document.forms[0].SESSION_ID) {					           
					           jQuery(document.forms[0].SESSION_ID).remove();        
					       }
					       var pageTypeEl = $(submitForm).PAGE_TYPE;
					       if (pageTypeEl) {
					           if (!document.forms[0].PAGE_TYPE) {
					               document.forms[0].appendChild(pageTypeEl);
					           }
					           else {
					               document.forms[0].PAGE_TYPE.value = $(submitForm).PAGE_TYPE.value;
					           }
					       }
					       var formObj = document.forms[0].FORMAT_OBJECT;
					       if (formObj) {
					           if (formObj.length > 1) formObj = formObj[0];
					           if ($(submitForm).FORMAT_OBJECT) formObj.value = $(submitForm).FORMAT_OBJECT.value;					           
					       }
					       var form = $(submitForm);
					       form.innerHTML = document.forms[0].innerHTML + form.innerHTML;
					       form.submit();
					   },
						false);    
	}	
}

function GetResults()
{
    form = $("results");
    form.QUERY_INDEX.value = $("queryList")[$("queryList").selectedIndex].value;
    if (form.SESSION_ID) jQuery(form.SESSION_ID).remove();            
    form.submit();   
}

function isIdIn(id, idArray){
  var idSeen=false;

  for(i=0; i<idArray.length; i++){
    if(id==idArray[i]){
      idSeen=true;
      break;
    }
  }
  return idSeen;
}

function GetSelectedSeqString(formName)
{
    var selSeqs = "";
    var idArray=new Array();
    forms = document.getElementsByName(formName);    
    for(var j=0; j < forms.length; j++){
      for(var i=0; i < forms[j].elements.length; i++){
        var theElem=forms[j].elements[i];
        if(theElem.type=="checkbox"&&theElem.name=="getSeqGi"&&theElem.checked){      
          if(!isIdIn(theElem.value, idArray)){            
            idArray[idArray.length]=theElem.value;
          }            
        }      
      }
    }
    selSeqs = idArray.join();
    return selSeqs;
}



function ViewSelectedSeqs(e)
{
    var submitForm = $("submitterTop");
    var targetForm = submitForm.getAttribute("seqsForm");
    $("selSeqs").value = GetSelectedSeqString(targetForm);
    submitForm.submit();
    utils.preventDefault(e);
}

function ViewSelectedSeqGraph(e) {
    var submitForm = $("submitterTop");
    var targetForm = submitForm.getAttribute("seqsForm");
    var seqList = $("selSeqs").value = GetSelectedSeqString(targetForm);
    SubmitToSeqViewer(e, seqList); 
}


function ViewSelectedSeqTree()
{
    var submitForm = $("treesubmitterTop");
    var targetForm = submitForm.getAttribute("seqsForm");
    $("seqSet").value = GetSelectedSeqString(targetForm);
    $("scrWidth").value = screen.width;
    $("scrHeight").value = screen.height;
    submitForm.submit();
    utils.preventDefault(e);
}

function ViewTree(linkID) {
    link = document.getElementById(linkID);
    var target = link.target;
    winRef = window.open(link.href + "&screenWidth=" + screen.width + "&screenHeight=" + screen.height, target);
}

function ViewSelectedSeqMultiAlign()
{
    var submitForm = $("multisubmitterTop");
    var targetForm = submitForm.getAttribute("seqsForm");
    $("seqSetM").value = GetSelectedSeqString(targetForm);    
    submitForm.submit();
}



function selectAllSeqs() 
{
    var selNum = 0;
    var g_SelectedIDsString = "";    
    var formName = this.getAttribute("seqsForm");
    forms = document.getElementsByName(formName);    
    for(var j=0; j < forms.length; j++){
        for(var i=0; i < forms[j].elements.length; i++){    
            var theElem=forms[j].elements[i];
            if(theElem.type=="checkbox"&&theElem.name=="getSeqGi"){
                theElem.checked = this.checked;
                if (this.checked && g_SelectedIDsString.indexOf(theElem.value) == -1) {
                    g_SelectedIDsString += " " + theElem.value;
                    selNum++;
                }
            }
        }
    }
    if ($("slcAlNum")) enableDescrLinks(selNum, "topSeqLinks", "slcAlNum");
    links = document.getElementsByName("selectAll");
    for(var i=0; i < links.length;i++) {
        if(links[i] != this)  links[i].checked = this.checked;
    }       
}


function InitSeqAlignLinks()
{
    var links = document.getElementsByName("getSeqs");
    for(var i=0; i < links.length;i++) {
        utils.addEvent(links[i],"click",ViewSelectedSeqs,false);
    }
    var links = document.getElementsByName("graphSeqs");
    for (var i = 0; i < links.length; i++) {
        utils.addEvent(links[i], "click", ViewSelectedSeqGraph, false);
    }

    links = document.getElementsByName("treeView");
    for(var i=0; i < links.length;i++) {
        utils.addEvent(links[i],"click",ViewSelectedSeqTree,false);  
    }    
    links = document.getElementsByName("mltiAln");
    for(var i=0; i < links.length;i++) {
        utils.addEvent(links[i],"click",ViewSelectedSeqMultiAlign,false);  
    }        
    links = document.getElementsByName("selectAll");
    for(var i=0; i < links.length;i++) {
        utils.addEvent(links[i],"click",selectAllSeqs,false);  
    }   
    
    if($("showAlign"))
        utils.addEvent($("showAlign"),"click",showHideLinks,false);  
}

function InitDownLoad()
{
    var diThresh = getHiddenFieldVal("DI_THRESH");
    var stepNumber = getHiddenFieldVal("STEP_NUMBER");
    var deltaBlast = (diThresh && diThresh != "") ? true : false;
    if (!deltaBlast && stepNumber != undefined) {
        if(stepNumber == "" || stepNumber < 2) {        
            jQuery("#dnPSSMPar").hide();        
        }
    }    
}
function Reformat(e)
{
    if(utils.hasClass($("FormatForm").FORMAT_ORGANISM,"orgHint"))  $("FormatForm").FORMAT_ORGANISM.value = "";        
    $("FormatForm").submit();    
}
function InitCustomButton(bn)
{
  utils.addEvent(bn, "mouseover", function() {this.src = this.getAttribute("mouseovImg");}, false);
  utils.addEvent(bn, "mouseout", function() {this.src = this.getAttribute("mouseoutImg");}, false);
  utils.addEvent(bn, "mousedown", function() {this.src = this.getAttribute("mousedownImg");}, false);
  utils.addEvent(bn, "mouseup", function() {this.src = this.getAttribute("mouseupImg");}, false);    
}

function InitAllCustomButtons()
{
    if($("go")) InitCustomButton($("go"));
    if($("dn")) InitCustomButton($("dn"));
    if($("onPageReformat")) InitCustomButton($("onPageReformat"));    
}
function showHideLinks()
{
    var links = document.getElementsByName("selectAll");
    for(var i=0; i < links.length;i++) {
        //This is done since IE does not recognize getElementsByName for span elem
        var allLinks = utils.getParent(links[i]);
        var removeClass,addClass;
        if(utils.hasClass(allLinks,"shownInl")) {        
            removeClass="shownInl";    
            addClass="hidden";        
        }
        else {
            removeClass="hidden";
            addClass="shownInl";        
        }    
        utils.removeClass(allLinks,removeClass);
        utils.addClass(allLinks,addClass);   
    }
}
/*remove this function */
function InitHelpLinks()
{
    for(var i=1; i <= 11;i++) {           
        InitToggleEvent($("hlp" + i));      
    }
}
//This function is used for collapsible deflines onmouseover="showInfo(this)"
//Initialized in showdefline.cpp
function showInfo(elem)
{
    var targetElem = $("info_" + elem.id);
    if(!targetElem) return;
    if(elem.getAttribute("init") == "on") return;
    
    Toggle.addTarget(elem, targetElem);  
    elem.setAttribute("init","on");    
}

function InitPsiBlast()
{
    //utils.addEvent($("ttt"),"keyup",SetHitlistSize,false);  
    var hts = document.getElementsByName("HITLIST_SIZE");
    for(var i=0; i < hts.length;i++) {    
        utils.addEvent(hts[i],"keyup",SetHitlistSize,false);  
    } 
    if($("psiInp")) {
        var numSubsets = $("psiInp").getAttribute("numSubsets");
        for(var i=1; i <= numSubsets;i++) {
            if ($("alnPos" + i)) InitToggleEvent($("alnPos" + i));  
            if ($("deflnG" + i)) InitToggleEvent($("deflnG" + i));
            if ($("deflnB" + i)) InitToggleEvent($("deflnB" + i));        
        }         
    }
}

function SetHitlistSize()
{
    var hts = document.getElementsByName("HITLIST_SIZE");
    for(var i=0; i < hts.length;i++) {    
        if(this != hts[i]) {
            hts[i].value = this.value;
        }
    }    
}
function InitToggleEvent(toggleNode)
{
    if(toggleNode) {
        var srcid = toggleNode.getAttribute("toggle");
        if(srcid) Toggle.addTarget(srcid, toggleNode);  
    }
} 				

function InitIFrameLinks()
{
    CheckIframe($("RSIFrameNoRes"),"prlink");
    CheckIframe($("RSIFrameDesc"),"prlink");
    CheckIframe($("RSIFrameAln"),"prlink");
}

function CheckIframe(iframe,contentElemID)
{
    if(!iframe) return;
    
    var iframeDoc;
    
    if(iframe.contentDocument) {//Firefox
        iframeDoc = iframe.contentDocument;                
    }
    else if (iframe.contentWindow) {//IE
        iframeDoc = iframe.contentWindow.document;                
    }
    else if(iframe.document) {
        iframeDoc = iframe.document;                
    }
    if(iframeDoc){        
        if(iframeDoc.getElementById(contentElemID)) {                        
            utils.addClass(iframe,"shown");
            utils.removeClass(iframe,"hidden");        
        }           
     }
}    


function InitHitMatrix()
{
    if($("bl2seImg")) {
    
        utils.addEvent($("hitmtImg"),"load",
                        function() {                              
						    utils.addClass($("bl2seImg"),"shown");
                            utils.removeClass($("bl2seImg"),"hidden");                  
                           
						}, 
						false);          
        utils.addEvent($("showHitMatrix"),"click",
                        function() {                            
                            $("hitmtImg").src= $("hitmtImg").getAttribute("imgsrc");
                            if(utils.hasClass($("htmb"),"shown")) {	                                
							    utils.addClass($("htmb"),"hidden");
                                utils.removeClass($("htmb"),"shown");                  
                            }
                            else {                                
                                utils.addClass($("htmb"),"shown");
                                utils.removeClass($("htmb"),"hidden");                  
                            }
						}, 
						false);          
        
        if($("blastSpec") && $("blastSpec").value=="GlobalAln") {            
            $("hitmtImg").src= $("hitmtImg").getAttribute("imgsrc");
        }        
    }   
}    
    
    
    
	
 				
function SetFormSubmitEvent()
{
    var el = $("refPage");
    if(el) {
	    SubmitEventNew("refPage");	
	}
	SubmitEventNew("frmPage");	
	el = $("searchOptions");
	if(el) {
	    SubmitEventNew("searchOptions");	
	}
	el = $("saveSearchOptions");
	if(el) {
	    SubmitEventNew("saveSearchOptions");	
	}
	//SubmitEventNew("breadCrSearchOptions");	
	list = $("queryList");
	if(list) {
        utils.addEvent(list,"change",GetResults,false);  
    }
    
    list = $("go");
	if(list) {
        utils.addEvent(list,"click",GetResults,false);  
    }
    
    
    list= $("onPageReformat");
    if(list) {
        utils.addEvent(list,"click",Reformat,false);  
    }

    
    InitToggleEvent($("refInfo"));
    InitToggleEvent($("resStat"));
    InitToggleEvent($("dbDetails"));
    InitToggleEvent($("graphicInfo"));
    InitToggleEvent($("descrInfo"));
    InitToggleEvent($("alignInfo"));
    InitToggleEvent($("ovrInfo"));        
    InitToggleEvent($("queryInfo"));        
    InitToggleEvent($("hitMatrixInfo"));            
    InitToggleEvent($("bl2ovrInfo"));    
    //Init only for PSI blastfse
    if($("prevRID")) InitPsiBlast();    
    InitSeqAlignLinks();
    InitAllCustomButtons();        
    if($("dnPSSMPar")) InitDownLoad(); 
    InitHitMatrix();
    if($("noRes")) {
        if($("hitCvs")) utils.addClass($("hitCvs"),"hidden");
        if($("hitText")) utils.addClass($("hitText"),"hidden");
    }
    InitIFrameLinks();
    showDbDetails(); //fill behind the scene    
    if ($("showDetails") && utils.hasClass($("showDetails"), "shown")) {
        utils.addEvent($("showDetails"), "click", showDbDetails, false);
    }
    initContentWidth();
}

function initContentWidth() {
    var lineLengthElem;
    if($("FormatForm")) lineLengthElem  = $("FormatForm").LINE_LENGTH;
    if (lineLengthElem) {
        var lineLength = parseInt(lineLengthElem[lineLengthElem.selectedIndex].value);
        if (parseInt(lineLengthElem.getAttribute("defval")) == lineLength) return;

        var charWidth = (navigator.userAgent.match(/ie/i)) ? 8 : 7;
        var minWidth = (lineLength + parseInt(17)) * charWidth;


        var alignView = $("FormatForm").ALIGNMENT_VIEW;
        var formatType = $("FormatForm").FORMAT_TYPE;
        var queryAnch = formatType[formatType.selectedIndex].value == "HTML" && (alignView[alignView.selectedIndex].value != "Pairwise" && alignView[alignView.selectedIndex].value != "PairwiseWithIdentities");

        var addWidth = (queryAnch) ? 250 : 350;

        minWidth = minWidth + parseInt(addWidth) + "px";
        jQuery($("content")).css("min-width", minWidth);
    }
    
}





function ShowHideAlnDeflines(alnID, checkbx) {
    var dflTableID = "dln_" + alnID;
    if ($(dflTableID)) {
        var rmClass, addClass;
        if (checkbx.checked) {
            rmClass = "hidden";
            addClass = "shown";
        }
        else {
            rmClass = "shown";
            addClass = "hidden";
        }
        var elems = $C(rmClass, "class", $(dflTableID), "tr");
        if (elems) {
            //alert(elems.length);
            for (var i = 0; i < elems.length; i++) {
                utils.removeClass(elems[i], rmClass);
                utils.addClass(elems[i], addClass);
            }
        }
    }
}

function SortAln(e, sortLink, sortItem) {
    var p = utils.getParent(sortLink);
    var p = utils.getParent(p);
    p_TD = utils.getParent(p);
    p_TR = utils.getParent(p_TD);
    if (utils.hasClass(p_TR, "dflnAln")) {
        p_TD.innerHTML = "Reading seqaligns...";
        var gi = p_TD.id.substr(2);
        var rid = p_TD.getAttribute("rid");
        getAlignSort(rid, gi, p_TD, sortItem);
        e = e || window.event;
        utils.preventDefault(e);
        return;
    }
    var links = document.getElementsByName("alnSort");
    if (links.length >= sortItem) {
        var href = links[sortItem].href.replace(new RegExp("selectAllTop.*(&|$)"), "");
        var hrefLn = sortLink.href.replace(new RegExp(".*#"), "");
        sortLink.href = href + hrefLn;
    }
}



var fullArr;
var numDbs;
function showDbDetails(e,dbSetIndex) 
{
    if (!($("dbPlusSpecies"))) return; //No org display
    if ($("dbPlusSpecies").getAttribute("init") == "on" && dbSetIndex == null) return;
    $("dbPlusSpecies").setAttribute("init", "on");
    
    dbInfoUrl = "getDBInfo.cgi";
    var rp = new RemoteDataProvider(dbInfoUrl);
    rp.minArr = 10;

    if (!fullArr) {
        var arr = $("results").DATABASE.value.split(" ");
        numDbs = arr.length;
        if (arr.length > rp.minArr) {
            fullArr = new Array();
            while (arr.length > 1) {
                var arrNew = arr.splice(0, rp.minArr); //does not include stopindex
                fullArr.push(arrNew);
            }
            if (!dbSetIndex) dbSetIndex = 0;
        }
    }

    rp.onSuccess = function(obj) {
        var navDB = document.createElement("div");
        if (fullArr) {
            var prevLink, nextLink, firstLink, lastLink;
            if (this.currDbSetIndex >= 1) {
                var firstStart = 1;
                var firstEnd = firstStart + fullArr[0].length - 1;
                firstLink = document.createElement("a");
                jQuery(firstLink).attr("href", "#");
                jQuery(firstLink).attr("id", "firstDbSet");
                jQuery(firstLink).attr("onclick", "showDbDetails(event,0);");
                jQuery(firstLink).attr("title", "Databases " + firstStart + "-" + firstEnd);
                jQuery(firstLink).html("First " + this.minArr + " dbs");

            }
            if (this.currDbSetIndex >= 1) {
                var prevStart = (this.currDbSetIndex - 1) * this.minArr + 1;
                var prevEnd = prevStart + fullArr[this.currDbSetIndex - 1].length - 1;
                prevLink = document.createElement("a");
                jQuery(prevLink).attr("href", "#");
                jQuery(prevLink).attr("id", "prevDbSet");
                jQuery(prevLink).attr("onclick", "showDbDetails(event," + (this.currDbSetIndex - 1) + ");");
                jQuery(prevLink).attr("title", "Databases " + prevStart + "-" + prevEnd);
                jQuery(prevLink).html("Prev " + this.minArr + " dbs");
            }

            if (this.currDbSetIndex < fullArr.length - 1) {
                var nextStart = (this.currDbSetIndex + 1) * this.minArr + 1;
                var nextEnd = nextStart + fullArr[this.currDbSetIndex + 1].length - 1;
                nextLink = document.createElement("a");
                jQuery(nextLink).attr("href", "#");
                jQuery(nextLink).attr("id", "nextDbSet");
                jQuery(nextLink).attr("onclick", "showDbDetails(event," + (this.currDbSetIndex + 1) + ");");
                jQuery(nextLink).attr("title", "Databases " + nextStart + "-" + nextEnd);
                jQuery(nextLink).html("Next " + this.minArr + " dbs");
            }
            if (this.currDbSetIndex < fullArr.length - 1) {
                var lastInd = fullArr.length - 1;
                var lastStart = numDbs - fullArr[lastInd].length;
                var lastEnd = numDbs;
                lastLink = document.createElement("a");
                jQuery(lastLink).attr("href", "#");
                jQuery(lastLink).attr("id", "lastDbSet");
                jQuery(lastLink).attr("onclick", "showDbDetails(event," + lastInd + ");");
                jQuery(lastLink).attr("title", "Databases " + lastStart + "-" + lastEnd);
                jQuery(lastLink).html("Last " + this.minArr + " dbs");
            }


            jQuery(navDB).attr("id", "addDbSet");
            if (firstLink) jQuery(navDB).append(firstLink);
            if (prevLink) jQuery(navDB).append(prevLink);
            if (lastLink) jQuery(navDB).append(lastLink);
            if (nextLink) jQuery(navDB).append(nextLink);
        }

        jQuery($("dbPlusSpecies")).html(navDB);
        jQuery(navDB).after(obj.responseText);
        if (fullArr) {
            var cap = jQuery($("dbSpecies")).find("caption");
            if (cap) {
                var currStart = (this.currDbSetIndex) * this.minArr + 1;
                var currEnd = currStart + fullArr[this.currDbSetIndex].length - 1;
                var capText = cap.html() + "<div class=\"cpAdd\"> Databases " + currStart + "-" + currEnd;
                cap.html(capText);
            }
        }
    };
    rp.onError = function(obj) {
        $("dbPlusSpecies").innerHTML += "error, requests:" + this.iActiveRequests + " status:" + obj.status;
    }
    var dbs;
    if (fullArr) {
        rp.currDbSetIndex = dbSetIndex;        
        var currArr = fullArr[dbSetIndex];
        dbs = currArr.join(",");
    }
    else {
        dbs = $("results").DATABASE.value.replace(/ /g, ",");
    }

    rp.Request("CMD=getDBOrg&DATABASE=" + dbs, "POST");
    if(e) utils.preventDefault(e);
}


function synchronizeCheck(id, formName, inputName, isChecked) {
    var numCheckBoxes = 0;
    var numChecked = 0;
    jQuery($("alignments")).find("input[name='getSeqGi']").each(function (index) {
        numCheckBoxes++;
        if (this.checked != isChecked && this.name == inputName && id == this.value) {//isChecked
            this.checked = isChecked;            
        }
        if (this.checked) numChecked++;
    });
    if ($("slcAlNum")) {
        var currSelNum = parseInt($("slcAlNum").innerHTML);
        var selNum = isChecked ? currSelNum + 1 : currSelNum - 1;
        enableDescrLinks(selNum, "topSeqLinks", "slcAlNum");
    }
    var selectAllCheck = (isChecked && numCheckBoxes == numChecked) ? true : false;    
    links = document.getElementsByName("selectAll");
    for (var i = 0; i < links.length; i++) {
        if (links[i] != this) links[i].checked = selectAllCheck;              
    }
}

/**********Functions moved from formatRes.js***************************/

function enableLinkForSelectedSeq(selNum, linkElem) 
{
    var minSelected = linkElem.getAttribute("minSlct");
    if(minSelected) {
        minSelected = parseInt(minSelected);
        if (selNum >= minSelected) {
            linkElem.removeAttribute("disabled");
        }
        else {
            linkElem.setAttribute("disabled", "disabled");
        }
    }        
}

function enableDescrLinks(selNum, toolbarID, selElID) {
    jQuery($(toolbarID)).find("a[minSlct]").each(function (index) {
        enableLinkForSelectedSeq(selNum, this);         
    });
    $(selElID).innerHTML = selNum;    
}

function SubmitToSeqViewer(e, seqList) {
    $("sbmtGraphics").action = $("seqViewUrl").value + $("seqViewPath").value;


    var rp = new RemoteDataProvider("url2nc.cgi");
    rp.onSuccess = function (obj) {
        var jsnResp = JSON.parse(obj.responseText);
        ncid = jsnResp.ncid;

        if (ncid != "") {
            $("seqViewParams").name = "rkey";
            $("seqViewParams").value = ncid;
        }
        else {
            initSeqViewerGet(seqList);
        }

        $("sbmtGraphics").submit();        //request-start jserror=NS_ERROR_FAILURE:  //jserrorline=1156  10 per day //
    };
    rp.onError = function (obj) {
        initSeqViewerGet(seqList);
        $("sbmtGraphics").submit();
        utils.preventDefault(e);
    }
    var params = $("ridParam").value + "[" + seqList + "]";
    rp.Request(params, "POST");
    utils.preventDefault(e);
}

utils.addEvent(window,
				"load", SetFormSubmitEvent,
				false);

jQuery(window).load(function () {
    if ($("kmerSearch") && $("kmerSearch").value == "true") {
        if ($("searchOptions")) jQuery("#searchOptions").hide();
        if ($("saveSearchOptions")) jQuery("#saveSearchOptions").hide();
    }
    if ($("msgFrm") && utils.hasClass($("msgFrm"), "hidetop")) {
        jQuery("#content").find("a.resLink").each(function (index) {
            jQuery(this).hide();
        });
        jQuery("#hnr").hide();
    }
});


/* If user agent has "safari" in it, include safari-specific stylesheet. */ 
if (navigator.userAgent.match(/safari/i) || navigator.userAgent.match(/opera/i)) {
document.write("<link rel='stylesheet' type='text/css' href='css/safari-descriptions.css'  media='screen'/>");
}
if (navigator.userAgent.match(/opera/i)) {    
document.write("<link rel='stylesheet' type='text/css' href='css/opera-descriptions.css'  media='screen'/>");
}
if (navigator.userAgent.match(/firefox/i) || navigator.userAgent.match(/safari/i)) {
document.write("<link rel='stylesheet' type='text/css' href='css/firefox-descriptions.css'  media='screen'/>");
}



