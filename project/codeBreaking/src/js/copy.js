export function copy($text) {
    const range = document.createRange();
    range.selectNode($text);

    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    
    document.execCommand("copy");
    sel.removeRange(range);
}