function switchWritePreview(wname, tabname) {
    marked.setOptions({
            gfm:true,
            breaks:true,
            highlight: function(code, lang, callback) {
                if(hljs.getLanguage(lang)) {
                    return hljs.highlight(lang, code).value;
                }
                else {
                    return code;
                }
            }
        });
    var markdownText = document.getElementById('write-'+wname).value;
    var markdownHtml = marked(markdownText);
    var htmlClean = DOMPurify.sanitize(markdownHtml);
    document.getElementById('preview-'+wname).innerHTML = htmlClean;

    document.getElementById('write-'+wname).style.display = "none";
    document.getElementById('preview-'+wname).style.display = "none";
    document.getElementById('write-'+wname+'-But').classList.remove("active");
    document.getElementById('preview-'+wname+'-But').classList.remove("active");

    document.getElementById(tabname+'-'+wname).style.display = "block";
    document.getElementById(tabname+'-'+wname+"-But").classList.add("active");
}
