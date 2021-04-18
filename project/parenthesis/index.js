function copy(number) {
    const obj = document.getElementsByClassName("testcase-code")[number];
    
    const range = document.createRange();
    range.selectNode(obj.childNodes[0]);
    console.log(obj.childNodes[0]);

    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    document.execCommand("copy");
    sel.removeRange(range);
}

const copyButtons = document.getElementsByClassName("copy");
let count = 0;
for (copyButton of copyButtons){
    const a = count;
    const getCount = () => {
        return a;
    }
    copyButton.onclick = () => {
        copy(getCount());
    }
    count++;
}

