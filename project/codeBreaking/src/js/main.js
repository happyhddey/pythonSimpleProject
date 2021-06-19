import { GermanCode } from './codeGenerator.js'
import { copy } from './copy.js'

const charList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
const codeAlphabet = ["A", "D", "F", "G", "V", "X"]
const codeGenerator = new GermanCode(charList, codeAlphabet);

const originalText = "THEANSWERTOLIFETHEUNIVERSEANDEVERYTHING";
const $codebook = document.getElementsByClassName('codebook')[0];
$codebook.innerText = codeGenerator.getCodeBookStr();
const $code = document.getElementsByClassName('code')[0];
$code.innerText = codeGenerator.makeCode(originalText);

function RefreshCodeBook(){
    codeGenerator.updateCodeBook();
    const codebook = codeGenerator.getCodeBookStr();
    $codebook.innerText = codebook;
    $code.innerText = codeGenerator.makeCode(originalText);
}

function Refresh(delayTime){
    const id = setInterval(RefreshCodeBook, delayTime);
}

const $codebookBtn = document.getElementsByClassName('codebook-copy')[0];
$codebookBtn.onclick = () => {
    copy($codebook);
}

const $codeBtn = document.getElementsByClassName('code-copy')[0];
$codeBtn.onclick = () => {
    copy($code);
}

const delayTime = 10000;
Refresh(delayTime);
